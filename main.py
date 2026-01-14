import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import requests
from dotenv import load_dotenv
import requests

load_dotenv()

def ask_ai_puter(question):
    url = "https://puter.ai/api/ask"
    try:
        response = requests.post(url, json={"query": question}, timeout=15)
        if response.status_code == 200:
            data = response.json()
            return data.get("answer", "[AI error] No answer found")
        else:
            return f"[AI error] {response.status_code}: {response.text}"
    except Exception as e:
        return f"[AI error] Network issue: {e}"





r = sr.Recognizer()

def callback(recognizer, audio):
    try:
        word = recognizer.recognize_google(audio)
        print(f"You said: {word}")
        # You can call process_command(word) here if you want
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"API error: {e}")

stop_listening = None
try:
    stop_listening = r.listen_in_background(sr.Microphone(), callback)
except Exception as e:
    print(f"Background listening disabled: {e}")
 
def speak(text):
    print(f"[speak] -> {text}")
    try:
        local_engine = pyttsx3.init()
        local_engine.say(text)
        local_engine.runAndWait()
        try:
            local_engine.stop()
        except Exception:
            pass
    except Exception as e:
        print(f"[speak] error: {e}")



def process_command(command):
    command = command.lower()
    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "wikipedia" in command:
        speak("Opening Wikipedia")
        webbrowser.open("https://www.wikipedia.org")

    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com/")

    elif "insta" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com/")

    elif "link" in command:
        speak("Opening linkdin")
        webbrowser.open("https://www.linkedin.com/feed/")

    elif "git" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com/AyanD-coder")
  
    # elif command in ("exit", "quit", "stop", "bye"):
    #     speak("Goodbye")
    #     exit()

    elif any(word in command for word in ("exit", "quit", "stop", "bye")):
        speak("Goodbye")
        exit()

    else:
        speak("Let me think...")
        answer = ask_ai_puter(command)
        speak(answer)

if __name__ == "__main__":
    print("Assistant is running... say something!")
    try:
        while True:
            time.sleep(0.1)
            try:
                # Listen for wake word
                with sr.Microphone() as source:
                    print("Listening......")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source, timeout=3, phrase_time_limit=6)
                word = r.recognize_google(audio)
                print("Recognising......")
                print(f"You said: {word}")

                if "hello" in word.lower()  or "alpha" in word.lower() or "hey" in word.lower():
                    speak("Hello Ayan, how can I help you?")
                    with sr.Microphone() as source:
                        print("Listening for command......")
                        audio = r.listen(source, timeout=3, phrase_time_limit=10)
                        command = r.recognize_google(audio)
                        print(f"You said: {command}")
                        process_command(command)

                elif "exit" in word.lower() or "quit" in word.lower() or "stop" in word.lower() or "bye" in word.lower():
                    speak("Goodbye")
                    break
                else:
                    print("Wake word not detected.")

            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception as e:
                print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Interrupted by user. Exiting...")
    finally:
        if stop_listening:
            try:
                stop_listening()
            except Exception:
                pass

          
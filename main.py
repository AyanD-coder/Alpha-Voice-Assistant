import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import time
from dotenv import load_dotenv

# load_dotenv()
# HF_TOKEN = os.getenv("HF_TOKEN")
# print("Token loaded:", HF_TOKEN[:10], "...")
# # def ask_ai_puter(question):
# #     url = "https://puter.ai/api/ask"
# #     try:
# #         response = requests.post(url, json={"query": question}, timeout=15)
# #         if response.status_code == 200:
# #             data = response.json()
# #             return data.get("answer", "[AI error] No answer found")
# #         else:
# #             return f"[AI error] {response.status_code}: {response.text}"
# #     except Exception as e:
# #         return f"[AI error] Network issue: {e}"


# def ask_ai_hf(question):
#     """Query Hugging Face API via router"""
#     url = "https://router.huggingface.com/api/models/gpt2"
#     headers = {"Authorization": f"Bearer {HF_TOKEN}"}
#     payload = {"inputs": question}
#     try:
#         response = requests.post(url, headers=headers, json=payload, timeout=15)
#         if response.status_code == 200:
#             data = response.json()
#             # Handle different response formats
#             if isinstance(data, list) and "generated_text" in data[0]:
#                 return data[0]["generated_text"]
#             elif isinstance(data, dict):
#                 return data.get("generated_text", str(data))
#             else:
#                 return str(data)
#         else:
#             return f"[HF error] {response.status_code}: {response.text}"
#     except Exception as e:
#         return f"[HF error] Network issue: {e}"



r = sr.Recognizer()
 
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
  
    

    elif any(word in command for word in ("exit", "quit", "stop", "bye")):
        speak("Goodbye")
        exit()

    # elif any(word in command for word in ("what", "who", "how", "why", "explain", "tell me about", "define")):
    #     speak("Let me think...")
    #     answer = ask_ai_puter(command)
    #     speak(answer)

    # else:
    #     speak("Let me think...")
    #     answer = ask_ai_hf(command)
    #     speak(answer)



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
                    speak("Hello Coder, how can I help you?")
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
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception as e:
                print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Interrupted by user. Exiting...")
    finally:
        print("Exiting.")

          
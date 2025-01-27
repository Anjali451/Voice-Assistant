import speech_recognition as sr
import pyttsx3
import webbrowser
from threading import Thread
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Initialize speech recognition and text-to-speech
engine = pyttsx3.init()
recognizer = sr.Recognizer()

# Global flag to keep the assistant active during a session
active_session = False

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Process commands
def processCommand(command):
    global active_session
    command = command.lower()
    if "open" in command:
        website = command.split("open")[-1].strip()
        speak(f"Opening {website}")
        if "youtube" in website:
            webbrowser.open("https://www.youtube.com")
        elif "google" in website:
            webbrowser.open("https://www.google.com")
        else:
            speak("I don't know that website. Opening Google instead.")
            webbrowser.open("https://www.google.com")
    elif "weather" in command:
        speak("I currently don't have weather functionality, but I can guide you to a weather website.")
        webbrowser.open("https://www.weather.com")
    elif "your name" in command:
        speak("I am Kitty, your assistant. You can call me Anjali's helper!")
    elif "stop listening" in command or "exit" in command or "quit" in command or "close this conversation" in command:
        speak("See you soon, have a nice day.")
        active_session = False
    else:
        speak("Sorry, I didn't understand that command.")

# Listen for commands
def listen():
    global active_session
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                if not active_session:
                    # Wait for wake word to activate session
                    print("Listening for wake word...")
                    status_label.config(text="Listening for wake word...", bootstyle=INFO)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                    command = recognizer.recognize_google(audio)
                    if "kitty" in command.lower():
                        active_session = True
                        speak("Namaste, how can I help you?")
                        status_label.config(text="Session active. Listening for commands...", bootstyle=SUCCESS)
                else:
                    # Listen continuously during an active session
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)
                    if not active_session:
                        status_label.config(text="Session ended. Listening for wake word...", bootstyle=INFO)
        except sr.UnknownValueError:
            continue
        except sr.WaitTimeoutError:
            continue
        except Exception as e:
            status_label.config(text=f"Error: {e}", bootstyle=DANGER)
            break

# Start voice assistant in a separate thread
def startAssistant():
    listen_thread = Thread(target=listen, daemon=True)
    listen_thread.start()

# Stop the voice assistant
def stopAssistant():
    global active_session
    active_session = False
    speak("Assistant stopped.")
    status_label.config(text="Assistant stopped.", bootstyle=WARNING)

# Create GUI
app = ttk.Window(themename="solar")
app.title("Voice Assistant")
app.geometry("500x400")
app.resizable(False, False)

# Heading
heading = ttk.Label(app, text="Voice Assistant", font=("Helvetica", 24, "bold"))
heading.pack(pady=20)

# Buttons
start_button = ttk.Button(app, text="Start Assistant", bootstyle=SUCCESS, command=startAssistant)
start_button.pack(pady=10)

stop_button = ttk.Button(app, text="Stop Assistant", bootstyle=DANGER, command=stopAssistant)
stop_button.pack(pady=10)

exit_button = ttk.Button(app, text="Exit", bootstyle=SECONDARY, command=app.quit)
exit_button.pack(pady=10)

# Status Label
status_label = ttk.Label(app, text="Assistant is idle.", font=("Helvetica", 12), bootstyle=INFO)
status_label.pack(pady=20)

# Footer
footer = ttk.Label(app, text="Created by Anjali Sinha", font=("Helvetica", 10, "italic"), bootstyle=LIGHT)
footer.pack(side=BOTTOM, pady=10)

# Run GUI loop
app.mainloop()

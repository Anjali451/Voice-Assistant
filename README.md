**#Voice Assistant**
-------------------
This project is a desktop-based voice assistant built using Python. It allows users to interact with the assistant through voice commands, such as opening websites, checking the weather, and more, with a seamless graphical user interface (GUI). Once the conversation starts, users can issue multiple commands without needing to repeat the wake word.
![Screenshot (54)](Voice-Assistant.jpg)

**Features**
-------------------
Hands-Free Interaction: Start the conversation with the assistant and give commands without repeating the wake word.
Smart Commands: Recognizes and processes commands such as opening websites and retrieving basic information.
Elegant GUI: Built using ttkbootstrap for a clean, modern look.
Customizable: Easily add or modify commands in the code.

**Technologies Used**
-------------------
Python Libraries:
speech_recognition for voice recognition.
pyttsx3 for text-to-speech synthesis.
webbrowser for launching websites.
ttkbootstrap for creating the GUI.
Multithreading: Ensures the GUI remains responsive while listening for commands.

**Usage**
-------------------
Launch the assistant using the "Start Assistant" button in the GUI.
Speak the wake word "Kitty" to activate the assistant.
Issue commands such as:
"Open YouTube"
"What is your name?"
"Exit" to stop the assistant.
Use the "Stop Assistant" button to end the conversation or "Exit" to close the program.

**Future Enhancements**
-------------------
Adding more intelligent features like weather forecasts, email integration, and music playback.
Improving natural language understanding for complex queries.
Implementing support for additional languages.

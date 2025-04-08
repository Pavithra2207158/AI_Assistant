import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import pyjokes
import random
import os

# Initialise text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    """Speak the given text"""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greet user based on time"""
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        greet = "Good morning"
    elif 12 <= hour < 18:
        greet = "Good afternoon"
    else:
        greet = "Good evening"
    speak(f"{greet}, Pavithra! How can I assist you today?")

def listen():
    """Capture voice input"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that")
        return ""

def play_music():
    """Play random music from a folder"""
    music_folder = "C:/Users/YourUsername/Music"  # Update this path
    songs = os.listdir(music_folder)
    if songs:
        song = random.choice(songs)
        os.startfile(os.path.join(music_folder, song))
        speak(f"Playing {song}")
    else:
        speak("No music found in your folder.")

def execute_command(command):
    """Process voice command"""
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")

    elif "search for" in command:
        query = command.replace("search for", "").strip()
        speak(f"Searching for {query}")
        pywhatkit.search(query)

    elif "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "").strip()
        try:
            summary = wikipedia.summary(topic, sentences=1)
            speak(summary)
        except wikipedia.exceptions.DisambiguationError:
            speak(f"Multiple results found for {topic}, please be more specific.")
        except wikipedia.exceptions.PageError:
            speak(f"Sorry, I couldn't find anything on {topic}.")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open gmail" in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)

    elif "play music" in command:
        play_music()

    elif "how are you" in command:
        speak("I'm doing great, thanks for asking!")

    elif "tell me something cool" in command:
        speak("Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old!")

    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a great day!")
        exit()

    else:
        speak("I didn't understand that command.")

# Main loop
greet_user()
while True:
    command = listen()
    if command:
        execute_command(command)




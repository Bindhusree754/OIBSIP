import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import sys

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """ Convert text to speech """
    print(f"Speaking: {text}")  # Debugging output
    engine.say(text)
    engine.runAndWait()

def listen():
    """ Listen to the user's voice and convert it to text """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")  # Debugging output
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError as e:
            print(f"Request error: {e}")
            return None

def respond_to_command(command):
    """ Respond to different commands """
    if command:
        command = command.lower()
        if "hello" in command:
            speak("Hello! How can I assist you today?")
        elif "time" in command:
            now = datetime.datetime.now()
            speak(f"The current time is {now.strftime('%H:%M')}.")
        elif "date" in command:
            now = datetime.datetime.now()
            speak(f"Today's date is {now.strftime('%Y-%m-%d')}.")
        elif "search" in command:
            query = command.replace("search", "").strip()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                speak(f"Searching for {query} on the web.")
            else:
                speak("What do you want to search for?")
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            sys.exit() 
        else:
            speak("Sorry, I didn't understand that command.")

def main():
    speak("Hello, I am your voice assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            respond_to_command(command)

if __name__ == "__main__":
    main()

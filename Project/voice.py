import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import pyaudio

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set properties for pyttsx3
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech input
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query.lower()

    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        speak("Sorry, I didn't get that.")
        return None

    except sr.RequestError:
        print("Sorry, the speech service is down.")
        speak("Sorry, the speech service is down.")
        return None

# Function to get answers from Wikipedia
def get_wikipedia_summary(query):
    try:
        # Search on Wikipedia and get a summary of the first result
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query was ambiguous, please be more specific: {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find anything on that topic."

# Function to execute basic commands and respond to conversations
def respond_to_command(query):
    if "good morning" in query:
        speak("Good morning to you too!")

    elif "good afternoon" in query:
        speak("Good afternoon! How can I help you today?")

    elif "good evening" in query:
        speak("Good evening! Hope you're having a great day.")

    elif "how are you" in query:
        speak("I'm just a program, but I'm functioning perfectly. How are you?")

    elif "your name" in query:
        speak("I am your personal assistant, here to help!")

    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")

    elif "open google" in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "play music" in query:
        music_dir = "C:/Users/YourName/Music"  # Change to your music folder path
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music")
        else:
            speak("No music found in the directory")

    elif "exit" in query or "quit" in query:
        speak("Goodbye!")
        exit()

    # If the query starts with "what is" or "who is", search Wikipedia
    elif "what is" in query or "who is" in query or "tell me about" in query:
        # Remove the "what is" or similar prefix and search for the topic
        topic = query.replace("what is", "").replace("who is", "").replace("tell me about", "").strip()
        speak(f"Searching Wikipedia for {topic}")
        summary = get_wikipedia_summary(topic)
        speak(summary)

    else:
        speak("Sorry, I don't know the answer to that yet.")

# Main loop for the assistant
if __name__ == "__main__":
    speak("Hello! How can I assist you today?")
    while True:
        command = take_command()
        if command:
            respond_to_command(command)

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import tkinter as tk
from tkinter import scrolledtext

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
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query was ambiguous, please be more specific: {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find anything on that topic."

# Function to execute basic commands and respond to conversations
def respond_to_command(query):
    response = ""
    if "good morning" in query:
        response = "Good morning to you too!"
    elif "good afternoon" in query:
        response = "Good afternoon! How can I help you today?"
    elif "good evening" in query:
        response = "Good evening! Hope you're having a great day."
    elif "how are you" in query:
        response = "I'm just a program, but I'm functioning perfectly. How are you?"
    elif "your name" in query:
        response = "I am your personal assistant, here to help!"
    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M")
        response = f"The current time is {current_time}"
    elif "open google" in query:
        response = "Opening Google"
        webbrowser.open("https://www.google.com")
    elif "play music" in query:
        music_dir = "C:/Users/vishv/Desktop/Music"  # Change to your music folder path
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
            response = "Playing music"
        else:
            response = "No music found in the directory"
    elif "exit" in query or "quit" in query:
        response = "Goodbye!"
        speak(response)
        exit()
    elif "what is" in query or "who is" in query or "tell me about" in query:
        topic = query.replace("what is", "").replace("who is", "").replace("tell me about", "").strip()
        response = f"Searching Wikipedia for {topic}"
        summary = get_wikipedia_summary(topic)
        response += f"\n{summary}"
    else:
        response = "Sorry, I don't know the answer to that yet."

    return response

# Function to handle button click
def on_button_click():
    command = take_command()
    if command:
        append_to_chat(f"You: {command}")
        response = respond_to_command(command)
        append_to_chat(f"Assistant: {response}")
        speak(response)

# Function to append text to the chat area
def append_to_chat(text):
    chat_area.config(state=tk.NORMAL)  # Enable the chat area for editing
    chat_area.insert(tk.END, text + "\n")  # Insert the text
    chat_area.config(state=tk.DISABLED)  # Disable editing
    chat_area.yview(tk.END)  # Auto-scroll to the end

# Create the GUI
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("500x400")

# Create a chat area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 12))
chat_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Create a button to start listening
button = tk.Button(root, text="Start Listening", command=on_button_click, font=("Arial", 14), bg="lightblue")
button.pack(pady=10)

# Run the GUI
if __name__ == "__main__":
    speak("Hello! How can I assist you today?")
    root.mainloop()

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Make sure Pillow is installed

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set properties for pyttsx3
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

# Function to make the assistant speak and display text in the GUI
def speak(text):
    engine.say(text)
    engine.runAndWait()
    display_text(f"Assistant: {text}")

# Function to display text in the output area of the GUI
def display_text(text):
    output_display.config(state=tk.NORMAL)
    output_display.insert(tk.END, text + "\n")
    output_display.config(state=tk.DISABLED)
    output_display.see(tk.END)

# Function to recognize speech input without displaying "Listening..." and "Recognizing..." in the GUI
def take_command():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio, language='en-in')
            display_text(f"You: {query}")
            return query.lower()

    except sr.UnknownValueError:
        speak("Sorry, I didn't get that.")
        return None
    except sr.RequestError:
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
import os

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
        music_dir = "C:/Users/vishv/OneDrive/Desktop/Music"  # Replace with your music folder path
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music")
        else:
            speak("No music found in the directory")
    elif "exit" in query or "quit" in query:
        speak("Goodbye!")
        root.quit()
    elif "what is" in query or "who is" in query or "tell me about" in query:
        topic = query.replace("what is", "").replace("who is", "").replace("tell me about", "").strip()
        speak(f"Searching Wikipedia for {topic}")
        summary = get_wikipedia_summary(topic)
        speak(summary)

    elif "open youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "weather" in query:
        speak("Please wait, fetching the current weather...")
        speak("The current weather is sunny with a temperature of 25 degrees Celsius.")
    
    elif "calculate" in query:
        speak("Please tell me the mathematical operation.")
        operation = take_command()
        try:
            result = eval(operation)
            speak(f"The result of {operation} is {result}")
        except Exception as e:
            speak("Sorry, I couldn't calculate that.")

    elif "set reminder" in query:
        speak("What would you like to be reminded about?")
        reminder_text = take_command()
        speak(f"Reminder set for: {reminder_text}. I’ll remind you soon.")

    elif "open notepad" in query:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open calculator" in query:
        speak("Opening Calculator")
        os.system("calc")
    
    elif "joke" in query:
        joke = "Why did the computer go to the doctor? Because it had a virus!"
        speak(joke)

    # New function to create a text file with "Hello World"
    elif "create text file" in query:
        speak("Please provide a name for the text file.")
        file_name = take_command().strip()

        # Validate file name (basic validation)
        if not file_name.endswith(".txt"):
            file_name += ".txt"  # Ensure the file has the .txt extension

        speak(f"Creating a new text file named {file_name}. Please wait.")
        
        # Default content for the text file
        content = "Hello World"

        # Save the content to the text file
        try:
            with open(file_name, 'w') as f:
                f.write(content)
            speak(f"Text file {file_name} has been created successfully with 'Hello World' text.")
        except Exception as e:
            speak(f"Sorry, I couldn't create the file. Error: {str(e)}")
    else:
        speak("Sorry, I don't know the answer to that yet.")


# Function to start listening for commands
def on_button_click():
    speak("Listening for your command...")
    command = take_command()
    if command:
        respond_to_command(command)

# Create the GUI
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("500x450")
root.config(bg="#f2f2f2")

# Add a logo
try:
    logo_image = Image.open("7.png")  # Replace with your logo image path
    logo_image = logo_image.resize((120, 120))
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo_photo, bg="#f2f2f2")
    logo_label.pack(pady=(20, 10))
except FileNotFoundError:
    display_text("Logo image not found. Please check the path.")

# Title Label
label = tk.Label(root, text="Your Personal Voice Assistant", font=("Arial", 16, "bold"), bg="#f2f2f2", fg="#333")
label.pack(pady=(10, 5))

# Button to start listening
button = tk.Button(root, text="Start Listening", command=on_button_click, font=("Arial", 14), bg="#4CAF50", fg="white", padx=20, pady=10)
button.pack(pady=(10, 20))

# Output display area
output_display = tk.Text(root, wrap=tk.WORD, height=12, font=("Arial", 12), state=tk.DISABLED, bg="#e6e6e6", fg="#333", relief="groove", bd=2)
output_display.pack(padx=20, pady=(0, 20), fill=tk.BOTH, expand=True)

# Run the GUI
if __name__ == "__main__":
    speak("Hello! How can I assist you today?")
    root.mainloop()

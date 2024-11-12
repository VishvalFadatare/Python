import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Increase duration if needed
        print("Listening... Please speak something.")
        
        try:
            audio = recognizer.listen(source, timeout=5)  # Added timeout to prevent hanging
            print("Audio captured. Processing...")
            # Use pocketsphinx for recognition
            query = recognizer.recognize_sphinx(audio)
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Could not request results from the recognition service.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")  # Catch all other exceptions
            return None

def answer_query(query):
    if query is None:
        return  # Don't proceed if no query was recognized

    if "good morning" in query.lower():
        speak("Good morning! How can I assist you today?")
    elif "what is global warming" in query.lower():
        speak("Global warming is the long-term heating of Earth's climate system due to human activities.")
    else:
        try:
            summary = wikipedia.summary(query, sentences=1)
            speak(summary)
        except Exception as e:
            print("Could not find information on that topic.")
            speak("I could not find information on that topic.")

if __name__ == "__main__":
    while True:
        query = take_command()
        answer_query(query)

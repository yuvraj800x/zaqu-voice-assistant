import speech_recognition as sr
import pyttsx3
import ollama


recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(text):
    print("zaqu:", text)
    engine = pyttsx3.init() 
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def ask_ai(question):
    print("zaqu thinking...")
    response = ollama.chat(
        model='phi3:mini',
        messages=[{'role': 'user', 'content': question}]
    )
    return response['message']['content']

def listner():
    print("listening...")
    with microphone as source:
        recognizer.energy_threshold = 300
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=7, phrase_time_limit=5)
    
    try:
        text = recognizer.recognize_google(audio, language="en-IN")  
        print("you said:", text)
        return text.lower()
    except:
        speak("could'nt understand ,speek again")
        return ""
def respond(text):
    commands = {
        "hello": "Hello! How are you?",
        "what is your name": "My name is zaqu!",
    }
    if text == "stop":
        speak("Goodbye! See you later!")
        return "bye"
    elif text in commands:
        speak(commands[text])
    else:
        ai_reply = ask_ai(text)
        speak(ai_reply)
   
while True:
    voice = listner()
    if voice != " ":
        if respond(voice) == "bye":
            break
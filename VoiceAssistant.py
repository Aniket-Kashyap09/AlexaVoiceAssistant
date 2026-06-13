import pyttsx3
import speech_recognition as sr 
import webbrowser
import datetime
import pyjokes
import os
import time #Used for time delea with the use of sleep function

""" -> Speech to Text Code(Structure) """
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print(" Not Understanding ")

# sptext()

""" -> Text to Speech(Speaker)"""

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) #For Male[0] Voice version by get and set property
    rate = engine.getProperty('rate') #rate for voice management
    engine.setProperty('rate', 150) #150 used for voice speed
    engine.say(x) #used for speak  
    engine.runAndWait() #first Listen and then speak

# speechtx("Hello Welcome to Aniket")

"""#used for dividing the uper code(Program) and Lower Code"""

if __name__ == '__main__':  #Used for set you assistant name

    command = sptext()
    if command and "alexa" in command.lower():
    # if sptext().lower() == "reacher": # Reacher his name
            # speechtx("Assistant started. Say something")
            while True:
                    # data1 = speechtx().lower() #using for lower case
                    #  data1 = sptext()   # ✅ correct function
                    # if data1 is None:
                    #     continue

                    # data1 = data1.lower()
                    data1 = sptext()
                    if data1 is None:
                        continue
                    data1 = data1.lower()
                
                    if "your name" in data1:
                        name = "my name is reacher"
                        speechtx(name)

                    elif "old are you" in data1:
                        age = "i am two year old"
                        speechtx(age)

                    elif "time" in data1:
                        # time = datetime.datetime.now().strftime("%I%M%p")
                        current_time = datetime.datetime.now().strftime("%I:%M %p")
                        print(current_time)
                        speechtx(current_time)

                    elif 'youtube' in data1:
                        webbrowser.open("https://www.youtube.com/") #Used for open youtube with the help of webbrowers module 
                    
                    elif 'ram' in data1:
                        webbrowser.open("https://www.linkedin.com/feed/")

                    elif 'google' in data1:
                        webbrowser.open("https://www.google.com/")
                    
                    elif "joke" in data1:
                        joke_1 = pyjokes.get_joke(language="en", category="neutral") #Show & speak jokes with the help of pyjokes module
                        print(joke_1)
                        speechtx(joke_1)
                    # elif 'play video' in data1:
                    #     adrs = "C:\Users\HP\Videos\Captures" 
                    #     listvideo = os.listdir(adrs) #Used for open system videos with the help of OS module
                    #     print(listvideo)
                    #     os.startfile(os.path.join(adrs, listvideo[0])) #Used for path and indexing for start the video

                    elif "exit" in data1:
                        speechtx("thank you") #Used for exit/stop Assistant
                        break
                    
                    # time.sleep(3) # 5sec delay
    else:
       print("Wrong Pronounciation! Thanks")

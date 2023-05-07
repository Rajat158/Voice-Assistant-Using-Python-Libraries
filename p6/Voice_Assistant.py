import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os


#Creating a variable to store the voice recognized data.
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#Functions is used to talk
def talk(text):
    engine.say(text)
    engine.runAndWait()

#Function is used for taking command from the owner.
def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening......')
        r.pause_threshold=1
        voice = listener.listen(source)
    try:
        print("Recognizing...")  
        command = listener.recognize_google(voice, language='en-in')  
        print(f"User said: {command}\n")
        command = command.lower()
        if 'janny' in command:
            command = command.replace('janny', '')
    except Exception as e:
        print("Say that again please............")
        return("None")
    return command

#Function is made for Greeting me every time.
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        talk("Good Morning Rajat")
    elif(hour>=12 and hour<18):
        talk("Good Afternoon Rajat")
    else:
        talk("Good evening Rajat")
    talk("I am janny, your virtual assistant. Sir how may i help you") 


# Function is used to run my voice commands but matching the words.
def run_ai():
    command = take_command()

    #For playing Song From YouTube
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    #For getting the current time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"Sir, the time is {time}")

    #For searching on wikipedia
    elif 'search' in command:
        talk('Searching Wikipedia...')
        person = command.replace('search', '')
        info = wikipedia.summary(person, sentences=2)
        talk("According to Wikipedia")
        print(info)
        talk(info)

    #For Searching on Google
    elif 'google' in command:
        webbrowser.open("https://www.google.com")

    #For Opening The Leetcode
    elif 'leetcode' in command:
        webbrowser.open("https://leetcode.com")
    
    #For Opening the GFG
    elif 'gfg' in command:
        webbrowser.open("https://www.geeksforgeeks.org")


#For some fun

    #Asking for date.
    elif 'date' in command:
        talk('sorry, I have a Boyfrien. But Thanks for offering.')

    #Asking for Boyfrind
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    #Asking for Collage Review
    elif 'college' in command:
        talk('Sir your collage is a worst collage i have seen in my whole life. you are so strong that you survived here.') 

    #Asking for a Joke
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again.')

#Running the command for one time
wishMe()
run_ai()

#=================================================
#Running the commands multiple times 

# while(True):
#     wishMe()
#     run_ai()

#For running multiple time uncomment the above part
#===================================================


#=============================
#Made BY-
#Rajat Gupta
#=============================

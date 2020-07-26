import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')#microsoft's speech api
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning")
    elif(hour>=12 and hour<18):
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak("hello! My name is Comp Assist and I am Aliasgar's Virtual assistant. How may I help you?")   
def takeCommand():
    '''
        it takes microphone input from the user and returns String output

    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        audio= r.listen(source)
    try:
        print("Recognising")
        query=r.recognize_google(audio,language='en-in')
        print(f'user said:{query}\n')

    except Exception :
       
        print('say that again please...')
        return 'None'
    return query

if __name__ == "__main__":
    
    wishMe()
    while True:
        query=takeCommand().lower()
        #logic for executing tasks based on the user input through microphone
        if("wikipedia" in query):
            speak('searching wikipedia')
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=4)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif('open youtube' in query ):
            webbrowser.open("youtube.com")
        elif('open google' in query ):
            webbrowser.open("google.com")
        elif('open classroom' in query):
            webbrowser.open('classroom.google.com')
        elif('open stack overflow' in query ):
            webbrowser.open("stackoverflow.com")
        elif('open skillrack' in query ):
            webbrowser.open("skillrack.com")
        elif('open hackerrank' in query):
            webbrowser.open('hackerrank.com')
        elif('open geeksforgeeks' in query ):
            webbrowser.open("geeksforgeeks.org")
        elif('the time' in query):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is{strTime}")
        elif('open(name of the program)' in query):
            codepath=#"file-path"
            os.startfile(codepath)
        elif('open (name of the proogram))' in query):
            codepath=#"file-path"
            os.startfile(codepath)
        
            
            
            


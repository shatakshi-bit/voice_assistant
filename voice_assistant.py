import pyttsx3
import datetime
import wikipedia
import webbrowser
import random
import os
import smtplib
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am V A . please tell me how may i help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold =500
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("yout email","your password")
    server.sendmail("your email",to,content)
    server.close()


if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
    #logic for implementing task accordinb to query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
           
        elif 'open google' in query:
            webbrowser.open('google.com')
       

        elif 'open psit ' in query:
            webbrowser.open('psit.ac.in')

        elif 'open command prompt' in query:
            os.system('start cmd')
            
       
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
       

        elif 'play music' in query:
            music_dir='C:\\Users\\vishn\\OneDrive\\Desktop\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,(len(songs)-1))]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H hours:%M minutes:%S seconds")
            print(strTime)
            speak(f"the time is{strTime}")

        elif 'visual studio code' in query:
            codePath="C:\\Users\\vishn\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak('what shoul i say?')
                content=takeCommand()
                to="email u want to sent to"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak('sorry my friend i am not able to send this email at the moment')
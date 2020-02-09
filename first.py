import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib


engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour <18:
        speak("good afternoon")
    else:
        speak("good evening")    

    speak("Hello I'm VERONICA how may i help you")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    ''' take command from microphone
    '''
    r=sr.Recognizer()
    with sr.Microphone as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("say that again")
        return "None"
    return query

def sentEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("k319kr@gmail.com","khush@31")
    server.sent("k319kr@gmail.com",to,content)
    server.close()



if __name__=="__main__":
    wishme()
    query=takecommand().lower()
#logics to execute the different tasks
    if wikipedia in query:
        speak("searching in wikipedia")
        query=query.replace("wikipedia"," ")
        results=wikipedia.summary(query,sentences=3)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif'open youtube' in query:
        webbrowser.open("youtube.com")
    elif'open google' in query:
        webbrowser.open("google.com")
    elif'open hakerrank' in query:
        webbrowser.open("hackerrank.com")
    elif'stack overflow' in query:
        webbrowser.open("stackoverflow.com")
    elif'weather'or 'temperature' in query:
        webbrowser.open("google.com")
    
   ''' elif 'play music ' in query:
        music_dir='D\\music\\downloads'
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    '''
    elif 'time enquiry ' in query:
        strTime=datetime.datetime.now().strftime('%H:%M:%S')
        speak(f"the time is {strTime}")

    elif 'code' in query:
        pathcode="C:\\Users\\home\\Downloads\\VSCode-win32-x64-1.37.1"
        os.startfile(pathcode)
    elif 'email' in query:
        try:
            speak("what should i say")
            content=takecommand()
            to="k319kr@gmail.com"
            sentEmail(to, content)
            speak("mail has been sent")
        except Exception as e:
            print(e)
            speak("sorry couldn't send the mail")
'''
this code is not working and we need to find the microphone connectivity for run the jarvis for me 
and there are some changes that been used
1 open as system is on and 
2 more interactive and connectivity through bluetooh too 
3 run all the devices
4 operate on all appliances in our house

'''
    
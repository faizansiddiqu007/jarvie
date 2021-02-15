import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init()
voices =engine.setProperty("rate", 169)

engine.setProperty('voices',voices)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning buddy")
    elif hour >= 12 and hour < 18:
        speak("good afternoon buddy")
    else:
        speak("good evening buddy")

    speak("hey! i am jarvie sir please tell me how can i help you")

def takecomand():

    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("listening..................")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing.....")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")
    except Exception as e:


        print("speak that again please....")
        return "none"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP(smtp.gmail.com ,587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com' , 'your- password here')
    server.sendmail('youremail@gmail.com' , to, content)
    server.close()


if __name__ == "__main__" :
    wishMe()
    while True :
        query = takecomand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open Youtube' in query:
            c = webbrowser.get('firefox')
            c.open('http://www.youtube.com')


        elif 'open google' in query:

            c = webbrowser.get('firefox')
            c.open('http://www.google.com')

        elif 'open instagram' in query:

            c = webbrowser.get('firefox')
            c.open('http://www.instagram.com')

        elif 'open stack overflow' in query:

            c = webbrowser.get('firefox')
            c.open('http://www.stackoverflow.com')

        elif 'the time' in query :

            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}")

        elif'send mails' in query :
            try:
                speak("what should i say")
                content = takecomand()
                to = "youremail@gmail.com"
                sendEmail(to,content)
                speak("email has been send!")

            except Exception as e :
                print(e)
                speak("sorry! i am not able to send the email")

        elif'quit' in query :
            exit()


















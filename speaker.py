import pyttsx3
while True:
    speak=pyttsx3.init()
    a=input('choose either male or female voice=')
    if a.lower()=='female':
        voi=speak.getProperty('voices')
        speak.setProperty('voice',voi[1].id)
        break
    elif a.lower()=='male':
        break
    else:
        print('enter again')
speak.setProperty('rate',150)
word=input('Enter the sentence you want to say=')
speak.say(word)
speak.runAndWait()

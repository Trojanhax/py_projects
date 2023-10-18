import pyttsx3

while True:
    ur = input('Enter your text (or "q" to quit): ')
    if ur == "q":
        print('Goodbye!')
        break
    else:
        engine = pyttsx3.init()
        engine.say(ur)
        engine.runAndWait()

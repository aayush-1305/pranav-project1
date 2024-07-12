import pyttsx3
print('welcome to voice speaker')
engine = pyttsx3.init()
while True:
    cmd = input("Enter Command: ")
    if cmd == 'exit':
        print("Bye bye friend ")
        engine.say("Bye bye friend ")
        engine.runAndWait()
        break
    engine.say(cmd)
    engine.runAndWait()



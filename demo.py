import  speech_recognition as s

def take_query():
    sr=s.Recognizer()
    print("Say Somthing")
    #reco.. class has two method listen() and recognizer_google(audio , clip , target lang)
    with s.Microphone() as n:
     try:
        audio=sr.listen(n)
        sr.adjust_for_ambient_noise(n,duration=5)
        text=sr.recognize_google(audio,language='eng-IN')
        # return_google method may give generally 2 exceptions
        # 1.request error nd they did when  internet is not available
        # 2.unknown value error nd they give  when google is not understand the user audio
        # exception by listen()
        # 1.wait time out error
        # 2.ambient noise
        return text
     except:
         print("Exeption occured")

print("You said:",take_query())
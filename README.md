# Speech_to_text
this code helps &amp; enables to convert the speech by the user to text by installing the library called SpeechRecognition.
 
CODE:

import speech_recgonition as sr
r = sr.Recogizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = sr.listen(source)
try :
    note = sr.recognize_google(audio)
    print("you said:", note)
except sr.UnknownValueError :
    print("Could not undersatnd:")
except sr.RequestError as e:
    print("Could not Request: {0}".format(e))

#!/usr/bin/env python
# coding: utf-8

# In[14]:


import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)
try :
    note = r.recognize_google(audio)
    print("you said:", note)
except sr.UnknownValueError :
    print("Could not undersatnd:")
except sr.RequestError as e:
    print("Could not Request: {0}".format(e))


# In[ ]:





# In[ ]:





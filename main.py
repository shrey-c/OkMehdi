from nltk import word_tokenize
from nltk.corpus import stopwords
import nltk
import simpleaudio as sa
import speech_recognition as sr
from os import system
import requests
import webbrowser as wb
from datetime import datetime
from myemailpro import sendemail
from contacts import mycontacts
from currecyexchange import convert, allcurrencies
import country_feature
from interactive_dictionary import giveMeaningOfWord

"""
sentence = "What is the weather in Chicago?"
tokens = word_tokenize(sentence)
stop_words = set(stopwords.words('english'))
clean_tokens = [w for w in tokens if not w in stop_words]
tagged = nltk.pos_tag(clean_tokens)
print(nltk.ne_chunk(tagged))
"""



def play_audio():
    wave_obj = sa.WaveObject.from_wave_file("beep-3.wav")
    p = wave_obj.play()
    p.wait_done()

def getLocalTime():
    hour = str(datetime.now().hour)
    minute = str(datetime.now().minute)
    d = datetime.strptime(hour+":"+minute, "%H:%M").strftime("%I:%M %p")
    return d

def listenAndReturn():
    while True:
        play_audio()
        with mic as source:
            audio = r.listen(source)
        try:
            b = r.recognize_google(audio)
            return b
        
        except sr.UnknownValueError:
            speak("Please could you say that again")
        except sr.RequestError as e:
            print(e)
            speak("Please could you say that again")

def emailFunction():
    from_addr = "wimpycat714@gmail.com"
    speak("who do you want to send to?")
    to_addr = mycontacts[listenAndReturn().lower()]
    speak("subject?")
    subject = listenAndReturn()
    speak("body?")
    body = listenAndReturn()
    try:
        sendemail(from_addr    = from_addr, 
            to_addr = to_addr,
            cc_addr_list = [], 
            subject      = subject, 
            message      = body, 
            login        = 'wimpycat714@gmail.com', 
            password     = 'temppassword123')
        speak("the mail was sent successfully")
    except:
        speak("Oops, there was a problem sending the mail")

def currencyFunction(query):
    speak("okay, please wait...")
    value = [int(s) for s in query.split() if s.isdigit()][0]
    from_country = query[(query.index('to') - 4) : (query.index('to') - 1)]
    to_country = query[(query.index('to')) + 3 : ]
    a = convert(value, from_country.upper(), to_country.upper())
    if a=="Error":
        speak("There was a problem converting the currency")
    else:
        speak("It is equal to " + a + " indian rupees")

def speak(s):
    print(s)
    system("say " + s)

def jarvis(query):
    tokens = word_tokenize(query)
    stop_words = set(stopwords.words('english'))
    clean_tokens = [w for w in tokens if not w in stop_words]

    if query.lower() == "what is your name":
        speak("My name is Jarvis")
    elif "I" and "send" and "email" in clean_tokens:
        emailFunction()
    elif 'convert' in query.lower():
        currencyFunction(query.lower())
    
    # capital
    elif 'capital' in query.lower() and (tokens[-1] in [i[1] for i in country_feature.countries] or tokens[-2]+" "+tokens[-1] in [i[1] for i in country_feature.countries] or clean_tokens[-3]+" "+tokens[-2]+" "+tokens[-1] in [i[1] for i in country_feature.countries]):
        countryAlphaCode = ""
        country = ""
        for i in country_feature.countries:
            if (i[1] == tokens[-1]) or (i[1] == tokens[-2]+" "+tokens[-1]) or (i[1] == tokens[-3]+" "+tokens[-2]+" "+tokens[-1]):
                country = i[1]
                countryAlphaCode = i[0]
                break
        try: 
            captial = country_feature.returnCapital(countryAlphaCode)
            speak("The capital of " + country + " is " + captial)
        except:
            speak("Sorry, i dont know")
    
    # calling code
    elif 'calling code' in query.lower() and (tokens[-1] in [i[1] for i in country_feature.countries] or tokens[-2]+" "+tokens[-1] in [i[1] for i in country_feature.countries] or clean_tokens[-3]+" "+tokens[-2]+" "+tokens[-1] in [i[1] for i in country_feature.countries]):
        countryAlphaCode = ""
        country = ""
        for i in country_feature.countries:
            if (i[1] == tokens[-1]) or (i[1] == tokens[-2]+" "+tokens[-1]) or (i[1] == tokens[-3]+" "+tokens[-2]+" "+tokens[-1]):
                country = i[1]
                countryAlphaCode = i[0]
                break
        try: 
            calling_code = country_feature.returnCallingCode(countryAlphaCode)
            speak("The calling code of " + country + " is " + " ".join(str(calling_code)))
        except:
            speak("Sorry, i dont know")
    
    # currency used in a country
    elif 'currency' in query.lower() and (tokens[-1] in [i[1] for i in country_feature.countries] or tokens[-2]+" "+tokens[-1] in [i[1] for i in country_feature.countries] or clean_tokens[-3]+" "+tokens[-2]+" "+tokens[-1] in [i[1] for i in country_feature.countries]):
        countryAlphaCode = ""
        country = ""
        for i in country_feature.countries:
            if (i[1] == tokens[-1]) or (i[1] == tokens[-2]+" "+tokens[-1]) or (i[1] == tokens[-3]+" "+tokens[-2]+" "+tokens[-1]):
                country = i[1]
                countryAlphaCode = i[0]
                break
        try: 
            currency = country_feature.returnCurrency(countryAlphaCode)
            speak("The currency of " + country + " is " + currency)
        except:
            speak("Sorry, i dont know")

    # population
    elif 'population' in query.lower() and (tokens[-1] in [i[1] for i in country_feature.countries] or tokens[-2]+" "+tokens[-1] in [i[1] for i in country_feature.countries] or clean_tokens[-3]+" "+tokens[-2]+" "+tokens[-1] in [i[1] for i in country_feature.countries]):
        countryAlphaCode = ""
        country = ""
        for i in country_feature.countries:
            if (i[1] == tokens[-1]) or (i[1] == tokens[-2]+" "+tokens[-1]) or (i[1] == tokens[-3]+" "+tokens[-2]+" "+tokens[-1]):
                country = i[1]
                countryAlphaCode = i[0]
                break
        try: 
            population = country_feature.returnPopulation(countryAlphaCode)
            speak("The population of " + country + " is " + str(population))
        except:
            speak("Sorry, i dont know")        

    elif query.lower() == "what is the capital of uae" or query.lower() in "capital of uae":
        speak("The capital of UAE is Abu Dhabi")
    elif query.lower() == "what is the capital of india" or query.lower() in "capital of india":
        speak("The capital of India is New Delhi")
    elif query.lower() in "what is the time":
        speak("It is " + getLocalTime())
    
    # give meaning of a word
    elif ('define' in query.lower()) and len(query.split()) == 2:
        definition = giveMeaningOfWord(query[7:])
        speak(definition)

    elif 'close' and 'application' in word_tokenize(query):
        speak("Closing application, please wait")
        quit()

    else:
        pass
#        url = "http://www.google.com/search?q="+query
#        wb.open(url)
#        speak("Here are some results from google")
#        quit()


r = sr.Recognizer()
mic = sr.Microphone(device_index=0)
while True:
    play_audio()
    with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        a = r.recognize_google(audio)
        print(a)
        jarvis(a)

    except sr.UnknownValueError:
        print("Sorry, Could not understand you")
        system("say Sorry, Could not understand you")
    except sr.RequestError as e:
        print("Sorry, Could not understand you")
        system("say Sorry, Could not understand you")

import pyttsx3
import requests
import json
import speech_recognition as srg
r = srg.Recognizer()

    

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",115)

API_KEY = "368351d19e2e048d089a5fcebc4d0c68"

while True:
    print("enter city name:",end='')
    with srg.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        city = r.recognize_google(audio)
        city = city.lower()
        print(city)

    URL = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_KEY

    res = requests.get(URL)
    if res.status_code ==200:
        data = res.json()
        main = data["main"]

        temprature = main["temp"]
        humidity = main["humidity"]
        wind_speed = data["wind"]
        report = data["weather"]
        tempra=float(temprature)-273
        tempra = round(tempra,2)

        print(f"City ID:{data['id']}")
        engine.say(f"City ID:{data['id']}")
        print(f"temprature:{tempra}")
        engine.say(f"temprature: {tempra}"+"degree celcius")
        print(f"humidity: {humidity}")
        engine.say(f"humidity: {humidity}")
        print(f"wind speed: {wind_speed['speed']}"+" mtr/sec")
        engine.say(f"wind speed: {wind_speed['speed']}"+"meter per second")
        print(f"weather report: {report[0]['description']}")
        engine.say(f"weather report: {report[0]['description']}")
        engine.runAndWait()
    else:
        print("city not found!")
        engine.say("city not found!")
        engine.runAndWait()




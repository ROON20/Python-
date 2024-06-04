import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time
import smtplib
import requests
import json
import sched

# Initialize the scheduler
scheduler = sched.scheduler(time.time, time.sleep)

# Function to capture voice input
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Did not understand")
            return ""

# Function to convert text to speech
def speechtx(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)  # Set to a reasonable speed
    engine.say(text)
    engine.runAndWait()

# Function to send an email
def send_email(to_address, subject, message):
    from_address = 'your-email@gmail.com' #enter your email add
    password = 'your-password'  #enter your email password
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, password)
        email_message = f'Subject: {subject}\n\n{message}'
        server.sendmail(from_address, to_address, email_message)
        server.close()
        speechtx("Email has been sent successfully.")
    except Exception as e:
        print(e)
        speechtx("Sorry, I was unable to send the email.")

# Function to get weather updates
def get_weather():
    api_key = 'your-openweather-api-key'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = 'your-city'
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speechtx(f"Temperature: {current_temperature}°C\nDescription: {weather_description}")
    else:
        speechtx("City not found.")

# Function to set a reminder
def set_reminder(reminder_time, reminder_message):
    def reminder():
        speechtx(f"Reminder: {reminder_message}")
    
    reminder_time_struct = time.strptime(reminder_time, '%H:%M')
    reminder_epoch = time.mktime(reminder_time_struct)
    current_epoch = time.time()
    delay = reminder_epoch - current_epoch
    if delay > 0:
        scheduler.enter(delay, 1, reminder)
        scheduler.run()
    else:
        speechtx("The reminder time has already passed.")

if __name__ == '__main__':
    speechtx("Hi, I'm Ron. How can I help you today?")
    while True:
        data = sptext().lower()
        if "hi ron" in data:
            speechtx("Hello, how can I help you?")
        
        elif "your name" in data:
            name = "My name is Ron."
            speechtx(name)

        elif "old are you" in data:
            age = "I am twenty one years old."
            speechtx(age)

        elif "time" in data:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speechtx(f"The time is {current_time}")

        elif "youtube" in data:
            speechtx("Opening YouTube")
            webbrowser.open("https://www.youtube.com/")

        elif "send email" in data:
            speechtx("What is the recipient's email address?")
            to_address = sptext().lower()
            speechtx("What is the subject?")
            subject = sptext().lower()
            speechtx("What is the message?")
            message = sptext().lower()
            send_email(to_address, subject, message)

        elif "weather" in data:
            get_weather()

        elif "reminder" in data:
            speechtx("At what time should I set the reminder? Please specify in HH:MM format.")
            reminder_time = sptext().lower()
            speechtx("What is the reminder message?")
            reminder_message = sptext().lower()
            set_reminder(reminder_time, reminder_message)

        elif "stop" in data:
            speechtx("Thank you. Goodbye!")
            break
        
        time.sleep(5)
else:
    print("Thanks")

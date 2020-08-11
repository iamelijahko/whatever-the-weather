from flask import Flask
import requests
from datetime import datetime
import smtplib   # built-in module for sending emails

# API call: London (latitude: 51.5085, longitude: -0.1257), get the key from your account at OpenWeather.com
url = 'https://api.openweathermap.org/data/2.5/onecall?lat=51.5085&lon=-0.1257&appid={API_key}&units=metric'


# Get weather data from the above url
def get_weather():
    data = requests.get(url)
    if data:
        weather_data = data.json()  # arrange data in json format
        city = weather_data['timezone']
        timestamp = weather_data['hourly'][3]['dt']  # After 2 hours
        time = datetime.fromtimestamp(timestamp)  # convert timestamp into 2020-08-07 12:00:00 format (datetime object)
        temp_celsius = weather_data['hourly'][3]['temp']
        humidity = weather_data['hourly'][3]['humidity']
        weather_main = weather_data['hourly'][3]['weather'][0]['main']  # weather main description
        weather_description = weather_data['hourly'][3]['weather'][0]['description']  # weather detail description
        icon = weather_data['hourly'][3]['weather'][0]['icon']  # refer to icons in "weather_icons" folder
        final = (city, time, temp_celsius, humidity, weather_main, weather_description, icon)
        return final
    else:
        return None

    
# Send an alert message to your email
def send_mail(this_temp):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "sender@gmail.com"  # replace with your own email
    receiver_email = "receiver@gmail.com"  # replace with your own email
    password = "abcd1234efgh5678"  # replace with Google App passwords (16 characters)
    text = f'Subject: HOT SPELL ALERT!\nTemperature in 2 hours will be {this_temp}.\nStay cool and drink more water!'
    smtplibObj = smtplib.SMTP(smtp_server, port)  # 587 for STARTTLS connection. 465 for SSL/TLS connection
    smtplibObj.ehlo()  # say hello to the gmail server
    smtplibObj.starttls()  # in case a problem occurs
    smtplibObj.login(sender_email, password)
    smtplibObj.sendmail(sender_email, receiver_email, text)
    smtplibObj.quit()
    print("Warning message sent to mailbox!")


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route("/ifttt", methods=["POST"])
def handler():
    print("Message sent successfully from IFTTT")  # check if mail is sent from pythonanywhere.com, please refer to Web > Log Files > Serve log > click yourUserName.pythonanywhere.com.server.log
    weather = get_weather()
    if weather:
        if weather[2] >= 30.0:  # temperature condition in Celsius
            send_mail(weather[2])
    return ""

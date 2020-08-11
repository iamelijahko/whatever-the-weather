from flask import Flask
import requests
from datetime import datetime
import smtplib

url = 'https://api.openweathermap.org/data/2.5/onecall?lat=51.5085&lon=-0.1257&appid=b25d29248e9e6d670095320c14eb6e4b&units=metric'


def get_weather():
    data = requests.get(url)
    if data:
        weather_data = data.json()  # data in json format
        city = weather_data['timezone']
        timestamp = weather_data['hourly'][3]['dt']  # After 2 hours after weather
        time = datetime.fromtimestamp(timestamp)  # returns the local date and time (datetime object)
        temp_celsius = weather_data['hourly'][3]['temp']
        humidity = weather_data['hourly'][3]['humidity']
        weather_main = weather_data['hourly'][3]['weather'][0]['main']
        weather_description = weather_data['hourly'][3]['weather'][0]['description']
        icon = weather_data['hourly'][3]['weather'][0]['icon']
        final = (city, time, temp_celsius, humidity, weather_main, weather_description, icon)
        return final
    else:
        return None


def send_mail(this_temp):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "iamelijahko@gmail.com"
    receiver_email = "elijah.ko@network.rca.ac.uk"
    password = "hkgnyqtgytcpdwpo"
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
    print("Message sent succefful from IFTTT")
    weather = get_weather()
    if weather:
        send_mail(weather[2])
    return ""

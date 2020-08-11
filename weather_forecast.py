from tkinter import *  # Tkinter is a standard library to create GUI application in Python. Here we import everything.
from configparser import ConfigParser  # pass API key from config.ini file to here
import requests
from datetime import datetime
from geopy.geocoders import Nominatim
import smtplib  # built-in module for sending emails

url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}&units=metric'

# read and get API key
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if city_entry.get() == 'Enter a city name ...':
        city_entry.delete(0, "end")  # delete all the text in the entry
        city_entry.insert(0, '')  # Insert blank for user input
        city_entry.config(font=("Helvetica", 14), fg='#1c1c1c')


def email_alert(this_city, this_temp):
    # define the SMTP server:
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "iamelijahko@gmail.com"
    receiver_email = "elijah.ko@network.rca.ac.uk"
    password = "hkgnyqtgytcpdwpo"
    text = f'Subject: Python: Hot weather warning\n{this_city} will be BOILING in 3 hours!\nTemperature will be {this_temp} degree Celsius.\nRemember to drink more water!'
    smtplibObj = smtplib.SMTP(smtp_server, port)  # 587 for STARTTLS connection. 465 for SSL/TLS connection
    smtplibObj.ehlo()  # say hello to the gmail server
    smtplibObj.starttls()  # in case a problem occurs
    smtplibObj.login(sender_email, password)
    smtplibObj.sendmail(sender_email, receiver_email, text)
    smtplibObj.quit()
    print('Email sent!')


def get_weather(city):
    # convert city name to latitude and longitude
    geolocator = Nominatim(user_agent='location_application')
    location = geolocator.geocode(city)
    latitude = location.latitude
    longitude = location.longitude
    # pass all values to url
    data = requests.get(url.format(latitude, longitude, api_key))
    if data:
        weather_data = data.json()  # data in json format
        city = weather_data['timezone']
        timestamp = weather_data['hourly'][4]['dt']  # after 3 hours
        time = datetime.fromtimestamp(timestamp)  # returns the local date and time (datetime object)
        temp_celsius = weather_data['hourly'][4]['temp']
        humidity = weather_data['hourly'][4]['humidity']
        weather_main = weather_data['hourly'][4]['weather'][0]['main']
        weather_description = weather_data['hourly'][4]['weather'][0]['description']
        icon = weather_data['hourly'][4]['weather'][0]['icon']
        final = (city, time, temp_celsius, humidity, weather_main, weather_description, icon)
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_label['text'] = f'{weather[0]}'
        time_label['text'] = f'At {weather[1]}'
        weather_icon['bitmap'] = f'weather_icons/{weather[6]}.png'
        weather_details['text'] = f'{weather[4]}, {weather[5]}'
        humidity_label['text'] = f'Humidity: {weather[3]}%'
        if weather[2] < 5.0:
            temperature_label['text'] = '{:.2f}°C, Freezing'.format(weather[2])
        elif 5.0 <= weather[2] < 15.0:
            temperature_label['text'] = '{:.2f}°C, Cold'.format(weather[2])
        elif 15.0 <= weather[2] < 25.0:
            temperature_label['text'] = '{:.2f}°C, Warm'.format(weather[2])
        elif 25.0 <= weather[2] < 30.0:
            temperature_label['text'] = '{:.2f}°C, Hot'.format(weather[2])
        elif weather[2] >= 30.0:
            temperature_label['text'] = '{:.2f}°C, Boiling'.format(weather[2])
            # Send email alert
            email_alert(weather[0], weather[2])  # city, temperature


app = Tk()  # create an app as Tk()
app.title("WeatherForecast.app")
app.geometry('500x500')

# entry box
city_text = StringVar()  # user entry, city name
city_entry = Entry(app, textvariable=city_text)  # Entry( master, option, ... )
city_entry.insert(0, 'Enter a city name ...')
city_entry.config(fg='#bfbfbf', font=("Helvetica", 14))
city_entry.bind('<FocusIn>', on_entry_click)  # delete temporary text and insert entry text
city_entry.pack()  # place it on screen

# button
search_button = Button(app, text='Forecast in 3 hours', width=20, command=search, font=("Helvetica", 14), fg='#2c419e')
search_button.pack()

# label - city
location_label = Label(app, text='', font=("Helvetica", 20, "bold"), fg='#2c419e')
location_label.pack()

# label - time
time_label = Label(app, text='', font=("Helvetica", 20, "bold"), fg='#2c419e')
time_label.pack()

# label - weather icon
weather_icon = Label(app, bitmap='')
weather_icon.pack()

# label - weather description
weather_details = Label(app, text='', font=("Helvetica", 14), fg='#2c419e')
weather_details.pack()

# label - temperature
temperature_label = Label(app, text='', font=("Helvetica", 20), fg='#2c419e')
temperature_label.pack()

# label - humidity
humidity_label = Label(app, text='', font=("Helvetica", 16), fg='#2c419e')
humidity_label.pack()

app.mainloop()  # infinite loop used to run the application

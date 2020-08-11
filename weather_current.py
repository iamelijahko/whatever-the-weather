import tkinter as tk
from tkinter import messagebox
from configparser import ConfigParser  # pass API key from .ini file to here
import requests

# API calls from open weather
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

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


def get_weather(city):
    data = requests.get(url.format(city, api_key))
    if data:
        weather_data = data.json()  # data in json format
        city = weather_data['name']
        country = weather_data['sys']['country']
        temp_kelvin = weather_data['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
        humidity = weather_data['main']['humidity']
        icon = weather_data['weather'][0]['icon']
        weather_main = weather_data['weather'][0]['main']
        weather_description = weather_data['weather'][0]['description']
        final = (city, country, temp_celsius, temp_fahrenheit, humidity, icon, weather_main, weather_description)
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_label['text'] = f'{weather[0]}, {weather[1]}'  # city, country
        weather_icon['bitmap'] = f'weather_icons/{weather[5]}.png'  # icon
        temperature_label['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])  # temp_celsius, temp_fahrenheit
        weather_details['text'] = f'{weather[6]}, {weather[7]}'  # weather_main, weather_description
        humidity_label['text'] = f'Humidity: {weather[4]}%'  # humidity
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))


app = tk.Tk()  # create an app as Tk()
app.title("CurrentWeather.app")
app.geometry('500x500')

# entry box
city_text = tk.StringVar()  # user entry, city name
city_entry = tk.Entry(app, textvariable=city_text)  # Entry( master, option, ... )
city_entry.insert(0, 'Enter a city name ...')
city_entry.config(fg='#bfbfbf', font=("Helvetica", 14))
city_entry.bind('<FocusIn>', on_entry_click)  # delete temporary text and insert entry text
city_entry.pack()  # place it on screen

# button
search_button = tk.Button(app, text='Search current weather', width=20, command=search, font=("Helvetica", 14), fg='#2c419e')
search_button.pack()

# label - city
location_label = tk.Label(app, text='', font=("Helvetica", 20, "bold"), fg='#2c419e')
location_label.pack()

# label - weather icon
weather_icon = tk.Label(app, bitmap='')
weather_icon.pack()

# label - weather details
weather_details = tk.Label(app, text='', font=("Helvetica", 14), fg='#2c419e')
weather_details.pack()

# label - temperature
temperature_label = tk.Label(app, text='', font=("Helvetica", 20), fg='#2c419e')
temperature_label.pack()

# label - humidity
humidity_label = tk.Label(app, text='', font=("Helvetica", 16), fg='#2c419e')
humidity_label.pack()

# infinite loop used to run the application
app.mainloop()

# Hot Spell Expelliarmus - Your personal heatwave alert ♨️📱</h1>
### Author: Elijah Ko</h2>

Now that lockdown is continuing to ease, we're excited about the prospect of enjoying, safely, more of the great outdoors this summer. That also means a return to the very British hobby of getting sun tanning 🔆 in the parks 🏞 !

However, even if you can enjoy the weather and manage social distancing, you could be vulnerable to *heat exhaustion* 🥵 . Particularly the elderly, people with conditions such as diabetes, young children and people working or exercising outdoors. Heat-stroke may set in which requires urgent medical help.

###### Reference: https://www.bbc.co.uk/news/world-44937692?fbclid=IwAR0-Gwn56dI3zLNJpmcAFe5-rggRwHClo0LZMyxZuV5yt0BvqRkS7vI-8LA

## What if ... you can receive a hot spell warning once you step into your favourite local parks?

The project can be broken down into five main sections:

### 1. Trigger an IFTTT command once you step into the park (IF "Location" THEN "Webhooks")
###### Video instruction: https://youtu.be/0aIHCevDfS4

IF THIS - "Location" widget

Select *"You enter an area"*, this triggers everytime you enter an area you specify. In my case, I have chosen the Roundwood Park.

THEN THAT - "Webhooks" widget

##### URL field, fill in "*https://yourAccountName.pythonanywhere.com/ifttt*"
##### Method: POST (optional)
##### Content Type: text/plain (optional)
##### Body: (optional)
    
### 2. IFTTT send a Webhook request (server) to Pythonanywhere.com to auto run the "hot_spell_expelliarmus.py" (client)
###### Video instruction: https://youtu.be/sewhAOozGO8
   - copy and paste the "hot_spell_expelliarmus.py" to (pythonanywhere.com > home > username > yourDirectory)
   - rememebr to "save" and "run" the program
   - Go to Dashboard > Web Apps (Open Web tab) > click "Reload yourAccountName.pythonanywhere.com"
   
### 3a. Grabbing weather data (run "hot_spell_expelliarmus.py" on pythonanywhere.com)
   - Make API call from https://openweathermap.org/api/one-call-api, to get current and forecast weather data.
   - API format - https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={APIKEY}
   - Open an account from OpenWeather.com to gain your unique API key

### 3b. Processing data

Using Python to parse the acquired data. If temperature in the next 2 hours is over 30 degree Celsius. Trigger an alert message to your email.

### 3c. Trigger output:

Send alert to your mailbox with the following messages.
"Subject: HOT SPELL ALERT! Body: Temperature in 2 hours will be {this_temp} degree Celsius. Stay cool and drink more water!"

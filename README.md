Hot Spell Expelliarmus - Personal Heatwave Alert

Now that lockdown is continuing to ease, we're excited about the prospect of enjoying, safely, more of the great outdoors this summer. That also means a return to the very British hobby of getting sun tanning in the parks!

However, even if you can enjoy the weather and manage social distancing, you could be vulnerable to heat exhaustion. Particularly the elderly, people with conditions such as diabetes, young children and people working or exercising outdoors. Heat-stroke may set in which requires urgent medical help.

What if ... you can receive a hot spell warning once you step into your favourite local parks?

The project can be broken down into three main sections:

1. Trigger an IFTTT command once you step into the park
   IF THIS -   "Location: widget
                Select "You enter an area", this triggers everytime you enter an area you specify. In my case, I have chosen the Roundwood Park.
   THEN THAT - "Webhooks" widget
                URL field, fill in "https://yourAccountName.pythonanywhere.com/ifttt
                Method: POST (optional)
                Content Type: text/plain (optional)
                Body: (optional)
    
               
   

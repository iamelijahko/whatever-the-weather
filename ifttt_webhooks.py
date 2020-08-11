import requests

headers = {
    'Content-type': 'application/json',
}

# data = '{"value1": "33"}'
humidity = 67.3
data = '{' + '"value1' + '": "' + str(humidity) + '"' + '}'

print("ALERT! From PyCharm! Humidity is above threshold")

response = requests.post('https://maker.ifttt.com/trigger/get_ahead_of_migraines/with/key/_mvhfa4lZebHXb7kWT1ZR', headers=headers, data=data)

print("COMPLETED! Sending Webhook to IFTTT.")
print(data)
import requests
import twilio
from twilio.rest import Client
from uagents import Agent, Context



uagents = Agent(
    name="Rohit",
    port=8000,
    seed="uagents secret phrase",
    endpoint=["http://127.0.0.1:8080/submit"],
)


api_key = '30d4741c779ba94c470ca1f63045390a'   #api_key is from openweathermap

city = input("Enter city: ")       

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

params = {
        "units": "metric",  # Use Celsius for temperature
    }


if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    
    Temp = round(weather_data.json()['main']['temp']) 

    celsius = (Temp - 32) * 5 / 9
    


# Taking the minimum and maximum Temperature from the user
min_temp = int(input('Enter the Minimum Temperature in Celsius: '))
max_temp = int(input('Enter the Maximum Temperature in Celsius: '))

print(f"The weather in {city} is: {weather}")         #Current Weather Of City
print(f"The temperature in {city} is:{celsius}ºC")       #Current Temperature Of City



def check_Temperature():                                                                              
    if Temp < min_temp:
        return (f"Temperature in {city} is above ({min_temp}°C) \n Current Temperature is ({celsius}) \n Current Weather is {weather}.")
    elif Temp > max_temp:
        return (f"Temperature in {city} is below ({max_temp}°C) \n Current Temperature is ({celsius}) \n Current Weather is {weather}.")
    else:
        return (f"Temperature in {city} is within ({min_temp}-{max_temp}°C).")
    
    
   
TWILIO_ACCOUNT_SID = "AC6dfae05b9d4fb289fcfe04ec4460e84c"
TWILIO_AUTH_TOKEN = "ba4281e198693b68f6f1cad33e17e937"
TWILIO_PHONE_NUMBER = "+13852824782"
TO_PHONE_NUMBER = "+919130079926"  # Replace with the Your phone number



def alert_message(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        to=TO_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
        body=message
    )
        

@uagents.on_interval(period=900.0) #checking every 15 minutes
async def Temperature_alert(ctx:Context):
    temperature = check_Temperature()
    ctx.logger.info(temperature)
    if "below" in temperature or "above" in temperature :
        await new_func(temperature)

async def new_func(temperature):
    await alert_message(temperature)

if __name__ == "__main__":
    uagents.run()


    


        


    

    
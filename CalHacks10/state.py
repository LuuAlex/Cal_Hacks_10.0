import reflex as rx
import datetime
import python_weather
import datetime
import asyncio
import os
import together

class State(rx.State):
    time_period1 = ""
    time_period2 = ""
    location = ""
    clothes_preference = ""
    activity = ""

    output = ""

    def answer(self):
        current = datetime.datetime.now()
        start = datetime.datetime(current.year, current.month, current.day, int(self.time_period1[0:2]), int(self.time_period2[3:5]))
        end = datetime.datetime(current.year, current.month, current.day, int(self.time_period1[0:2]), int(self.time_period2[3:5]))
        self.input = [start, end, self.location, self.clothes_preference, self.activity]
        
        
async def getweather(city, start_hr, end_hr):
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # fetch a weather forecast from a city
    weather = await client.get(city)    
    # get the weather forecast for a few days
    forecast = next(weather.forecasts)
    
    # hourly forecasts
    elapsed = {}
    for hourly in forecast.hourly:
        if hourly.time >= start_hr and hourly.time <= end_hr:
            elapsed[str(hourly.time)] = ("Temperature:", hourly.temperature, "Weather description:", hourly.description, str(hourly.kind))
    
    return elapsed

f = open("CalHacks10/api_key.txt", "r")
together.api_key = f.read()

def to_prompt(weather_dict, location, activity_description, clothes, start_hr, end_hr):
    return f'''You will be giving a detailed suggestion of clothes. These are the inputs that I put:
                Location: {location}
                Time period spent outside: {str(start_hr)} to  {str(end_hr)}
                The weather at each hour is this: {weather_dict}
                I plan to do this: {activity_description}
                And may wear these clothes: {clothes}
                Now, give a detailed suggestion of clothes (including color combinations) that fit the weather.
                Format your answer as a couple of sentences. DO NOT ONLY USE THE CLOTHES GIVEN.
                '''

def llm_text(wd, location, start_hr, end_hr, activity_description, clothes):
    p = to_prompt(wd, location, activity_description, clothes, start_hr, end_hr)
    output = together.Complete.create(
      prompt = p, 
      model = "lmsys/vicuna-7b-v1.5", 
      max_tokens = 512,
      temperature = 0.3,
      top_k = 60,
      top_p = 0.6,
      repetition_penalty = 1.1,
      stop = ['<human>', '\n\n']
    )
    return output['output']['choices'][0]['text']

import base64
import requests                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                         
url = "https://api.together.xyz/inference"                                                                                                                                                                                                           
model = "stabilityai/stable-diffusion-xl-base-1.0"
f = open("CalHacks10/api_key.txt", "r")
together.api_key = f.read()

location = "New York"
start_hr = datetime.time(12, 0)
end_hr = datetime.time(6, 0)
activity_description = "hike, study"
clothes = "shorts, hoodie, tshirt"
start_hr = datetime.time(0, 0)
end_hr = datetime.time(12, 0)
wd = asyncio.run(getweather(location, start_hr, end_hr))
prompt = llm_text(wd, location, start_hr, end_hr, activity_description, clothes)

                                                                                                                                                                                                                                                     
print(f"Model: {model}")                                                                                                                                                                                                                             
print(f"Prompt: {repr(prompt)}")                                                                                                                                                                                                                     
print()
                                                                                                                                                                                                                                                     
payload = {                                                                                                                                                                                                                                          
    "model": model,                                                                                                                                                                                                                                  
    "prompt": prompt,                                                                                                                                                                                                                                
    "results": 2,                                                                                                                                                                                                                               
    "width": 1024,
    "height": 1024,
    "steps": 20,
    "seed": 42,
    #"negative_prompt": negative_prompt,
}                                                                                                                                                                                                                                                    
headers = {                                                                                                                                                                                                                                          
    "accept": "application/json",                                                                                                                                                                                                                    
    "content-type": "application/json",                                                                                                                                                                                                              
    "Authorization": f"Bearer 4faf98f505175c9ac8bd6e6c5f895f8a6e335f511bf4aff88409d81916c2a3c9"                                                                                                                                                                                     
}                                                                                                                                                                                                                                    
response = requests.post(url, json=payload, headers=headers, stream=True)                                                                                                                                                                            
response.raise_for_status()

response_json = response.json()
                                                                                                                                                                                                                                                     
# save the first image
image = response_json["output"]["choices"][0]
with open("tokyocrossing.png", "wb") as f:
    f.write(base64.b64decode(image["image_base64"]))
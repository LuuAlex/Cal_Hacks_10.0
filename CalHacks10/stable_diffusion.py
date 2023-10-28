import base64
import os
import requests                                                                                                                                                                                                                                      
import together
import datetime
import asyncio
from weather import getweather
from llm import llm_text
                                                                                                                                                                                                                                         
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

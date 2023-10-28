import together
from weather import getweather
import datetime
import asyncio
import os

together.api_key = "4faf98f505175c9ac8bd6e6c5f895f8a6e335f511bf4aff88409d81916c2a3c9"

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
location = "Parsippany, NJ"
start_hr = datetime.time(12, 0)
end_hr = datetime.time(6, 0)
activity_description = "birthday party"
clothes = "princess costume, hoodie, overalls"

if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

start_hr = datetime.time(0, 0)
end_hr = datetime.time(12, 0)
wd = asyncio.run(getweather(location, start_hr, end_hr))

p = to_prompt(wd, location, activity_description, clothes, start_hr, end_hr)
print(p)

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

# print generated text
print(output['output']['choices'][0]['text'])
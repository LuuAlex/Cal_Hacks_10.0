import together
from weather import getweather
import datetime
import asyncio
import os

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

if __name__ == '__main__':
    location = "Parsippany, NJ"
    start_hr = datetime.time(12, 0)
    end_hr = datetime.time(6, 0)
    activity_description = "hike, study"
    clothes = "shorts, hoodie, tshirt"
    start_hr = datetime.time(0, 0)
    end_hr = datetime.time(12, 0)
    wd = asyncio.run(getweather(location, start_hr, end_hr))
    result = llm_text(wd, location, start_hr, end_hr, activity_description, clothes)
    print(result)
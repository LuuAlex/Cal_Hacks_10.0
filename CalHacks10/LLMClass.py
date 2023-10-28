import python_weather
import together
import base64
import requests
import io
from PIL import Image                                                                                                                                                                                                                                      


class LLM():
    f = open("CalHacks10/api_key.txt", "r").read()
    together.api_key = f     

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
        p = LLM.to_prompt(wd, location, activity_description, clothes, start_hr, end_hr)
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

    async def run_entire_llm(location, start_hr, end_hr, activity_description, clothes):
        url = "https://api.together.xyz/inference"                                                                                                                                                                                                           
        model = "stabilityai/stable-diffusion-xl-base-1.0"
        wd = await LLM.getweather(location, start_hr, end_hr)
        prompt = LLM.llm_text(wd, location, start_hr, end_hr, activity_description, clothes)
                                                                                                                                                                                                                                                            
        payload = {                                                                                                                                                                                                                                          
            "model": model,                                                                                                                                                                                                                                  
             "prompt": prompt,                                                                                                                                                                                                                                
             "results": 2,                                                                                                                                                                                                                               
             "width": 1024,
             "height": 1024,
             "steps": 20,
             "seed": 42,
         }                                                                                                                                                                                                                                                    
        headers = {                                                                                                                                                                                                                                          
             "accept": "application/json",                                                                                                                                                                                                                    
             "content-type": "application/json",                                                                                                                                                                                                              
             "Authorization": f"Bearer {LLM.f}"                                                                                                                                                                                     
        }                                                                                                                                                                                                                                    
        response = requests.post(url, json=payload, headers=headers, stream=True)                                                                                                                                                                            
        response.raise_for_status()

        response_json = response.json()
                                                                                                                                                                                                                                                            
        # save the first image
        image = response_json["output"]["choices"][0]
        image = base64.b64decode(image["image_base64"])
        decoded_string = io.BytesIO(image)
        img = Image.open(decoded_string)
        return prompt, img #decoded_string #img.show()
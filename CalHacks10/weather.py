# import the module
import python_weather
import datetime
import asyncio
import os

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

if __name__ == '__main__':
  # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  city = "Dublin, CA"
  start_hr = datetime.time(0, 0)
  end_hr = datetime.time(12, 0)
  asyncio.run(getweather(city, start_hr, end_hr))
import reflex as rx
import datetime
import asyncio

from .LLMClass import LLM

class State(rx.State):
    time_period1 = ""
    time_period2 = ""
    location = ""
    clothes_preference = ""
    activity = ""

    output = ""
    image = ""
    weather: list[tuple[str, tuple]] = []
    new_weather: list[tuple] = []
    loading_screen = True

    async def answer(self):
        self.output = ""
        self.image = ""
        self.weather = []
        self.new_weather = []
        self.loading_screen = True

        start = datetime.time(int(self.time_period1[0:2]), int(self.time_period1[3:5]))
        end = datetime.time(int(self.time_period2[0:2]), int(self.time_period2[3:5]))
        self.weather, self.output, self.image = await LLM.run_entire_llm(self.location, start, end, self.activity, self.clothes_preference)
        self.weatherDisplayCreateRows()
        self.loading_screen = False
        
    def weatherDisplayCreateRows(self):
      rv = []
      data = self.weather
      for item in data:
          temp = []
          temp.append(item[0])
          temp.append(item[1][1])
          temp.append(item[1][3])
          rv.append(tuple(temp))
      self.new_weather = rv
    def load(self):
        self.output = ""
        self.image = ""
        self.weather = []
        self.new_weather = []
        self.loading_screen = True

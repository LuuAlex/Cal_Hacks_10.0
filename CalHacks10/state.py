import reflex as rx
import datetime

from .LLMClass import LLM

class State(rx.State):
    time_period1_hours = ""
    time_period1_mins = ""
    time_period1_ampm = ""

    time_period2_hours = ""
    time_period2_mins = ""
    time_period2_ampm = ""

    location = ""
    clothes_preference = ""
    activity = ""

    output = ""
    image = ""
    weather: list[tuple[str, tuple]] = []
    new_weather: list[tuple] = []
    loading_screen = True

    def create_time(self, hours, mins, ampm):
        hours = int(hours)
        mins = int(mins)

        if ampm == "AM" and hours == 12:
            hours = 0
        
        elif ampm == "PM" and hours < 12:
            hours += 12
        
        # Create a new datetime object with the time in 24-hour format
        time_24_hour = datetime.time(hours, mins)
        return time_24_hour

    def create_time(self, hours, mins, ampm):
        hours = int(hours)
        mins = int(mins)

        if ampm == "AM" and hours == 12:
            hours = 0
        
        elif ampm == "PM" and hours < 12:
            hours += 12
        
        # Create a new datetime object with the time in 24-hour format
        time_24_hour = datetime.time(hours, mins)
        return time_24_hour

    async def answer(self):
        self.output = ""
        self.image = ""
        self.weather = []
        self.new_weather = []
        self.loading_screen = True

        
        start = self.create_time(self.time_period1_hours, self.time_period1_mins, self.time_period1_ampm)
        end = self.create_time(self.time_period2_hours, self.time_period2_mins, self.time_period2_ampm)
        self.weather, self.output, self.image = await LLM.run_entire_llm(self.location, start, end, self.activity, self.clothes_preference)
        self.weatherDisplayCreateRows()
        self.loading_screen = False
        
    def weatherDisplayCreateRows(self):
      rv = []
      data = self.weather
      for item in data:
          temp = []
          AMPM = "AM"
          hour = int(item[0][0:2])
          min = item[0][3:5]
          if hour > 12:
              AMPM = "PM"
              hour -= 12
          if hour == 12:
              AMPM = "PM"
          if hour == 0:
              hour = 12
          new_time = f"{hour}:{min} {AMPM}"
          temp.append(new_time)
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

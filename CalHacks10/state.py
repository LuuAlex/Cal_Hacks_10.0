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

    def create_time(hours, mins, ampm):
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
        start = self.create_time(self.time_period1_hours, self.time_period1_mins, self.time_period1_ampm)
        end = self.create_time(self.time_period2_hours, self.time_period2_mins, self.time_period2_ampm)
        self.weather, self.output, self.image = await LLM.run_entire_llm(self.location, start, end, self.activity, self.clothes_preference)
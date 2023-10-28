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
    update_image = False

    async def answer(self):
        start = datetime.time(int(self.time_period1[0:2]), int(self.time_period2[3:5]))
        end = datetime.time(int(self.time_period1[0:2]), int(self.time_period2[3:5]))
        self.output, self.image = await LLM.run_entire_llm(self.location, start, end, self.activity, self.clothes_preference)
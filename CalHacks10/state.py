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

    async def answer(self):
        print("RUNNING ANSWER")
        current = datetime.datetime.now()
        start = datetime.datetime(current.year, current.month, current.day, int(self.time_period1[0:2]), int(self.time_period2[3:5]))
        end = datetime.datetime(current.year, current.month, current.day, int(self.time_period1[0:2]), int(self.time_period2[3:5]))
        self.output =  await LLM.run_entire_llm(self.location, start, end, self.activity, self.clothes_preference)
    
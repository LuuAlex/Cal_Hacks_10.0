import reflex as rx
import datetime

class State(rx.State):
    time_period1 = ""
    time_period2 = ""
    location = ""
    clothes_preference = ""
    activity = ""

    input = []
    output = "hi"

    def merge(self):
        current = datetime.datetime.now()
        start = datetime.datetime(current.year, current.month, current.day, int(self.time_period1[0:2]), int(self.time_period2[3:5]))
        end = datetime.datetime(current.year, current.month, current.day, int(self.time_period1[0:2]), int(self.time_period2[3:5]))
        self.input = [start, end, self.location, self.clothes_preference, self.activity]
    
    def answer(self):
        # plug in backend chatbot
        self.output = str(self.input)
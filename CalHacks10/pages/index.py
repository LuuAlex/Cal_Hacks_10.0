from CalHacks10 import styles
from CalHacks10.state import State

import reflex as rx


@rx.page(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    return rx.container(
        chat(),
        input_bar("Enter location in city, state format", State.location, State.set_location),
        input_bar("Enter first time in terms of a 24 hour clock", State.time_period1, State.set_time_period1),
        input_bar("Enter second time in terms of a 24 hour clock", State.time_period2, State.set_time_period2),
        input_bar("Enter activities, separated by commas", State.activity, State.set_activity),
        input_bar("Enter clothes you have, separated by commas", State.clothes_preference, State.set_clothes_preference),
        submit()
    )

def chat() -> rx.Component:
    questions = [
        (
            "I can help you figure out what clothes you should wear, but I need some information." + 
            "Can you give the location you are in?"
        ),
        (
           "What is the time period you plan to spend outside? Please put the first time."
        ),
        (
           "Please put in the second time."
        ),
        (
           "What are the activities you plan to do?"
        ),
        (
           "What are the clothes you currently have in your wardrobe?"
        ),
    ]
    return rx.box(
        *[question for question in questions]
    )


def input_bar(placeholder, stateVar, changeVar) -> rx.Component:
    return rx.hstack(
        rx.input(
            value=stateVar,
            placeholder=placeholder,
            on_change=changeVar
        )
    )

def submit() -> rx.Component:
    return rx.box(
        rx.button(
            "Submit",
            on_click=rx.redirect("/suggestion")
        )
    )
    

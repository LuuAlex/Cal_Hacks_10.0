from CalHacks10 import styles
from CalHacks10.state import State
from typing import List

import reflex as rx

#class SelectState(rx.State):
#    option: str = "No selection yet."

hour_options: List[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
minute_options: List[str] = []
for i in range(0,59):
    minute_options.append(f"{i}")

@rx.page(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    questions = [
        (
            "What city and state you are in?"
        ),
        (
           "When do you plan to go outside?"
        ),
        (
           "When do you plan to come back?"
        ),
        (
           "What are the activities you plan to do during this time?"
        ),
        (
           "What are the clothes you currently have in your wardrobe?"
        ),
    ]

    return rx.container(
        title(),
        dark_mode(),
        instruction(),
        input_bar("Enter your location in city, state format (ex: Berkeley, CA.", State.location, State.set_location, questions[0]),
        input_bar("Enter the time you plan to go outside (ex: 12:00).", State.time_period1, State.set_time_period1, questions[1]),
        #dropdown(hour_options),
        #dropdown(minute_options)
        input_bar("Enter the time you plan to be back home.", State.time_period2, State.set_time_period2, questions[2]),
        input_bar("\nEnter the activities you are planning for the day as a list.\n", State.activity, State.set_activity, questions[3]),
        input_bar("\nEnter the clothes you currently own.\n", State.clothes_preference, State.set_clothes_preference, questions[4]),
        submit()
    )

def title() -> rx.Component:
    return rx.text(
        "Fit Creator",
        background_image="linear-gradient(271.68deg, #EE756A 10.75%, #756AEE 88.52%)",
        background_clip="text",
        font_weight="bold",
        font_size="4em",
        text_align="center"
    )

def instruction() -> rx.Component:
    return rx.box(
        "Having trouble deciding what to wear today? Don't want to check the weather app? Fill out these questions to get a personalized fit!"
    )

def input_bar(placeholder, stateVar, changeVar, question) -> rx.Component:
    return rx.vstack(
        rx.box(
            question,
            margin_y="1em"
        ),
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
            on_click=rx.redirect("/suggestion"), 
            color = 'green',
            margin_y="1em"
        )
    )
def dark_mode() -> rx.Component:
    return rx.box(
        rx.button(rx.icon(tag="moon"), on_click=rx.toggle_color_mode,)
    )

def dropdown(type):
    return rx.vstack(
        rx.select(
            type,
            on_change=State.set_option,
            color_schemes="twitter",
        ),
    )

from CalHacks10 import styles
from CalHacks10.state import State
from typing import List

import reflex as rx

hour_options: List[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
minute_options: List[str] = []
for i in range(0,59):
    minute_options.append(f"{i}")

@rx.page(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    questions = [
        (
            "Please input the city and state you are in."
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

    return rx.container(
        title(),
        dark_mode(),
        instruction(),
        input_bar("\nEnter location in city, state format\n", State.location, State.set_location, questions[0]),
        input_bar("\nEnter first time in terms of a 24 hour clock\n", State.time_period1, State.set_time_period1, questions[1]),
        input_bar("\nEnter second time in terms of a 24 hour clock\n", State.time_period2, State.set_time_period2, questions[2]),
        input_bar("\nEnter activities, separated by commas\n", State.activity, State.set_activity, questions[3]),
        input_bar("\nEnter clothes you have, separated by commas\n", State.clothes_preference, State.set_clothes_preference, questions[4]),
        submit()
    )

def title() -> rx.Component:
    return rx.text(
        "Clothes Generator",
        background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
        background_clip="text",
        font_weight="bold",
        font_size="4em",
        text_align="center"
    )

def instruction() -> rx.Component:
    return rx.box(
        "I can help you figure out what clothes you should wear, but I need some information."
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
            on_click=rx.redirect("/suggestion"), color = 'green'
        )
    )
def dark_mode() -> rx.Component:
    return rx.box(
        rx.button(rx.icon(tag="moon"), on_click=rx.toggle_color_mode,)
    )

    

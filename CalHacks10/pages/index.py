from CalHacks10 import styles
from CalHacks10.state import State
from typing import List

import reflex as rx

hour_options = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
minute_options = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
for i in range(10,60):
    minute_options.append(f"{i}")
am_pm_options = ["AM", "PM"]

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
        rx.card(
            rx.box(
                rx.hstack(
                    title(),
                    rx.spacer(),
                    dark_mode(),
                    width="100%",
                    align="right",
                ),
                rx.box(margin_y="1em"),
                instruction(),
            ),
            margin="8px"
        ),
        rx.box(margin_y="1em"),
        rx.card(
            rx.box(
                input_bar("Enter your location in city, state format (ex: Berkeley, CA).", State.location, State.set_location, questions[0]),
                rx.box(margin_y="2em"),
                time_input_bar([State.time_period1_hours, State.time_period1_mins, State.time_period1_ampm], [State.set_time_period1_hours, State.set_time_period1_mins, State.set_time_period1_ampm], questions[1]),
                rx.box(margin_y="2em"),
                time_input_bar([State.time_period2_hours, State.time_period2_mins, State.time_period2_ampm], [State.set_time_period2_hours, State.set_time_period2_mins, State.set_time_period2_ampm], questions[2]),
                rx.box(margin_y="2em"),
                input_bar("Enter the activities you are planning for the day as a list.", State.activity, State.set_activity, questions[3]),
                rx.box(margin_y="2em"),
                input_bar("Enter the clothes you currently own.", State.clothes_preference, State.set_clothes_preference, questions[4]),
            ),
            margin="8px"
        ),
        rx.box(margin_y="1em"),
        rx.card(
            submit(),
            margin="8px"
        ),
        max_width="70em"
    )

def title() -> rx.Component:
    return rx.text(
        "Fit Creator",
        background_image="linear-gradient(271.68deg, #EE756A 10.75%, #756AEE 88.52%)",
        background_clip="text",
        font_weight="bold",
        font_size="4em",
        text_align="center",
    )

def instruction() -> rx.Component:
    return rx.box(
        rx.text(
            "Having trouble deciding what to wear today? Don't want to check the weather app? Fill out these questions to get a personalized fit!",
            font_size="20px"
        ),
    )

def input_bar(placeholder, stateVar, changeVar, question) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                question,
                font_size="18px"
            ),
            text_align="left",
            
        ),
        rx.box(margin_y="1em"),
        rx.input(
            value=stateVar,
            placeholder=placeholder,
            on_change=changeVar
        )
    )

def time_input_bar(stateVar, changeVar, question) -> rx.Component:
    return rx.box(
        rx.text(
            question,
            font_size="18px"
        ),
        rx.box(margin_y="1em"),
        rx.hstack(
            rx.select(hour_options, on_change=changeVar[0], value=stateVar[0], placeholder="Hours"),
            rx.box(":", margin_y="1em"),
            rx.select(minute_options, on_change=changeVar[1], value=stateVar[1], placeholder="Minutes"),
            rx.select(am_pm_options, on_change=changeVar[2], value=stateVar[2], placeholder="AM/PM")
        )
    )

def submit() -> rx.Component:
    return rx.box(
        rx.button(
            "Submit",
            on_click=rx.redirect("/suggestion"), 
            color='light green',
        )
    )
def dark_mode() -> rx.Component:
    return rx.box(
        rx.button(rx.icon(tag="moon"), on_click=rx.toggle_color_mode,)
    )

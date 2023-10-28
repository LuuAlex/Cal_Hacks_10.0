from CalHacks10.state import State
import reflex as rx
import asyncio

@rx.page(route="/suggestion", title="Suggestion")
def dashboard() -> rx.Component:

    return rx.container(
        rx.button(
            on_click=State.answer
        ),
        rx.image(
            src=State.image
        ),
        rx.box(
            State.output
        ),
        rx.box(
            
            State.weather
        )
    )

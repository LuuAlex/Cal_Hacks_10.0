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
            rx.cond(
                weatherShow(State.weather),
                rx.grid(
                  rx.foreach(
                    State.weather,
                    weatherDisplay
                  )
                )
                
            )
            
        )
    )

def weatherShow(value):
    return value != []

def weatherDisplay(data):
    return rx.grid_item(
        f'Time: {data[0]} ',
        f'{data[1][0]} {data[1][1]} ',
        f'{data[1][2]} {data[1][3]} ',
    )


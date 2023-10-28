from CalHacks10.state import State
import reflex as rx
import asyncio

@rx.page(route="/suggestion", title="Suggestion")
def dashboard() -> rx.Component:

    return rx.container(
        rx.card(
            rx.image(
                src=State.image,
                width='370px',
                height='370px',
                marginLeft='auto',
                marginRight='auto'
            ),
            margin='8px',
        ),
        rx.card(
            rx.box(
                State.output
            ),
            margin='8px',
        ),
        rx.card(
            rx.cond(
                weatherShow(State.weather),
                rx.grid(
                  rx.foreach(
                    State.weather,
                    weatherDisplay
                  )
                )
            ),
            margin='8px',
        )
    )

def weatherShow(value):
    return value != []

def weatherDisplay(data):
    return rx.table_container(
        rx.table(
            headers=["Name", "Age", "Location"],
            rows=[
                ("John", 30, "New York"),
                ("Jane", 31, "San Francisco"),
                ("Joe", 32, "Los Angeles"),
            ],
            footers=["Footer 1", "Footer 2", "Footer 3"],
            variant="striped",
        )
    )
    #return rx.grid_item(
    #    f'Time: {data[0]} ',
    #    f'{data[1][0]} {data[1][1]} ',
    #    f'{data[1][2]} {data[1][3]} ',)
    


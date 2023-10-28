from CalHacks10.state import State

import reflex as rx


@rx.page(route="/suggestion", title="Suggestion")
def dashboard() -> rx.Component:
    
    State.merge
    State.answer

    return rx.container(
        rx.box(
            State.output
        )
    )

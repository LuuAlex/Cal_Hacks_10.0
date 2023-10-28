from CalHacks10.state import State
import reflex as rx
import asyncio

@rx.page(route="/suggestion", title="Suggestion")
def dashboard() -> rx.Component:
    return rx.container(
        rx.card(
            rx.hstack(
              back(),
              rx.spacer(),
              dark_mode(),  
            ),
            margin = "8px"
        ),
        rx.card(
            rx.hstack(
                rx.cond(
                  ~State.loading_screen,
                  rx.image(
                          src=State.image,
                          width='370px',
                          height='370px',
                          marginLeft='auto',
                          marginRight='auto'
                      ),
                ),
                rx.cond(
                  State.loading_screen,
                  rx.circular_progress(
                      rx.circular_progress_label(
                          "Loading", color="rgb(107,99,246)",
                          font_size="30px"
                      ),
                      size="370px",
                      thickness="5px",
                      is_indeterminate=True,
                      marginLeft='auto',
                      marginRight='auto',
                  ),
                ),
            margin='8px',
            )
        ),
        rx.cond(
          ~State.loading_screen,
          rx.container(
            rx.card(
                rx.box(
                    State.output
                ),
                margin='8px',
                maxWidth="70em",
            ),
            rx.card(
                rx.cond(
                  weatherShow(State.weather),
                    rx.table_container(
                        rx.table(
                            headers=["Time", "Temperature (F)", "Description"],
                            rows = State.new_weather,
                            variant="striped"
                        )
                    )
                )
            ),
            margin='8px',
            maxWidth="70em",
          ),
        ),
        maxWidth="70em",
    )
def weatherShow(value):
    return value != []

def back() -> rx.Component:
    return rx.box(
        rx.button(
            "← Try a new input",
            on_mouse_up=State.load,
            on_click=rx.redirect("/"), 
            color = 'green',
            align="left",
            width = '100%',
        )
    )
def dark_mode() -> rx.Component:
    return rx.box(
        rx.button(rx.icon(tag="moon"), on_click=rx.toggle_color_mode,)
    )
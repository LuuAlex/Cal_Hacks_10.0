"""Welcome to Reflex!."""

from CalHacks10 import styles

# Import all the pages.
from CalHacks10.pages import *

import reflex as rx

# Create the app and compile it.

# Fonts to include.
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&family=IBM+Plex+Mono:ital,wght@0,500;0,600;1,600&display=swap",
]

style = {
    "font_family": "Instrument Sans",
    "font_size": "16px",
}


app = rx.App(
    style=style,
    stylesheets=STYLESHEETS,
)
app.compile()
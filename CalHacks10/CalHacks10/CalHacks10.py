"""Welcome to Reflex!."""

from CalHacks10 import styles

# Import all the pages.
from CalHacks10.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()

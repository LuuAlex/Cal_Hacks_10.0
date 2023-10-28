"""Welcome to Reflex!."""

from Cal_Hacks_10.0 import styles

# Import all the pages.
from Cal_Hacks_10.0.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()

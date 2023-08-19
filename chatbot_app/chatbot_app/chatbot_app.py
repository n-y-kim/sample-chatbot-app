"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
import random

from chatbot_app import style
from chatbot_app.state import State

#Create random 6 digit number
def random_number():
    return random.randint(100000, 999999)

def greeting_message(answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                answer, 
                style=style.answer_style,
            ),
            text_align="left",
        ),
        margin_y="1em",
    )

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right"
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left"
        ),
        margin_y="1em",
    )

def first_message() -> rx.Component:
    return rx.box(
        greeting_message("Hello, I'm chatbot app to help you with your questions about Azure."),
    )
    
def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )
    
def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Type your message here...",
            on_blur=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Send", 
            on_click=State.answer,
            style=style.button_style
        ),
    )

def index() -> rx.Component:
    return rx.container(
        first_message(),
        chat(),
        action_bar(),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()

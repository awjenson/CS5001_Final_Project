"""
Chat Bot: "Model" File for the Application
===========================
Course:   CS 5001
Student:  Andrew Jenson
Semester: Fall 2023
Assignment: Final Project

This file contains the constants used in the program.
"""

MODEL_QUIZZES = "model_quizzes.json"
MODEL_TIPS = "model_tips.json"
MODEL_USER = "model_user.json"

BOT_ICON = "🤖"
NORTHEASTERN_CS_5002 = "CS5002"

PROMPT_GET_NUMBER = f"{BOT_ICON} Enter a number:\n"
PROMPT_GET_NUMBER_ERROR = f"{BOT_ICON} ERROR. 🚫 Enter a valid number:"
PROMPT_STATEMENT = "Enter a number from the option(s) below:"

COMMAND_TXT_MENU = "Menu"
COMMAND_TXT_HELP = "Help"
COMMAND_TXT_QUIT = "Quit"
COMMAND_TXT_QUIZ = "Quiz"
COMMAND_TXT_TIPS = "Tips"

CONTENT_TYPE_TIP = "tip"
CONTENT_TYPE_QUIZ_QUESTION = "question"

UNEXPECTED_ERROR = f"{BOT_ICON} SORRY. ⛔️ Unexpected error. Try again."

FEEDBACK_TRANSITION = f"{BOT_ICON} OK. 👍 Here you go..."
FEEDBACK_CORRECT = f"{BOT_ICON} CORRECT! ✅"
FEEDBACK_WRONG = f"{BOT_ICON} WRONG. ❌"

HELP_STATEMENT = (
    f"This program is the {NORTHEASTERN_CS_5002} Chat Bot. "
    "It was created by Andrew Jenson for the Final Project of CS5001 in Fall 2023. "
    f"The goal is to help Northeastern University students succeed in {NORTHEASTERN_CS_5002}. "
    "It features quizzes and tips. "
    "You can interact with the chat bot by entering the numbered options displayed "
    "in between brackets (e.g [0]). "
    f"{PROMPT_STATEMENT}")

"""
Chat Bot: Menu "Controller" File for the Application
===========================
Course:   CS 5001
Student:  Andrew Jenson
Semester: Fall 2023
Assignment: Final Project

This "Controller" file runs the main program and contains the menu-related functions
of the chat bot.
"""

import controller_json # Communicate with this "Controller" file
import controller_helper # Contains helper functions for program's features
import model_constants # Contains the constants used in the program
import view_terminal # Communicate with this "View" file


def run_chat_bot(selected_bot: str):
    """
    Runs the chat bot program, which manages all of the available options for the user.

    Args:
        selected_bot (str): The name of the chat bot to run.

    Returns:
        None
    """

    first_message = f"{model_constants.BOT_ICON} Greetings, human..."
    view_terminal.print_with_line_breaks(first_message)

    intro_message = (f"{model_constants.BOT_ICON} Welcome to the {selected_bot} "
                    "Chat Bot! 👋")
    view_terminal.print_with_line_breaks(intro_message)

    run_menu()

    outro_message = f"{model_constants.BOT_ICON} Nice chatting with you..."
    view_terminal.print_with_line_breaks(outro_message)

    last_message = (f"{model_constants.BOT_ICON} Goodbye from the {selected_bot} "
                   "Chat Bot! 👋")
    view_terminal.print_with_line_breaks(last_message)


def run_menu():
    """
    Runs the main menu of the program.

    This function displays a list of available commands and prompts the user
    for their selection. Based on the user's input, it calls the appropriate
    function to handle the selected option (e.g. help, quiz, tips, or quit).

    Args:
        None

    Returns:
        None
    """

    menu_options = [model_constants.COMMAND_TXT_HELP,
                model_constants.COMMAND_TXT_QUIZ,
                model_constants.COMMAND_TXT_TIPS,
                model_constants.COMMAND_TXT_QUIT]

    while True:

        view_terminal.print_header_statement_and_options(
                        model_constants.COMMAND_TXT_MENU,
                        model_constants.PROMPT_STATEMENT,
                        menu_options)

        # Get user input
        user_input = view_terminal.get_valid_input_integer(
                                    model_constants.PROMPT_GET_NUMBER,
                                    model_constants.PROMPT_GET_NUMBER_ERROR,
                                    menu_options)

        # Check user input and run selected option
        # HELP
        if user_input == controller_helper.get_index_in_list(
                                            model_constants.COMMAND_TXT_HELP,
                                            menu_options):
            run_help()

        # QUIZ
        elif user_input == controller_helper.get_index_in_list(
                                                model_constants.COMMAND_TXT_QUIZ,
                                                menu_options):
            # Get quiz data
            all_quizzes_dict = controller_json.read_from_json_file(
                                                model_constants.MODEL_QUIZZES)
            run_quiz(all_quizzes_dict)

        # TIPS
        elif user_input == controller_helper.get_index_in_list(
                                                model_constants.COMMAND_TXT_TIPS,
                                                menu_options):
            # Get tips data
            all_tips_dict = controller_json.read_from_json_file(
                                                model_constants.MODEL_TIPS)
            run_tips(all_tips_dict)

        # QUIT
        elif user_input == controller_helper.get_index_in_list(
                                                model_constants.COMMAND_TXT_QUIT,
                                                menu_options):
            break

        # UNEXPECTED ERROR HANDLE
        else:
            view_terminal.print_with_line_breaks(model_constants.UNEXPECTED_ERROR)
            continue


def run_help():
    """
    Runs the help option of the program and displays help-related info for the user.

    Args:
        None

    Returns:
        None
    """

    help_list = [model_constants.COMMAND_TXT_MENU,]

    while True:

        view_terminal.print_header_statement_and_options(
                        model_constants.COMMAND_TXT_HELP,
                        model_constants.HELP_STATEMENT,
                        help_list)

        user_input = view_terminal.get_valid_input_integer(
                                        model_constants.PROMPT_GET_NUMBER,
                                        model_constants.PROMPT_GET_NUMBER_ERROR,
                                        help_list)

        if user_input == controller_helper.get_index_in_list(
                                            model_constants.COMMAND_TXT_MENU,
                                            help_list):
            break

        else:
            view_terminal.print_with_line_breaks(model_constants.UNEXPECTED_ERROR)
            continue

    end_message = (f"{model_constants.BOT_ICON} Exiting {model_constants.COMMAND_TXT_HELP}, "
                    f"returning to {model_constants.COMMAND_TXT_MENU}.")

    view_terminal.print_with_line_breaks(end_message)


def run_quiz(all_quizzes_dict: dict):
    """
    Presents a quiz based on the provided dictionary of quizzes.

    Args:
        all_quizzes_dict (dict): A dictionary of dictionaries,
            containing quiz categories as keys and quizzes as the values and then
            each quiz question as keys and options as lists of strings as the values.

    Returns:
        None
    """

    # Helper function returns a tuple of three integers
    get_three_results = controller_helper.common_logic_for_tips_and_quizzes(
                                            model_constants.COMMAND_TXT_QUIZ,
                                            model_constants.CONTENT_TYPE_QUIZ_QUESTION,
                                            all_quizzes_dict)

    (correct_answers, total_statements, percentage_correct) = get_three_results

    end_message = (f"{model_constants.BOT_ICON} DONE. 🏁 "
                    f"You answered {correct_answers} of {total_statements} "
                    f"questions correctly ({percentage_correct}%).")

    view_terminal.print_with_line_breaks(end_message)


def run_tips(all_tips_dict: dict):
    """
    Presents tips based on the provided dictionary of tips.

    Args:
        all_tips_dict (dict): A dictionary of dictionaries,
            containing tip categories as keys and tips as the values and then
            each tip string as keys and options as lists of strings as the values.

    Returns:
        None
    """

    # Helper function returns a tuple of three integers
    get_three_results = controller_helper.common_logic_for_tips_and_quizzes(
                                            model_constants.COMMAND_TXT_TIPS,
                                            model_constants.CONTENT_TYPE_TIP,
                                            all_tips_dict)

    (correct_answers, total_statements, percentage_correct) = get_three_results

    end_message = (f"{model_constants.BOT_ICON} DONE. 🏁 "
                    f"You reviewed {correct_answers} of {total_statements} "
                    f"tips ({percentage_correct}%).")

    view_terminal.print_with_line_breaks(end_message)


def main() -> None:
    """
    Main function for the program.
    """

    run_chat_bot(model_constants.NORTHEASTERN_CS_5002)


if __name__ == "__main__":
    main()

"""
Chat Bot: A "View" File for the Application
===========================
Course:   CS 5001
Student:  Andrew Jenson
Semester: Fall 2023
Assignment: Final Project

This "View" file contains functions that communicate with the program's user.
"""

import textwrap # https://www.w3schools.in/python/examples/text-wrapping-in-python


# Used by controller_json.py
def print_json_error(message: str, file_path: str):
    """
    Prints a user-friendly error message for JSON file access or parsing issues.

    Args:
        message (str): The specific error message to be printed
        file_path (str): The path of the JSON file causing the error

    Returns:
        None
    """

    print(f"{message} {file_path}")


# Used by Controller file(s)
def get_valid_input_integer(prompt: str, error_prompt: str, valid_options: list) -> int:
    """
    Gets a valid integer from the user and returns the integer from the provided valid options.

    Args:
        prompt (str): prompt message for the user
        error_prompt (str): prompt message if user enters an incorrect input
        valid_options (list): Valid integers the user can choose

    Returns:
        int: user input integer

    Raises:
        ValueError: If the user enters a non-integer value
    """

    valid_range_integers = range(len(valid_options))
    valid_range_string = ", ".join(map(str, valid_range_integers))
    error_message = f"{error_prompt} {valid_range_string}"

    while True:
        # adding to string prevents my code from crashing for EOFErrors
        user_input_string = input(f"{prompt}").strip().casefold()

        # Try/except handles if user enters a non-integer value
        try:
            user_input_integer = int(user_input_string)
            if 0 <= user_input_integer < len(valid_options):
                return user_input_integer
            print(error_message)

        except ValueError:
            print(error_message)
            continue


# Used by Controller file(s)
# options: Union Type (https://docs.python.org/3/library/stdtypes.html#types-union)
def print_header_statement_and_options(header: str, statement: str, options: list | dict):
    """
    Prints a header, statement, and list of options.

    Args:
        header (str): Title of the section to be displayed in all caps.
        statement (str): Descriptive message to be displayed below the header.
        options (list | dict): List of options or dictionary of key-value pairs to be displayed.

    Returns:
        None
    """

    capitalized_header(header)
    print_with_line_breaks(statement)
    print_options(options)


# Used by View file(s)
def capitalized_header(option_name: str):
    """
    Prints a header using the provided option name.

    Args:
        option_name (str): The name of the option to be displayed as a header

    Returns:
        None
    """

    print(f"""\n\n{option_name.upper()}:\n\n""")


# Used by Controller file(s)
def print_selected_topic_header(selected_menu_option: str, selected_topic: str):
    """
    Prints the selected menu topic's initial header.

    Args:
        selected_menu_option (str): Selected type of content that is displayed
        selected_topic (str): Selected topic of the selected menu option

    Returns:
        None
    """

    print(f"\n\n{selected_topic.upper()} {selected_menu_option.upper()}:")


# Used by Controller file(s)
def print_selected_topic_sub_header(
        content_type: str, statement_number: int, total_statements: int):
    """
    Prints the selected menu option's topic's sub headers for each statement.

    Args:
        content_type (str): Selected menu option type
        statement_number (int): Statement's number
        total_statements (int): Total number of statements for the selected topic

    Returns:
        None
    """

    print(f"""\n\n{content_type.capitalize()}: {statement_number} (of {total_statements})\n""")


# Used by Controller file(s)
def print_content_statement_and_options(statement: str, sorted_options: list):
    """
    Prints a content statement and its options for the selected menu option's topic.

    Args:
        statement (str): Statement text
        sorted_options (list): List of options

    Returns:
        None
    """

    print_with_line_breaks(statement)
    print_options(sorted_options)


# Used by View file(s)
def print_options(sorted_options):
    """
    Prints the valid options along with their corresponding numerical identifiers.

    Args:
        sorted_options: List of valid options

    Returns:
        None
    """

    for index, option in enumerate(sorted_options):
        print(f"""   [{index}] - {str(option)}""")
    print("\n")


# Used by Controller and View files
def print_with_line_breaks(text: str, total_characters_per_line: int = 79):
    """
    Prints a string of text with line breaks up to a set number of characters.

    Args:
        text (str): Text to be displayed
        total_characters_per_line (int) [default = 79]: Total characters per line,
            PEP 8 Style Guide for Python Code states, "Limit all lines to a maximum
            of 79 characters."

    Returns:
        None
    """

    wrapper = textwrap.TextWrapper(width = total_characters_per_line)
    word_list = wrapper.wrap(text = text)

    for line in word_list:
        print(line)

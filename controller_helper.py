"""
Chat Bot: Helper "Controller" File for the Application
===========================
Course:   CS 5001
Student:  Andrew Jenson
Semester: Fall 2023
Assignment: Final Project

This "Controller" file contains contains the helper functions.
"""

# Note: You can run this file for doctests.

import model_constants # Contains the constants used in the program
import view_terminal # Communicate with this "View" file


def get_index_in_list(item: str, list_to_review: list) -> int:
    """
    Searches a list for a specific item and returns its index (or -1 if the item is not found).

    Args:
        item (str): The item to search for in the list
        list_to_review (list): The list to search in

    Returns:
        int: The index number of the item in the list if found, -1 otherwise.

    Examples:
    >>> item = "quiz"
    >>> list_to_review = ["help", "quiz", "tips"]
    >>> get_index_in_list(item, list_to_review)
    1
    >>> item = "future feature"
    >>> list_to_review = ["help", "quiz", "tips"]
    >>> get_index_in_list(item, list_to_review)
    -1
    """

    # Used 'if item in list' here because regular 'if' statements in python
    # consider a '0' to be False (which could be an item's index number)
    if item in list_to_review:
        return list_to_review.index(item)
    # Item not found in list, return -1
    return -1


def get_topics_as_list(topics: dict) -> list:
    """
    Gets topics from a dictionary of topics and returns the selected topic as a list.

    Args:
        topics (dictionary): Topics to choose from

    Returns:
        list: The list of the selected topics extracted from a dictionary

    Examples:
        Doctests omitted due to potential lengthy doctest string.
    """

    topic_list = []
    for key in topics:
        topic_list.append(key)
    return topic_list


def common_logic_for_tips_and_quizzes(
        selected_option: str, content_type: str, all_content_dict: dict) -> tuple:
    """
    Performs common logic functionality for displaying tips and quizzes.

    This function handles user input for topic selection, displays relevant information,
    and returns the user's performance results.

    Args:
        selected_option (str): The chosen option (quiz or tips)
        content_type (str): They type of content being processed (quiz question or tip)
        all_content_dict (dict): A dictionary containing all available content

    Returns:
        tuple: A tuple containing three integers
            * correct_answers (int): The number of correct answers
            * total_statements (int): The total number of statements presented
            * percentage_correct (int): The percentage of correct answers

    Examples:
        Doctests omitted due to potential lengthy doctest string.
    """

    # Initialize local variables
    selected_topic_dict = {}
    correct_answers = 0
    total_statements = 0
    percentage_correct = 0

    # Get user input for topic selection
    topics_list = get_topics_as_list(all_content_dict)

    view_terminal.print_header_statement_and_options(
                    selected_option,
                    "Select topic:",
                    all_content_dict)

    user_selected_topic_number =  view_terminal.get_valid_input_integer(
                                                    model_constants.PROMPT_GET_NUMBER,
                                                    model_constants.PROMPT_GET_NUMBER_ERROR,
                                                    topics_list)

    user_selected_topic = topics_list[user_selected_topic_number]

    selected_topic_dict = all_content_dict[topics_list[user_selected_topic_number]]

    # Bot provides a friendly transitional comment after users selects a topic
    view_terminal.print_with_line_breaks(model_constants.FEEDBACK_TRANSITION)

    # Topic selected. Display header and iterate through statements and options
    view_terminal.print_selected_topic_header(
                    selected_option,
                    user_selected_topic)

    # Loop through each statement and return results
    correct_answers, total_statements, percentage_correct = loop_through_statements_return_results(
                                                                selected_topic_dict,
                                                                content_type)

    return (correct_answers, total_statements, percentage_correct)


def loop_through_statements_return_results(selected_topic_dict: dict, content_type: str) -> tuple:
    """
    Loops through all statements in a selected topic and returns the user's performance results.

    This function presents each statement and its options, collects user responses, checks their
    answers, and returns the number of correct answers, total statements, and percentage of
    correct answers.

    Args:
        selected_topic_dict (dict): A dictionary containing statements as keys and
            corresponding options as values for a selected topic
        content_type (str): The type of content being presented (quiz question or tip.

    Returns:
        tuple: A tuple containing three integers:
            correct_answers (int): number of correct answers
            total_statements (int): total number of statements
            percentage_correct (int): percentage of correct answers

    Examples:
        Doctests omitted due to potential lengthy doctest string.
    """

    # Initialize local variables
    statement_number = 0
    correct_answers = 0
    total_statements = 0
    percentage_correct = 0

    total_statements += len(selected_topic_dict)

    # loop through all items in dict
    for statement, options in selected_topic_dict.items():

        # **Note:** Correct answer is ALWAYS stored in first element
        # This is how the JSON data was organized (correct answer is first in list)
        # Both correct_answer and user_answer use casefold()
        correct_answer = options[0].strip().casefold()

        sorted_options = sorted(options)
        statement_number += 1

        view_terminal.print_selected_topic_sub_header(
                        content_type,
                        statement_number,
                        total_statements)

        view_terminal.print_content_statement_and_options(statement, sorted_options)

        user_selected_answer = view_terminal.get_valid_input_integer(
                                        model_constants.PROMPT_GET_NUMBER,
                                        model_constants.PROMPT_GET_NUMBER_ERROR,
                                        sorted_options)

        # Get user choice and check if it is correct
        # Both correct_answer and user_answer use casefold()
        user_answer = sorted_options[user_selected_answer].strip().casefold()

        correct_answers += check_answer(content_type, user_answer, correct_answer)

    # Calculate the percentage
    percentage_correct = get_percentage_integer(correct_answers, total_statements)

    return (correct_answers, total_statements, percentage_correct)


def check_answer(content_type_text: str, user_choice: str, correct_answer: str) -> int:
    """
    Evaluates a user's answer against the correct answer and returns a score.

    This function compares the user's answer with the correct answer,
    returning 1 if the answer is correct and 0 otherwise.

    Args:
        content_type (str): The type of content being presented (quiz question or tip)
        user_answer (str): The user's selected answer
        correct_answer (str): The correct answer

    Returns:
        int: 1 if the user's answer is correct, 0 otherwise

    Examples:
    >>> check_answer(model_constants.CONTENT_TYPE_QUIZ_QUESTION, "Wrong answer", "Correct answer")
    🤖 WRONG. ❌ Correct answer was: Correct answer
    0
    >>> check_answer(model_constants.CONTENT_TYPE_QUIZ_QUESTION, "Correct answer", "Correct answer")
    🤖 CORRECT! ✅
    1
    >>> check_answer(model_constants.CONTENT_TYPE_TIP, "Correct answer", "Correct answer")
    1
    """

    # Initialize variable(s)
    number = 0

    # TIP
    if content_type_text == model_constants.CONTENT_TYPE_TIP:
        # Tips ALWAYS return 1 (no wrong right/wrong answer check with tips)
        number =+ 1
        return number

    # QUIZ
    if user_choice == correct_answer:
        correct_answer_message = model_constants.FEEDBACK_CORRECT
        view_terminal.print_with_line_breaks(correct_answer_message)
        number =+ 1
    else:
        wrong_answer_message = (
            f"{model_constants.FEEDBACK_WRONG} "
            f"Correct answer was: {correct_answer.capitalize()}")
        view_terminal.print_with_line_breaks(wrong_answer_message)
        number =+ 0
    return number


def get_percentage_integer(numerator: int, denominator: int) -> int:
    """
    Calculates and returns the percentage as an integer.

    Args:
        numerator (int): The value to be expressed as a percentage
        denominator (int): The total value against which the percentage is calculated

    Returns:
        int: Calculated percentage

    Examples:
    >>> get_percentage_integer(3, 3) # Expected output: 100
    100
    >>> get_percentage_integer(1, 3) # Expected output: 33
    33
    """
    return int(numerator / denominator * 100)


if __name__ == "__main__":  # if doctest is not installed, comment out these lines
    import doctest

    doctest.testmod(verbose=True)

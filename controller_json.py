"""
Chat Bot: A "Controller" File for the Application
===========================
Course:   CS 5001
Student:  Andrew Jenson
Semester: Fall 2023
Assignment: Final Project

This file contains function(s) that communicate with the "Model" (JSON) files.
"""

# Note: You can run this file for doctests.
# Note: Correct answer is ALWAYS stored in first element of JSON data

import json
import model_constants
import view_terminal # used to send any error messages


def read_from_json_file(file_path: str) -> dict:
    """
    Reads a JSON file quiz or tip data and returns a dictionary.

    The function opens the specified JSON file, reads its contents,
    and converts the data into a Python dictionary.

    Args:
        file_path (str): The path of the JSON file to be read

    Returns:
        dict: A dictionary of content (e.g. quizzes or tips)

    Raises:
        FileNotFoundError: If the specified file path is not found
        PermissionError: If access to the file is denied
        json.JSONDecodeError: If the JSON syntax in the file is invalid

    Examples:
        >>> file_path = "model_quizzes.json"
        >>> python_dictionary = read_from_json_file(file_path)
        >>> isinstance(python_dictionary, dict)
        True
        >>> len(python_dictionary) > 0
        True

        >>> file_path = "file_does_not_exist.json"
        >>> python_dictionary = read_from_json_file(file_path)
        ERROR. File not found: file_does_not_exist.json
    """

    # Initialize variable(s)
    # Provided in case JSON file cannot be read
    unexpected_error_handle_dictionary = {
        "Message":{
        str(model_constants.UNEXPECTED_ERROR): ["Next"]}
        }

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            python_dictionary = json.load(file)
            return python_dictionary

    except FileNotFoundError:
        view_terminal.print_json_error("ERROR. File not found:", file_path)
        return unexpected_error_handle_dictionary

    except PermissionError:
        view_terminal.print_json_error("ERROR. File access denied:", file_path)
        return unexpected_error_handle_dictionary

    except json.JSONDecodeError as e:
        view_terminal.print_json_error("ERROR. Invalid JSON syntax:", str(e))
        return unexpected_error_handle_dictionary


if __name__ == "__main__":  # if doctest is not installed, comment out these lines
    import doctest

    doctest.testmod(verbose=True)

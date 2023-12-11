# Final Project Report

* Student Name: Andrew Jenson
* Github Username: awjenson
* Semester: Fall 2023
* Course: CS5001

## Description
This section provides an overview of the program I created for the CS5001 final project.

### CS5002 Chat Bot
A chat bot designed to help Northeastern University students in the [Align Master of Science in Computer Science program](https://www.khoury.northeastern.edu/programs/align-masters-of-science-in-computer-science/) (Align students) succeed in the Discrete Structures course titled CS5002 [(CS5002)](https://www.khoury.northeastern.edu/cs5002-discrete-data-structures-course-charter/). CS5002 is a course that is part of the Align Bridge Coursework and it is meant to provide Align students with an introduction to discrete mathematics, as well as some data structures and algorithms.

The chat bot is a 24/7 learning assistant that features tips and quizzes. When the program is run, the user is presented a Menu with four options: Help, Quiz, Tips, and Quit. The Help option displays informational text about the chat bot. The Quiz option presents the user with several CS5002-related quizzes. The Tips options presents the user with several CS5002-related tips. And, the Quit option quits the program.

| Menu Option        | Description           |
| ------------- |-------------|
| Help | *Displays informational text about the chat bot* |
| Quiz | *Presents the user with several CS5002-related quizzes* |
| Tips | *Presents the user with several CS5002-related tips* |
| Quit | *Quits the program* |

Next semester, I am taking CS5002. Based on several interviews I had with Align alumni, CS5002 is one of the most difficult courses in the Align program. As a result, I decided to use this final project as an opportunity to help prepare me for CS5002. By creating this chat bot, I hope to help my fellow students and I succeed in CS5002. In addition, I got the idea to build a 'CS5002 chat bot' after reading [an article](https://www.pcmag.com/news/harvards-new-computer-science-teacher-is-a-chatbot) about how Harvard created a 'CS50 chat bot' for students enrolled in Computer Science 50: Introduction to Computer Science (CS50).

## Key Features
This sections highlights some of the key features of the program.

### Front-End:

#### Chat Bot:
The chat bot was designed to communicate with users in a friendly, helpful, and direct style. When the user launches the program, the chat bot provides a friendly greeting. When the user quits the program, the chat bot provides a friendly goodbye. The chat bot helps the user navigate through the program by listing out the valid number options anytime the user enters an invalid number. When taking a quiz, if the user enters an incorrect answer, the chat bot notifies that user that they answered incorrectly and provides the correct answer for to help the user learn from their mistake. After the user finishes taking a quiz or reviewing tips, the chat bot presents the user with their results.

#### Navigation:
The program provides users with a simple, intuitive user experience (UX). Unlike other programs that run in the Terminal that require the user to enter characters or words in order to navigate through the program (e.g. `h` or `help`), the user only needs to type integers in order to navigate through all of the menu options and choices displayed (e.g. `0`). This UX design reduces both potential user errors (e.g. the user enters a misspelled word) and potential edge case errors (e.g. the user enters an uppercase letter when a program requires a lowercase letter) which both provide a bad UX.

#### Menu:

The program begins with a menu that displays four options: Help, Quiz, Tips, and Quit.

#### Quiz:
This program contains several CS5002-related quizzes. The source for the quiz content came from the [CS5002 textbook](https://course.ccs.neu.edu/cs1800f22/cs1800_text.pdf). After the user selects the Quiz option, the chat bot presents a list of the available quizzes by topic. After the user selects a topic, that chat bot starts the quiz on that topic. Each quiz consists of several questions. When the quiz is finished, the chat bot displays the user's results.

| Quiz Topics        | Description           |
| ------------- |-------------|
| Number Representations | *Binary representation, bytes, etc.* |
| Circuits | *Transistors, switches, basic logic gates, etc.* |
| Logic | *Truth tables, basic operators, logical equivalence, etc.* |

#### Tips:
This program contains several CS5002-related tips. The source for the tips content came from the [CS5002 textbook](https://course.ccs.neu.edu/cs1800f22/cs1800_text.pdf).After the user selects the Tips option, the chat bot presents a list of the available tips by topic. After the user selects a topic, that chat bot presents the tips on that topic. When the user finishes reviewing a topic's tips, the chat bot displays a summary of the number of tips the user reviewed.

| Tip Topics        | Description           |
| ------------- |-------------|
| General | *General CS5002-related tips* |
| Study Habits | *Good study habit tips* |
| Number Representations | *Binary representation, bytes, etc.* |
| Circuits | *Transistors, switches, basic logic gates, etc.* |
| Logic | *Truth tables, basic operators, logical equivalence, etc.* |


### Back-End:

#### Model View Controller (MVC)
The program uses the Model View Controller (MVC) design pattern. As a result, the program consists of data models, presentation information, and control information. The model files contain JSON data or the program's constants and only communicate with the controller files. The controller files act as intermediaries, communicating data between the model files and the view file. The view file only communicates with the controller files. This design creates organized files that each have a specific purpose.

| File Type (MVC) | File Name              |
| --------------- |------------------------|
| Model           | *model_constants.py*   |
| Model           | *model_quizzes.json*   |
| Model           | *model_tips.py*        |
| View            | *view_terminal.py*     |
| Controller      | *controller_helper.py* |
| Controller      | *controller_json.py*   |
| Controller      | *controller_menu.py*   |


### Code Readability:
A lot of effort was put into which words were best to use for the variables and functions. I constantly referenced the dictionary to ensure that the words used were the most accurate and descriptive word available. Also, I standardized the words across all of the files. My goal was to improve the readability both for myself and others.

I invested time in my code's readability because of the following quotes:
> * *“Programs must be written for people to read, and only incidentally for machines to execute.”* — Harold Abelson
> * *”Any fool can write code that a computer can understand. Good programmers write code that humans can understand.”* – Martin Fowler
> * *”You should name a variable using the same care with which you name a first-born child.”* — Robert C. Martin

### Refactoring:
Once I got my code working, I spent a lot of time refactoring it in order to ensure there was little to no code duplication. I worked hard to follow the *“Don't repeat yourself“* (DRY) principle of software development. As a result, I was able to remove hundreds of lines of duplicate code before submitting my final project. For my variables and constants, I standardized them as much as possible in order to reuse them throughout my program. For functions, I continued to refactor them which reduced their size and ensured that each function only had a single, well-defined responsibility. As a result, I was able to improve the reusability of several functions.

## Guide
This section explain how to run the program and provide screenshots of what the program looks like and its features. 

### Run the Program
To run the project locally, in the **Terminal**, run:

```bash
python3 controller_menu.py
```

At the start of the program, the Terminal displays a printed welcome message and then a printed Menu that lists several numbered options that the user can choose (e.g. Help, Quiz, Tips, and Quit). Enter a number available to select the desired option.


### Screenshots
The following screenshots provide a visual example of what to expect when you run the program. The screenshots display the full walkthrough of the program, including its key features: Quizzes and Tips. To navigate through the program, users enter a valid number whenever the CS5002 Chat Bot asks for user input.

 * [Screenshot 1: Run program in the Terminal](https://drive.google.com/file/d/1gxiTB9mjicME6IOOXKqWaTg_OmUbhRYi/view?usp=sharing "Run the program in the Terminal")

 * [Screenshot 2: Menu at launch](https://drive.google.com/file/d/19RaBsv6Q195MvIOs_JwWJtpmkl3_0sMU/view?usp=sharing "Menu at launch")

 * [Screenshot 3: Help - informational text](https://drive.google.com/file/d/11d60w99rXsAt0c1H4YmeTwbMxIOFZF-c/view?usp=sharing "Help - informational text")

 * [Screenshot 4: Return to the Menu](https://drive.google.com/file/d/1nc6aC-O6Hb_FD2CSe-JJNlAAM6Yk0Irs/view?usp=sharing "Return to the Menu")

 * [Screenshot 5: Quiz - Selecting a Topic](https://drive.google.com/file/d/1ErpLruiLkoPHAYZnul6DyQJqOKROfm6d/view?usp=sharing "Quiz - Selecting a Topic")

 * [Screenshot 6: Quiz - Question 1 (of 3)](https://drive.google.com/file/d/1RMj3y-G245hdaPpVvH1DmGfFGSG0SEf4/view?usp=sharing "Quiz - Question 1 (of 3)")

 * [Screenshot 7: Quiz - Question 2 (of 3)](https://drive.google.com/file/d/1rp0UVMwt8JWym05QpyLd_ry1o00A8GQZ/view?usp=sharing "Quiz - Question 2 (of 3)")

 * [Screenshot 8: Quiz - Question 3 (of 3)](https://drive.google.com/file/d/1nn1k5J4OiRA61-ki800UU8t3SALOXiGX/view?usp=sharing "Quiz - Question 3 (of 3)")

 * [Screenshot 9: Return to the Menu](https://drive.google.com/file/d/1GhjgFDGtF4WWilH4-kK4h5HjgC5IXTOC/view?usp=sharing "Return to the Menu")

 * [Screenshot 10: Tips - Selecting a Topic](https://drive.google.com/file/d/1BjarWIyxcToq5XFUEDM4SpG1r8g-LC7i/view?usp=sharing "Tips - Selecting a Topic")

 * [Screenshot 11: Tips - Tip 1 (of 3)](https://drive.google.com/file/d/1DeLwUvXGKBMEYgQ7WMxWTpgQY9wO37r7/view?usp=sharing "Tips - Tip 1 (of 3)")

 * [Screenshot 12: Tips - Tip 2 (of 3)](https://drive.google.com/file/d/1w_0Lre8PHtDVkWazYw-Zf-AL1wIAgTzG/view?usp=sharing "Tips - Tip 2 (of 3)")

 * [Screenshot 13: Tips - Tip 3 (of 3)](https://drive.google.com/file/d/1BgAE1Wm6JUsRq_HVIN4CTRljcTjcdlS3/view?usp=sharing "Tips - Tip 3 (of 3)")

 * [Screenshot 14: Return to the Menu](https://drive.google.com/file/d/1rcEdFzzmexEWDOnyYRsZNf-LTU2exg6f/view?usp=sharing "Return to the Menu")

 * [Screenshot 15: Quit the program](https://drive.google.com/file/d/1CiEMyD_ERxP7tLiKzzjdZ4SzwfMHAhze/view?usp=sharing "Quit the program")


## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

To run the project locally, in the **Terminal**, run:

```bash
python3 controller_menu.py
```

The `controller_menu.py` file is the file that runs the program.


## Code Review
This section provide a review of the program's files and the key aspects of the code.

### Models
The program has three Model files:
 * `model_constants.py`
 * `model_quizzes.json`
 * `model_tips.json`

#### model_constants.py
Many of the program's constants are stored in the `model_constants.py` file. By defining a constant value once and reusing it throughout my code, I reduce the need for repetitive code and improve its overall maintainability. If a constant's value needs to be change, I only need to update the constant definition in one place, ensuring the change is reflected throughout my entire codebase.

```python
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
```

#### model_quizzes.json
A single json file was used to store the 'Quiz' data. This helps maintain an organized project folder. For consistency purposes, the correct answer is **always** the first item each list. The source for the quiz content came from the [CS5002 textbook](https://course.ccs.neu.edu/cs1800f22/cs1800_text.pdf). Currently, quizzes only cover the first three chapters. But, I plan to add more chapter quizzes in the future.

```json
{
    "Number Representations": {
      "A ________ is an 8-bit binary number with leading zeros allowed.": [
        "byte",
        "yard",
        "meter",
        "mile"
      ],
      "This way of representing numbers (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) is called the decimal or ________ system.": [
        "base 10",
        "base 2",
        "base 16",
        "base 10,000"
      ],
      "Numbers on computers are represented with just ________ (bits), using the binary or base 2 system.": [
        "0 and 1",
        "1 and -1",
        "dollars and cents",
        "latitude and longitude"
      ]
    },
    "Circuits": {
      "Computer components are constructed from digital circuits which are constructed from ________ gates": [
        "logic",
        "sound",
        "light",
        "stone"
      ],
      "Unlike the AND and OR gates, the NOT gate has only one input, and its output is simply the ________ of its input.": [
        "opposite",
        "same",
        "repeat",
        "multiplication"
      ],
      "An OR gate takes two inputs and is “on” so long as at least one of the inputs is ________.”": [
        "on",
        "off",
        "missing",
        "invisible"
      ]
    },
    "Logic": {
      "The AND operator is denoted by the symbol ____.": [
        "∧",
        "∨",
        "⊕",
        "≡"
      ],
      "In logic, ________, also called the logical not is represented as ¬ (e.g. ¬A) or NOT (e.g. NOT A).": [
        "negation",
        "conjunction",
        "disjunction",
        "correlation"
      ],
      "One of the boolean algebra laws is ________.": [
        "De Morgan’s law",
        "Tort law",
        "Newton's Third Law of Motion",
        "Criminal law"
      ]
    }
  }
```

#### model_quizzes.json
A single json file was used to store the 'Tips' data. This helps maintain an organized project folder. For consistency purposes, there is only one option the user can choose to move to the next tip (or to go to the main Menu). As displayed below, that option is the "Next" option and it is **always** the first item each list. The source for the tips content came from current CS5002 students, Reddit forums, and the [CS5002 textbook](https://course.ccs.neu.edu/cs1800f22/cs1800_text.pdf). Currently, tips only cover the first three chapters. But, I plan to add more chapter tips in the future. 

```json
{
    "General": {
        "When watching the module videos, pause after they solve a new type of problem and try to solve one on your own. (The textbook often has example problems or you can slightly change the values of the problem from the video).": ["Next"],
        "Before taking the class, read problem solving books first. Book recommendations include “Problem-Solving Strategies” by Arthur Engel or “The Art of Problem Solving, Vol. 1: The Basics” by Sandor Lehoczky and Richard Rusczyk.": ["Next"],
        "Be aware that this class is probably unlike any other math class you have ever had before, so you should not expect the same practices that got you through earlier math classes to get you through this class.": ["Next"],
        "TrevTutor and Kimberly Brehm on YouTube make good videos on discrete math.": ["Next"],
        "Don’t fall behind on the coursework because the class can get very hard very fast.": ["Next"]
    },
    "Study Habits": {
        "Study with other people and work through exercises with other people.": ["Next"],
        "Do not study where there are distractions (e.g. bad lighting or noises).": ["Next"],
        "Avoid dehydration.": ["Next"],
        "Avoid hunger (and junk food).": ["Next"]
    },
    "Number Representations": {
        "Numbers on computers are represented with just 0 and 1, using the binary or base 2 system.": ["Next"],
        "A byte is an 8-bit binary number with leading zeros allowed.": ["Next"],
        "There are 256 different bytes and they represent the integers from 0 (00000000) to 255 (11111111).": ["Next"]
    },
    "Circuits": {
        "The basic logic gates are the AND, OR, and NOT gates. Other logic gates are NAND, NOR, XOR, and XNOR.": ["Next"],
        "AND Gate: Given two inputs (A and B) which can each take on two values (0 or 1), there are four possible input pairs to the AND gate.": ["Next"],
        "NOT Gate: Unlike the AND and OR gates, the NOT gate has only one input, and its output is simply the opposite of its input.": ["Next"]
    },
    "Logic": {
        "Truth Tables: In logic, variables may take on one of two truth values (T or F), and these variables are manipulated and combined by various logical operators (e.g. AND, OR, and NOT).": ["Next"],
        "Conjunction is a truth-functional connective similar to “and“ in English and is represented in symbolic logic as “∧“.": ["Next"],
        "Two Boolean formulas are said to be logically equivalent if they have the same truth table, i.e., they always have the same truth values for any given input. For example, ¬(¬p) is logically equivalent to p.": ["Next"]
    }
}
```


### Views
The program has one View file:
 * `view_terminal.py`

#### view_terminal.py
Currently, the only way to run the program is through the **Terminal**. In the future, I plan to create a web app.

##### get_valid_input_integer
`get_valid_input_integer` is one of the most important functions in this program. It handles the user's input. I designed my program to only accept valid integers. To goal was to reduce complexity for the user and, therefore, provide a good UX. This function contains a `while` loop with a `try except` statement. If a user enters invalid input, such as no data, any non-integer characters (e.g. ValueError), or invalid integers (e.g. negative integers or integers out or range) then this function prints an error message and the `while` loop continues until the user inputs a valid integer.

```python
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
```

##### print_header_statement_and_options
`print_header_statement_and_options` is a good example of using other functions to accomplish a task. The function's parameters (`header`, `statement`, and `options`) are all feed into another function and which print text, in a specific design, to the Terminal.

```python
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
```

##### print_with_line_breaks
`print_with_line_breaks` was created to provide a good UX since the user is interacting with the program via the Terminal. The [PEP 8 Style Guide for Python Code](https://peps.python.org/pep-0008/) states, *"Limit all lines to a maximum of 79 characters."* As a result, I decided to have all of the long-form text strings confirm this this guideline. The default `total_characters_per_line` was set to `int = 79`. In the future, this function's default value may change when the View file changes to connect to a web app.

```python
import textwrap

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
```


### Controllers
The program contains three Controller files:
 * `controller_menu.py`
 * `controller_json.py`
 * `controller_helper.py`

#### controller_menu.py
This Controller file contains the program's 'Menu' related functions, including the functions for the program's features: Help, Quizzes, and Tips.

##### run_menu
After the program is run, the 'Menu' text is printed to the Terminal for the user to read and navigate through the program. `run_menu()` is a simple function that first sets up a variable called `menu_options` which is a `list` data type and stores the options available (Help, Quizzes, and Tips).

The function contains a `while` loop that then contains an `if elif else` statement. If the user provides the input for the 'Quit' option, then a `break` statement results in the program to exit the `while` loop. If the user inputs the 'Help' options, then the program will call `run_help()`. If the user selects either the 'Quiz' or 'Tips' options, then program first calls the `controller_json.read_from_json_file`, collects the selected option's model data (e.g. quizzes or tips), and stores them as a dictionary of dictionaries. With this data, the program then feeds it into one of the following functions, `run_quiz(all_quizzes_dict)` or `run_tips(all_tips_dict)`, depending on the option selected.

```python
import model_constants
import view_terminal
import controller_helper


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
```

#### controller_json.py
This Controller file contains the function for reading JSON data.

##### read_from_json_file
The `read_from_json_file` function reads a JSON file in order to get either the 'Quiz' or 'Tips' data. In case this function is unable to successfully read a JSON file, rather than have the program crash, I included a variable called `unexpected_error_handle_dictionary` that consists of a simple dictionary of text, and it gets used to inform the user that the program was unable to get the the 'Quiz' or 'Tips' data and to please try again. The error handling is done inside a `try except` statement.

```python
import json
import model_constants
import view_terminal


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
```

#### controller_helper.py
This Controller file contains the helper functions.

##### common_logic_for_tips_and_quizzes
After building the `run_quiz()` and `run_tips()` functions, I refactored them and created the `common_logic_for_tips_and_quizzes` function. This function handles user input for topic selection, displays relevant information, and returns the user's performance results.

```python
import view_terminal
import model_constants


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
```

##### loop_through_statements_return_results
After I initially refactored my code with the `common_logic_for_tips_and_quizzes` function, I realized I could continue to refactor my code by creating a function that loops through each of the 'Quiz' and 'Tips' data statements and return the results. As a result, I created this function, `loop_through_statements_return_results`. This function presents each statement and its options, collects user responses, checks their answers, and returns the number of correct answers, total statements, and percentage of correct answers.

```python
import view_terminal
import model_constants


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
```

##### check_answer
Further, after I initially refactored my code with the `common_logic_for_tips_and_quizzes` function, I realized I could continue to refactor my code by creating the `check_answer` function. For 'Tips', since the only option the user can select is the 'Next' option and there are not right or wrong answers, this function first checks if the `content_type_text` equals 'Tips' and simply returns a `1`. For 'Quiz' questions, and `if else` statement is used to identify if the `user_choice`'s value is equal to the `correct_text`'s value. If `True`, the number returned is `1`. Otherwise, the number returned is `0`.

```python
import model_constants
import view_terminal

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
```


## Major Challenges
This section provides a summary of the major challenges I faced when working on this final project.

### Project Due Date
As [stated by the instructor](https://github.com/CS5001-khoury/FinalProjectTemplate/tree/main/instructions), *"The first part of the project is a staff (instructor or TA) to get approval for your project. We do this, because people often create projects that are often too large."* The project's due date challenged me to think smaller when it came to the final program that I submitted for the final project. Due to the lack of time, I had to make hard decisions about what to include versus exclude. When deciding on what to include, I followed the MoSCoW method developed by Dai Clegg in 1994 [(Wikipedia)](https://en.wikipedia.org/wiki/MoSCoW_method). *"MoSCoW is an acronym derived from the first letter of each of four prioritization categories: M - Must have, S - Should have, C - Could have, W - Won't have."* As a result, I did my best to include the 'must have' features based on the final project's [grading rubric](https://northeastern.instructure.com/courses/161511/assignments/1922669). For example, I spent most of my time ensuring that the logic code for my quizzes and tips worked and I had to sacrifice the actual content of the quizzes and tips that are stored in the JSON files.

### Code Refactoring
Code refactoring took several days to clean-up repetitive code and restructure my files [(Code Refactoring)](https://en.wikipedia.org/wiki/Code_refactoring). From the beginning, my coding strategy was to design each feature to be similar so that I could refactor my code. For example, I tried to re-use a limited number of the constants I created and design the functions that handle the quizzes and tips to be similar. Even after refactoring a lot of my code, it appears that there is still good amount of code left that can be refactored. As a result, it appears that refactoring is a never ending process and so I needed to balance this with the projects' due date.

### JSON Files
Since CS5001 did not contain any homework assignments on building a JSON file, I researched how to create a JSON file and converted my model data (e.g. tips and quizzes) into JSON data [(JSON)](https://en.wikipedia.org/wiki/JSON). This took extra time to build and test [(JSON Formatter & Validator)](https://jsonformatter.curiousconcept.com/#). As a result, instead of creating a lot of content for my program (e.g. adding lots of quizzes with a lot of questions in each quiz), I decided spend my available time learning how to build and implement JSON files into my program.

### Model View Controller (MVC)
For building version 1 (V1) I built my code in one python file to ensure that the program ran correctly without any bugs. Afterwards, for V2, in order to confirm to the [MVC design pattern](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller), I spent a few days creating new files and moving my code into the proper files. As a result, I had to update my code in the Controller files so that they could reference functions or constants in other files. The most difficult part was moving all of the constants into their own constants model file. This decision took a lot of time to complete because I only wanted my controller files to reference the constants in order to follow the MVC design pattern.

### Naming Convention
I spent a lot of time thinking of the most descriptive variables and functions. I compared words in the dictionary in order to select the most descriptive word. Furthermore, I tried to determine which words would make the most sense to other readers. I realized that writing good code takes a lot of time. And, sometimes the *"right"* answer can be subjective and up for debate. While I may believe a coding choice is "right" and I can support it with evidence, there may be another programmer who disagrees and have their own evidence to support their opinion. Overall, it's best to follow existing industry guidelines.

### Error Handling
I spent a lot of time debugging, testing for edge cases, and creating error handling code. While I am happy with the error handling that I have added, I realized that error handling likely is a never ending task. My test files showcase my efforts to reduce errors/bugs in my code.


## Example Runs
This section provides an example run of the program.

### YouTube Video
The following [URL](https://www.youtube.com/watch?v=XaQWKgJy7sk) is a video tutorial walkthrough of my program.

>CS5001 Final Project Video Tutorial - A CS5002 Chat Bot:
>
>**https://www.youtube.com/watch?v=XaQWKgJy7sk**


## Testing
I tested my code using **doctests** and **command line redirection**.

The doctests run in the Terminal, check to ensure all tests included in a docstring pass or fail. The test results are printed to the Terminal. To do this, I imported the `doctest` module. Command line redirection, which also runs in the Terminal, takes data from an input file and outputs the program results into another file. This redirecting of input is done using the `<` (less-than symbol) operator. And, the redirection of output is done using the `>` (greater-than symbol). In addition, I used the `diff` command to check for differences in my test output files. The usage is as follows: `diff file1 file2` in mac and linux or `diff (cat file1) (cat file2)` in windows. 

An example of command line redirection is:
```bash
python3 controller_menu.py < test_input.txt > test_output.txt
```

### doctest files:
 * test_doctest_controller_helper_py.txt
 * test_doctest_controller_json_py.txt

### Redirection files
 * test_1_input_help_no_errors.txt
 * test_1_output_help_no_errors.txt
 * test_2_input_help_many_errors.txt
 * test_2_output_help_many_errors.txt
 * test_3_input_run_all_features_no_errors.txt
 * test_3_output_run_all_features_no_errors.txt
 * test_4_input_run_all_features_many_errors.txt
 * test_4_output_run_all_features_many_errors.txt


## Missing Features / What's Next
This section outlines my proposed next steps for further developing this program.

### Content
For the final project, I only included a few quizzes and tips from the first three chapters of the [CS5002 textbook](https://course.ccs.neu.edu/cs1800f22/cs1800_text.pdf). This should be sufficient to showcase the CS5002 Chat Bot for the final project. Going forward, I want to add quizzes and tips for all of the chapters in the the CS5002's textbook. Also, I would like to offer other types of quizzes or tips that consider students' different learning styles.

### Classes
Creating a `Tip` class and a `Quiz` class seem to be good opportunities to write cleaner and more organized code. I would be interested to get more practice with building my own classes and to see what other classes I could created within my existing code. In addition, because I plan to create more chat bots, I can also create a `ChatBot` class.

### ChatGPT API
Initially, my plan was connect to [OpenAI's API](https://openai.com/product) and have ChatGPT generate the tips and quizzes. However, because I have never used a third party API and because connecting to an API was not part of the [grading rubric](https://northeastern.instructure.com/courses/161511/assignments/1922669), I decided to only add this feature if I had the available before the final project's due date. In the future, this would be a great feature to add because it would solve the problem above of having little content, it would be a great learning opportunity to learn how to use third-party APIs, and it would be interesting to gain experience on how to utilize artificial intelligence (AI) within software products.

### Web App
Initially, I was going to try a use [Flask](https://flask.palletsprojects.com/en/3.0.x/), a web application framework written in Python, in order to build a web application for my final project. However, because I have never used a third party API and because connecting to an API was not part of the [grading rubric](https://northeastern.instructure.com/courses/161511/assignments/1922669), I decided to only add this feature if I had the available before the final project's due date.

### Refactoring
This appears to be an ongoing task all computer programmer do with their software programs. After talking with the instructor, there is still more refactoring that I can do with the functions that handle running the quizzes and tips by breaking out more of the single tasks into separate functions.

### My MVC Design
While I made good progress setting up my code to have a MVC design. I want to refactor the Controller and View files to more seamlessly handle switching the interface from the Terminal to a Web App. I believe the way that I setup the communication between the Controller and View files were not designed correctly.

### Create Accounts (Login/Password)
While I want to let new users use the app without having to create a username and password, I do want to allow users to create accounts. This will allow the program to store user information such as the statistics on all of the quizzes they have completed. Once quiz data can be store in a user's account they I can add value by doing data analysis to highlight the user's progress with their historical quiz results.

### User Profile
I would like to write to a JSON file that stores user information and their inception-to-date quiz statistics so they can view their progress. Storing more user information will make this application more "sticky", meaning it will keep users coming back to use this program.

### Additional Chat Bots
If my code follows good MVC design, then I should be able to make a lot more chat bots simply by making a few edits in my code and by reading JSON data from different data models (that contains different quizzes and tips). As a result, I should be able to make a chat bot for all classes taught at Northeastern University.

### Additional Schools
Once I have successfully launched chat bots for all classes at Northeastern University, then I should be able to expand to other universities and schools (K-12). This expansion strategy is similar to Facebook's strategy. According to a [LinkedIn article](https://www.linkedin.com/pulse/facebook-early-days-journey-millions-users-sam-adekunle/), *"It [Facebook] started as a networking platform exclusively for Harvard students. After gaining traction at Harvard, Facebook expanded to other Ivy League universities and eventually to colleges and universities across the United States. Facebook continued to expand by opening its doors to high school students and gradually making the platform available to users outside the United States. This international expansion significantly increased its user base."*

### Business Model
In order to create better chat bots that continue to add more value for the users, I plan to generate revenue from these chat bots in order to cover the growing cost of hiring employees, research & development, and sales & marketing to build the best chat bots. If these chat bots are adding value to users then there should be a business model that can create a growing and profitable business.

### Mobile App
After creating a web app, I would consider creating both an iPhone app and an Android app. This could increase the number of users and, therefore, generate more revenue for the business. By allowing users to run the program on a mobile phone, users will benefit because they can run the program while on the go or at times when they are not near a computer. From a business standpoint, this decision should help to increase my program's daily active users (DAU) metric.


## Final Reflection
This section provides a summary of my experience in CS5001 during the Fall 2023 semester.

### What did I learn?

CS5001 is course taught at Northeastern University that provides students with an introduction to computing and programming. CS5001 was my first graduate-level course, my first computer science course, and my first university course that was taught online, asynchronously. So, in addition, to learning the course material, I also learned how to study at a graduate level and the logistics and time management required to study online, asynchronously.

The first half of the course began with teaching the fundamentals of computer programming which includes modules and homework assignments on data types, functions, and loops. The second half of the class focuses on computational thinking and which includes modules and homework assignments on recursion, error handling, advanced data types, data structures, and algorithmic efficiency. The programming language used in the modules, team activities, and the homework was [Python](https://www.python.org/). Furthermore, we learned how to use the Terminal, how to write code in an integrated development environment (e.g. [VSCode](https://code.visualstudio.com/)), and how to create a [GitHub](https://github.com/) profile.

| Module | Title                            |
| -- |--------------------------------------|
| 01 | *Introduction*                       |
| 02 | *Boolean Expressions & Conditionals* |
| 03 | *Functions and Testing*              |
| 04 | *Loops*                              |
| 05 | *Strings and Lists*                  |
| 06 | *Midterm Exam*                       |
| 07 | *Recursion*                          |
| 08 | *Error Handling*                     |
| 09 | *Dictionaries and Sets*              |
| 10 | *Classes & Objects*                  |
| 11 | *Stacks & Queues*                    |
| 12 | *Efficiency: Searching & Sorting*    |
| 13 | *Final Project*                      |

In addition to learning the course material, I realized that a graduate course requires a lot more hours per week to complete the homework assignments than my undergrad courses. And, because the course was taught online, asynchronously, I had to become a self-starter and manage my own workload. I created my own weekly schedule. Most of the homework assignments took me multiple days to complete. As a result, I quickly learned to start the assignments early, routinely schedule weekly meetings with the Instructor and TAs, and post questions onto the CS5001 Microsoft Teams channel.

### What do I need to do to learn more?

This course provided me with an introduction in computer programming. But, I still have a lot more to learn. While I believe that I now have a strong foundation in the basic fundamentals of computer science, I am less confident in the more advanced topics that were taught in the second half of this class. For example, recursion is one of the topics that I don't fully understand yet. During that module, I scheduled meetings with the Instructor and TAs in order to help grasp this topic. But, I don't feel confident yet in being able to explain or write an advanced recursive function. Classes is another topic that I want to better understand. For example, I decided to not create classes for my final project because I didn't feel confident in correctly building them and using them. Also, I don't fully understand why, when, and how to use stacks and queues in a computer program because we didn't have a homework assignment on it.

GibHub is a software that we used for this final project. While I have a basic understanding of GitHub, I want to learn how to use it in a professional setting. To be honest, I still don't fully understand how to create branches, make commits, or push my code to GitHub. As a result, a fear that I had when completing this final project was that I would finish my program successfully but be unable to push/merge it to my GitHub profile and, therefore, receive 0 points for my final project.


**Key takeaways?**
The key takeaways from CS5001 was all of the computer programming topics that I learned. What was great about this course is that while it taught me how to analyze a problem, how to divide and organize a problem into appropriate components for writing code, this same skill and logical thinking helped me manage my coursework and complete my homework on time. So, I am excited to continue to learn how to think like a programmer. It seems like a helpful skill to have in life. Because I enjoyed this course, I feel confident that I will enjoy computer programming as a career. I am eager to learn the more advanced computer science topics in future classes.

The module videos provided a nice structure for the course. The team activities allowed me the ability to talk through problems and questions with my fellow classmates. I heard that being able to teach something to another person helps you learn too. So, I'm glad the team activities were part of this course.

The final project was the best part of this course because I started I began with a blank Python file and over the course of a few weeks I was able to build a fully operational program by myself. The final project provided me with the opportunity showcase my skills and to practice building a complex computer program. I enjoyed writing this README file because I am proud of my final project.

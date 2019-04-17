# Instructions for Sprint B

## Objectives

- Demonstrate decoupling application logic from [views](http://flask.pocoo.org/docs/1.0/views/)
- Demonstrate benefits of decoupling in terms of code reuse and unit testing.

## Introduction

In sprint A we defined a minimal Flask application project structure as a Python package with four modules: \_\_init\_\_.py, app.py, helpers.py, and test_helpers.py. The four modules were included in the definition of a minimal Flask application because they represent a clean separation of concerns:

- all application routes and configuration are included in the app module
- all application logic is included in the helpers module
- all unit tests for the helpers module are included in the test_helpers module

In this assignment we will continue where sprint A concluded by:

1. decoupling application logic from views using "helper" functions and classes.
2. unit testing blocks of application logic.
3. serving views of epithets and the insult kit vocabulary.

## Adding Application Logic

### The helpers.py File

This module will be used to define much of our application logic before demonstrating more extensible ways of structuring projects. At this point, what is important is that we want to separate application logic from views as much as possible to promote code reuse and simplify testing. For example, to generate epithets for this assignment we'll need to:

1. read a file containing the [Shakespeare Insult Kit](http://www.pangloss.com/seidel/shake_rule.html) .
2. convert the contents of the file to a dictionary of lists keyed for each column of words in the insult kit.
3. select a random word from each column in column order.
4. create a formatted string of the randomly selected words.

Without separating application logic from views, each view would have redundant implementations of these four behaviors. As views are added, the redundant code will quickly become difficult to maintain. Instead, we'll keep our application [DRY](https://code.tutsplus.com/tutorials/3-key-software-principles-you-must-understand--net-25161) by factoring out classes to encapsulate these behaviors.

- Add the following class to the helpers.py file. It'll be used to handle file loading for you.

    ```python
    import json

    class Vocabulary:
        """
        Handle loading in a JSON file with proper unfinished swears in it!

        Usage:
            data = Vocabulary.read_json("/path/to/data.json")
        """

        def read_json(path, mode='r'):
            with open(path, mode=mode) as handle:
                return json.load(handle)
    ```

## Assignment

We now have everything we need to start the assignment. If you haven't done so already, please add the provided classes to the helpers.py file and complete the remainder of the assessment.

1. Unit test the provided class.
2. Define an EpithetGenerator class with methods to:
    1. select one random word from each column of the list.
    2. generate a quantity of epithets from a vocabulary file loaded from a path.
3. Unit test the EpithetGenerator class.
4. Use the EpithetGenerator class in the '/' route to serve a randomly generated epithet.
5. Use the Vocabulary class in the '/vocabulary' route to serve the vocabulary used to generate the epithet.
6. In the helpers.py file, add docstrings explaining what each code block does, for both provided and created classes.

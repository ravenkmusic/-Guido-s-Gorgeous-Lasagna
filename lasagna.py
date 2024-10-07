"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_bake_time


def preparation_time_in_minutes(number_of_layers):
    """"Calculate the preparation time of the lasagna.

    :param number_one: int number of layers.
    :return: total preparation time of lasagna in minutes.

    Takes number of layers and multiplies it by two, where two equals the number of minutes to prepare each layer.

    """
    preparation_time = number_of_layers * 2
    return preparation_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed cooking time of lasagna.

    :param number_one: int number of layers.
    :param number_two: int elapsed bake time in minutes.
    :return: int total time elapsed in minutes of preparation and cook time of lasagna

    Takes sum of preparation time of lasagna by total number of layers and the elapsed bake time and returns the total amount of time in all.

    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time

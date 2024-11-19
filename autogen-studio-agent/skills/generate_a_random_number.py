import random
from typing import Annotated


def generate_a_random_number(min_value: Annotated[int, "Generate number from"], max_value: Annotated[int, "Generate number to"]) -> int:
    """
    Function to generate a random number between 1000 and 9999.

    :param: 

    :return: A random number between 1000 and 9999.
    """

    return random.randint(min_value, max_value)


# Example usage of the function:
# generate_a_random_number(100, 200)

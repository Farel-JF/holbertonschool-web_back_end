from typing import Callable
"""function make_multiplier that takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier."""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns Callable[[float], float]: A function that takes a float as input
    and returns the product of the input and the multiplier."""
    def multiplier_function(value: float) -> float:
        """Returns float: The result of multiplying the value by the multiplier
        """
        return value * multiplier

    return multiplier_function

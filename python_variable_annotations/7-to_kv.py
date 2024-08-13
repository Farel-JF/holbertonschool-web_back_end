#!/usr/bin/env python3
"""This module provides a function to create a tuple with a string and the
square of a number. It takes a string and an integer or floating-point number
as arguments and returns a tuple. The first element of the tuple is the string,
and the second element is the square of the number."""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns Tuple[str, float]: A tuple where the first element is k and the
    second element isthe square of v, converted to a float."""
    return (k, float(v ** 2))

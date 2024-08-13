#!/usr/bin/env python3
"""
This module provides a function to sum all elements in a list of floats. It
takes a list of floating-point numbers as an argument and returns their sum as
a float."""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns float: The sum of all the elements in the input list."""
    return float(sum(input_list))

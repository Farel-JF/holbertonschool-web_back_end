#!/usr/bin/env python3
"""This module provides a function to sum all elements in a list of mixed
integers and floats. It takes a list of integers and floating-point numbers as
an argument and returns their sum as a float."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns float: The sum of all the elements in the input list."""
    return float(sum(mxd_lst))

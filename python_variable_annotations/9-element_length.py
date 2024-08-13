#!/usr/bin/env python3
"""This module provides a function to compute the length of sequences in an
iterable. It takes an iterable of sequences and returns a list of tuples. Each
tuple contains a sequence and its length."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns List[Tuple[Sequence, int]]: A list of tuples where each tuple
    contains a sequence"""
    return [(i, len(i)) for i in lst]

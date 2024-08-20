#!/usr/bin/env python3
"""Module for asynchronous number generation."""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronous generator that yields 10 random float numbers.
    The generator will:
    - Wait asynchronously for 1 second before yielding each number.
    - Generate random float numbers between 0 and 10.
    Yields:
    float: A random float number between 0 and 10."""
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

#!/usr/bin/env python3
"""Module to execute multiple coroutines concurrently."""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Runs the wait_random coroutine n times with the given max_delay and returns
    a list of all delays in ascending order.

    Args:
    n (int): The number of times to run the wait_random coroutine.
    max_delay (int): The maximum delay for each wait_random coroutine.

    Returns:
    List[float]: A list of delays in ascending order. Each delay is a float.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]

    return sorted(delays)

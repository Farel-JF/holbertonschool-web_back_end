#!/usr/bin/env python3
"""Module to create and return an asyncio Task using wait_n."""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates and returns an asyncio Task that runs wait_n with the given
    parameters.

    Args:
        n (int): Number of times to run the wait_random coroutine.
        max_delay (int): Maximum delay for each wait_random coroutine.

    Returns:
        asyncio.Task: A Task object that runs the wait_n coroutine.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

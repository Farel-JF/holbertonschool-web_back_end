#!/usr/bin/env python3
"""Module to create and return an asyncio Task."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Runs `wait_random` n times with the specified max_delay and returns a list
    of delays.

    Args:
        n (int): Number of times to run the wait_random coroutine.
        max_delay (int): Maximum delay for each wait_random coroutine.

    Returns:
        List[float]: List of delays in the order they complete.
    """

    return asyncio.create_task(wait_random(max_delay))

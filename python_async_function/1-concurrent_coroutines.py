#!/usr/bin/env python3
"""Module to execute multiple coroutines concurrently."""

import wait_random
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Returns list[float]: List of all delays in ascending order."""

    tasks = [asyncio.create_task(wait_random(n, max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_complete(tasks)]
    return delays

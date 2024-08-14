#!/usr/bin/env python3
"""Module to execute multiple coroutines concurrently."""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list[float]: List of all delays in ascending order."""

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return sorted(delays)

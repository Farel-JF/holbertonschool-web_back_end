#!/usr/bin/env python3
"""Module to measure the runtime for parallel asynchronous comprehensions."""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension four times in parallel and measures the
    total runtime.

    Returns:
    float: The total runtime for executing the four async_comprehension tasks
    in parallel."""
    step1 = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    step2 = time.time()
    return step2 - step1

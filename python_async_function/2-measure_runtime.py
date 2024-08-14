#!/usr/bin/env python3
"""Module to measure the runtime of wait_n."""

import asyncio
import time
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Measures the average time per coroutine in wait_n.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average time per coroutine, or 0 if n is 0.
    """
    if n <= 0:
        return 0.0

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
#!/usr/bin/env python3
"""Module to measure the runtime of wait_n."""

import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
     """Returns float: Average time per coroutine."""
     start_time = time.time()
     asyncio.run(wait_n(n, max_delay))
     total_time = time.time() - start_time
     return total_time / n

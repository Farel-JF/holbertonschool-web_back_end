Asynchronous Number Generation and Runtime Measurement
This project demonstrates asynchronous programming in Python using asyncio. It includes modules for generating random numbers asynchronously, collecting these numbers with async comprehension, and measuring the runtime for executing tasks in parallel.

Modules
1. 0-async_generator.py
Description:
This module defines an asynchronous generator that yields 10 random float numbers. Each number is generated with a 1-second delay to simulate an asynchronous operation.

Key Function:

async_generator() -> AsyncGenerator[float, None]
Asynchronously yields 10 random float numbers between 0 and 10.
2. 1-async_comprehension.py
Description:
This module defines a coroutine that uses async comprehension to collect 10 random numbers from the async_generator defined in 0-async_generator.py. It returns the collected numbers as a list.

Key Function:

async_comprehension() -> List[float]
Collects 10 random float numbers from async_generator and returns them in a list.
3. 2-measure_runtime.py
Description:
This module measures the total runtime for executing the async_comprehension coroutine four times in parallel. It demonstrates how to run multiple asynchronous tasks concurrently and measure the elapsed time.

Key Function:

measure_runtime() -> float
Executes async_comprehension four times concurrently and returns the total runtime.
Running the Scripts
Requirements
Python 3.7 or later
No additional packages required beyond the standard library
Running the Scripts
Generate Random Numbers Asynchronously

Execute the async_generator script to generate random numbers:

bash
Copy code
python3 0-async_generator.py
Note: This script itself does not have a standalone execution function but is intended to be used by other scripts.

Collect Random Numbers Using Async Comprehension

Execute the async_comprehension script:

bash
Copy code
python3 1-async_comprehension.py
Note: This script also does not have a standalone execution function but is used by other scripts.

Measure Runtime of Parallel Async Comprehensions

Run the measure_runtime script to measure how long it takes to execute async_comprehension four times in parallel:

bash
Copy code
python3 2-measure_runtime.py
This script will print the total runtime, which should be approximately 10 seconds.

Explanation of Runtime
The total runtime for the parallel execution of async_comprehension should be close to 10 seconds. This is because each call to async_comprehension takes around 10 seconds (10 yields, each with a 1-second delay). When running four instances in parallel, they execute simultaneously, so the overall runtime is roughly equal to the runtime of a single instance.

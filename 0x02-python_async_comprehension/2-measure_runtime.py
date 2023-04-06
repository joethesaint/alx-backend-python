#!/usr/bin/env python3
"""A measure_runtime coroutine that execute async_comprehension"""

import asyncio
import random
import time
from functools import partial

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four time in parallel using asyncio.gather.
    Aim is to measure the total runtime and return it.
    """
    # https://docs.python.org/3.8/library/functools.html#functools.partial
    """
    #First_trial
    func = partial(async_comprehension)
    start = time.perf_counter()

    await asyncio.gather(func(), func(), func(), func())

    elapsed = time.perf_counter() - start

    return elapsed
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time() - start
    return end

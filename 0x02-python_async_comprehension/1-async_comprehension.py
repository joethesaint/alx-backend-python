#!/usr/bin/env python3

"""
Import async_generator from the previous task and write a
coroutine called async_comprehension that takea no arguments.
"""

import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine collects 10 random numbers using an async
    comprehensing over async_generator, then return the 10
    random numbers
    """
    res = [i async for i in async_generator()]
    return res

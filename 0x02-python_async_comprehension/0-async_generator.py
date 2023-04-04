#!/usr/bin/env python3
"""A coroutine called async_generator and it takes no arguments."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Produce a random number for every iteration"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)

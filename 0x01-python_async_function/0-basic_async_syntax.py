#!/usr/bin/env python3
"""0. The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    async coroutine that takes in an int argument and
    waits for a random delay between 0 and max_delay
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time

#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    An async routine that takes in 2 int arguments and return
    the list of all the delays. The list of the delays should
    be in ascending order.
    """
    time_to_wait = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(time_to_wait)

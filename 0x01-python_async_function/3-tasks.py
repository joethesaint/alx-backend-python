#!/usr/bin/env python3
"""
A regular function(not an async function) that
takes an integer and returns a asyncio.Task
"""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    A function that creates an asynchronous task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))

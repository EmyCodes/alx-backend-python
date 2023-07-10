#!/usr/bin/env python3
import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """an asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random that waits
    for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it."""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def main():
    """Passing the coroutine here"""
    await asyncio.gather(
        wait_random(),
        wait_random(),
        wait_random()
    )

if __name__ == "__main__":
    asyncio.run(main())
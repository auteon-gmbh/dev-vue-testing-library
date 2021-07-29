"""
Async

https://www.python.org/dev/peps/pep-0492/
"""

import asyncio
import httpx
import time
from functools import wraps
from pprint import pprint

URI = 'https://random-data-api.com/api/vehicle/random_vehicle'


def timeit(func):
    @wraps(func)
    async def function_wrapper(*args, **kwargs):
        t0 = time.time()
        res = await func(*args, **kwargs)
        print(f'{time.time() - t0}s')
        return res

    return function_wrapper


@timeit
async def get_vehicle():
    async with httpx.AsyncClient() as client:
        r = await client.get(URI)
        return r.json()


@timeit
async def get_5_vehicles_sync():
    return [await get_vehicle() for i in range(5)]


@timeit
async def gather_5_vehicles():
    reqs = [get_vehicle() for i in range(5)]
    return await asyncio.gather(*reqs)


if __name__ == '__main__':
    t0 = time.time()

    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(get_5_vehicles_sync())
    pprint(results)

    print(f'total_time: {time.time() - t0}s')

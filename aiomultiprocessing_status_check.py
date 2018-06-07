from aiomultiprocess import Pool
import sys
import time
import requests
import asyncio

async def get_statuses(websites):
    status_codes = {}
    async with Pool() as pool:
    	tasks = await pool.map(get_website_status, websites)
    for status in tasks:
        if not status_codes.get(status):
            status_codes[status] = 0
        status_codes[status] += 1
    print(status_codes)


async def get_website_status(url):
    response = requests.get(url)
    return response.status_code


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        websites = f.read().splitlines()
    t0 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_statuses(websites))
    t1 = time.time()
    print("getting website codes took {0:.1f} seconds".format(t1-t0))

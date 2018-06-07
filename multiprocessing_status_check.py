from multiprocessing import Pool
import sys
import time
import requests


def get_statuses( statuses ):
    status_codes = {}
    for status in statuses:
        if not status_codes.get(status):
            status_codes[status] = 0
        status_codes[status] += 1
    print(status_codes)


def get_website_status(url):
    response = requests.get(url)
    return response.status_code

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        websites = f.read().splitlines()
    t0 = time.time()
    p = Pool(5)
    get_statuses(p.map( get_website_status, websites))
    t1 = time.time()
    print("getting website statuses took {0:.1f} seconds".format(t1-t0))
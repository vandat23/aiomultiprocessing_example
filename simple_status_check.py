
import requests
import sys
import time

def website_statuses(websites):
    status_codes = {}
    for website in websites:
        status = requests.get(website).status_code
        if not status_codes.get(status):
            status_codes[status] = 0
        status_codes[status] += 1
    return status_codes

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        websites = f.read().splitlines()
    t0 = time.time()
    print(website_statuses(websites))
    t1 = time.time()
    print("getting status codes took {0:.1f} seconds".format(t1-t0))
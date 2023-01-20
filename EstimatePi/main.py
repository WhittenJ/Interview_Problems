# Estimate pi, given that you have random(0,1)
from datetime import datetime

import random

def estimate_pi(n):
    num_point_circle = 0
    num_point_total = 0

    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)

        distance = x**2 + y**2 # squared
        if distance <= 1:
            num_point_circle += 1
        num_point_total += 1

    return 4 * num_point_circle/num_point_total

def format_results(n):
    d1 = datetime.now()
    result = estimate_pi(n)
    d2 = datetime.now()

    delta = d2 - d1
    seconds = delta.total_seconds()
    print('Pi is roughly %r. %i iterations took %s seconds' % (result, n, seconds))

format_results(10)
format_results(100)
format_results(1000)
format_results(10000)
format_results(100000)
format_results(1000000)
format_results(10000000)
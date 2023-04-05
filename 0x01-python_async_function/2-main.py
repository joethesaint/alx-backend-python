#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 50
max_delay = 9

print(measure_time(n, max_delay))

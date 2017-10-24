#!/usr/bin/python3

from intervaltree import Interval, IntervalTree
from functools import reduce
import sys


file_in = sys.argv[1]
user_out = sys.argv[2]

job_number = 0
machine_number = 0
jobs_order = []
jobs_times = []

input = open(file_in)
# Read input file
first = True
for line in input:
    if first:
        first = False
        job_number = int(line.strip().split(" ")[0])
        machine_number = int(line.strip().split(" ")[1])
    else:
        if len(line.strip().split(" ")) == 2 * machine_number:
            jobs_order.append([])
            jobs_times.append([])
            l = line.strip().split(" ")
            for i in range(0, 2 * machine_number, 2):
                m = int(l[i])
                t = int(l[i+1])
                jobs_order[-1].append(m)
                jobs_times[-1].append(t)
input.close()


machines = [IntervalTree() for _ in range(machine_number)]
result = -1

user = open(user_out)
# Read user output
task = 0
res = 0
prev = 0
for line in user:
    l = line.strip().split(" ")

    if len(l) == 0 or (len(l) == 1 and l[0] == ""):
        continue

    if len(l) != machine_number:
        print("0|Wrong Format")
        exit(0)

    for i in range(machine_number):
        try:
            start_time = int(l[i])
        except:
            print("0|Wrong Format")
            exit(0)

        if i == 0:
            if start_time < 0:
                print("0|Wrong Answer - Wrong time")
                exit(0)

        if i != 0:
            if start_time < prev + jobs_times[task][i-1]:
                print("0|Wrong Answer - Wrong time")
                exit(0)

        prev = start_time

        w = (start_time, start_time + jobs_times[task][i])
        if machines[jobs_order[task][i]].overlaps(w[0], w[1]):
            print("0|Wrong Answer - Overlap")
            exit(0)

        machines[jobs_order[task][i]].add(Interval(w[0], w[1]))
        res = max(res, w[1])

    task += 1

if task != job_number:
    print("0|Wrong Answer")
    exit(0)

user.close()

print("%d|SUCCESS" % res)

#!/usr/bin/python3

from intervaltree import Interval, IntervalTree
from functools import reduce
import sys

class Job:

    def __init__(self, id, start, time, proc):
        self.id = id
        self.start = start
        self.time = time
        self.proc = proc


file_in = sys.argv[1]
user_out = sys.argv[2]

proc_num = 0
job_num = 0
jobs = {}

input = open(file_in)
# Read input file
first = True
for line in input:
    if first:
        first = False
        job_num = int(line.strip().split(" ")[0])
        proc_num = int(line.strip().split(" ")[1])
    else:
        l = line.strip().split(" ")
        id = int(l[0])
        start = int(l[1])
        time = int(l[2])
        proc = int(l[3])
        jobs[id] = Job(id, start, time, proc)
input.close()

jobs_done = [0 for _ in range(job_num+5)]
proc = [IntervalTree() for _ in range(proc_num)]
result = -1

user = open(user_out)
# Read user output
for line in user:
    l = line.strip().split(" ")

    try:
        id = int(l[0])
    except:
        print("0|Wrong Format")
        exit(0)

    if not(id in jobs):
        print("0|Wrong job id")
        exit(0)

    if len(l) != 2 + jobs[id].proc:
        print("0|Wrong format")
        exit(0)

    try:
        start = int(l[1])
    except:
        print("0|Wrong Format")
        exit(0)

    if start < jobs[id].start:
        print("0|Wrong start time")
        exit(0)

    w = (start, start + jobs[id].time)

    req_proc = set()
    for i in range(jobs[id].proc):
        try:
            proc_id = int(l[i+2])
        except:
            print("0|Wrong Format")
            exit(0)

        if not(0 < proc_id <= proc_num):
            print("0|Wrong proc id")
            exit(0)

        proc_id -= 1

        req_proc.add(proc_id)

    if len(req_proc) != jobs[id].proc:
        print("0|Wrong Answer 1")
        exit(0)

    for p in req_proc:
        if proc[p].overlaps(w[0], w[1]):
            print("0|Wrong Answer 2")
            exit(0)

        '''
        for x in proc[p]:
            if max(w[0], x[0]) < min(w[1], x[1]):
                print("0|Wrong Answer 2")
                exit(0)
        '''
    for p in req_proc:
        proc[p].add(Interval(w[0], w[1]))

    result = max(result, w[1])
    jobs_done[id] = 1

user.close()

if reduce(lambda x,y: x+y, jobs_done) != job_num:
    print("0|Wrong Answer 3")
    exit(0)

print("%d|SUCCESS" % result)

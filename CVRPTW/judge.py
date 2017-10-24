#!/usr/bin/python3
import os
import re
import sys, traceback
from math import sqrt


class Depo:
    def __init__(self, line_tab):
        self.id = int(line_tab[0])
        self.x = int(line_tab[1])
        self.y = int(line_tab[2])
        self.q = int(line_tab[3])
        self.t_s = int(line_tab[4])
        self.t_e = int(line_tab[5])
        self.d = int(line_tab[6])
        self.done = False

    def to_string(self):
        return "%d %d %d %d %d %d %d\n" % (self.id, self.x, self.y, self.q, self.t_s, self.t_e, self.d)


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def all_ints(line_tab):
    for i in line_tab:
        if not is_int(i):
            return False
    return True

def read_instance(file_in):
    depos = {}
    f = open(file_in, "r")
    for line in f:
        line = line.strip()
        line_tab = line.split(" ")
        if len(line_tab) == 2:
            M = int(line_tab[0])
            Q = int(line_tab[0])
        elif len(line_tab) == 7:
            d = Depo(line_tab)
            depos[d.id] == d
    f.close()
    return d, M, Q


file_in = sys.argv[1]
user_out = sys.argv[2]

depos, M, Q = read_instance(file_in)

user = open(user_out)
first = True
res = 0.0
for line in user:
    line_tab = line.strip().split(" ")
    if len(line_tab) == 0 or (len(line_tab) == 1 and line_tab[0] == ""):
        continue

    if first:
        if len(line_tab) != 1:
            print("0|Wrong format")
            exit(0)
        if not is_int(line_tab[0]):
            print("0|Wrong Format")
            exit(0)

        route_num = int(line_tab[0])
        first = False
    else:
        if not all_ints(line_tab):
            print("0|Wrong Format")
            exit(0)

        prev = depos[0]
        sum_q = 0
        curr_time = 0.0
        for i in line_tab:
            id = int(i)
            if not (id in depos):
                print("0|Wrong Answer - wrong id")
                exit(0)

            d = depos[id]

            if d.done:
                print("0|Wrong answer - node visited second time")
                exit(0)

            sum_q += d.q
            if sum_q > Q:
                print("0|Wrong answer - Q exceeded")
                exit(0)

            curr_time += sqrt((prev.x - d.x) * (prev.x - d.x) + (prev.y - d.y) * (prev.y - d.y))

            if curr_time > d.t_e:
                print("0|Wrong answer - t_e exceeded")
                exit(0)

            if curr_time < d.t_s:
                curr_time = d.t_s
            curr_time += d.d
            d.done = True
            prev = d

        d = depos[0]
        curr_time += sqrt((prev.x - d.x) * (prev.x - d.x) + (prev.y - d.y) * (prev.y - d.y))
        res += curr_time

for d in depos.values():
    if not d.done:
        print("0|Wrong answer - node not visited")
        exit(0)

print("%f|SUCCESS" % res)

import os
import re
import sys, traceback


class Depo:

    def __init__(self, line_tab):
        self.id = int(line_tab[0])
        self.x = int(line_tab[1])
        self.y = int(line_tab[2])
        self.q = int(line_tab[3])
        self.t_s = int(line_tab[4])
        self.t_e = int(line_tab[5])
        self.d = int(line_tab[6])

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


def parse_file(file_name):
    try:
        f = open(file_name, "r")
        depos = []
        for line in f:
            line = line.strip()
            line = re.sub("\t", " ", line)
            line = re.sub(" +", " ", line)
            line_tab = line.split(" ")

            if len(line_tab) == 2 and is_int(line_tab[0]) and is_int(line_tab[1]):
                V = int(line_tab[0])
                Q = int(line_tab[1])

            if len(line_tab) == 7 and all_ints(line_tab):
                depos.append(Depo(line_tab))

        M = len(depos)

        res = ("%d %d\n" %(M, Q))

        for d in depos:
            if d.id == 0:
                res += d.to_string()
                continue

            if d.q > Q:
                return "Broken file, q > Q", False

            if (depos[0].x - d.x) * (depos[0].x - d.x) + (depos[0].y - d.y) * (depos[0].y - d.y) > d.t_e * d.t_e:
                return "Broken file, t_e too small", False

            res += d.to_string()

        return res, True
    except:
        print('-' * 60)
        traceback.print_exc(file=sys.stdout)
        print('-' * 60)
        return "Exception.", False


dirs = ["S-RC2-1000", "solomon_100", "solomon_25", "solomon_50", "example"]

for name in dirs:
    directory_in_str = "instances/" + name
    directory = os.fsencode(directory_in_str)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        output, status = parse_file(directory_in_str + "/" + filename)
        if status:
            f = open("parsed/" + name + "/" + filename + ".parsed", "w")
            f.write(output)
            f.close()
        else:
            print("File:", filename, "is broken.", output)
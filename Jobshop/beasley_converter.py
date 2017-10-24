import os
import re
import sys, traceback

def parse_file(file_name):
    try:
        f = open("beasley/" + file_name, "r")
        res = ""
        first = True

        for line in f:
            l = line.strip()
            l = re.sub("\t", " ", l)
            l = re.sub(" +", " ", l)
            ll = l.split(" ")

            machines = set()

            if first:
                T = int(ll[0])
                M = int(ll[1])
                if T <= 0 or M <= 0:
                    return "T or M le 0", False
                first = False
                res += ("%d %d\n" % (T, M))
            else:
                if len(ll) == 0 or len(ll) == 1:
                    continue
                if len(ll) != 2*M:
                    return "Not all machines.", False
                for i in range(0, 2*M, 2):
                    m = int(ll[i])
                    t = int(ll[i+1])
                    if m < 0 or m >= M:
                        return "Machine out of range.", False
                    machines.add(m)
                    if t <= 0:
                        return "Time le 0.", False

                if len(machines) != M:
                    return "", False

                res += ("%s\n" % l)

        f.close()
        return res, True
    except:
        print('-' * 60)
        traceback.print_exc(file=sys.stdout)
        print('-' * 60)
        return "Exception.", False


directory_in_str = "beasley"
directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename == "jobshop1.txt":
        continue
    else:
        output, status = parse_file(filename)
        if status:
            f = open("parsed/beasley_" + filename + ".parsed", "w")
            f.write(output)
            f.close()
        else:
            print("File:", filename, "is broken.", output)

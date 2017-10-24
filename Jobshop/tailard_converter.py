import os
import re
import sys, traceback

def parse_file(file_name):
    try:
        f = open("tailard/" + file_name, "r")
        res = ""
        first = True
        times = True

        t = []
        m = []

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
                if len(ll) == 0:
                    continue
                if len(ll) == 1 and ll[0] == "Machines":
                    times = False
                    continue
                if len(ll) == 1:
                    continue

                if len(ll) != M:
                    return "Not all machines.", False

                if times:
                    for i in range(M):
                        tmp_t = int(ll[i])
                        if tmp_t <= 0:
                            return "Time le 0.", False
                    t.append(ll)
                else:
                    for i in range(M):
                        tmp_m = int(ll[i])
                        tmp_m -= 1
                        if tmp_m < 0 or tmp_m >= M:
                            print(tmp_m, M)
                            return "Machine out of range.", False
                        machines.add(tmp_m)
                    if len(machines) != M:
                        return "", False
                    m.append(ll)

        if len(t) != len(m):
            return "Different times and machines", False

        if len(t) != T:
            return "Different number of tasks", False

        for i in range(T):
            tmp = ""
            tmp_bool = True
            for j in range(M):
                if tmp_bool:
                    tmp += ("%d %s" % (int(m[i][j])-1, t[i][j]))
                    tmp_bool = False
                else:
                    tmp += (" %d %s" % (int(m[i][j])-1, t[i][j]))
            res = res + tmp + "\n"

        f.close()
        return res, True
    except:
        print('-' * 60)
        traceback.print_exc(file=sys.stdout)
        print('-' * 60)
        return "Exception.", False


directory_in_str = "tailard"
directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename == "jobshop1.txt":
        continue
    else:
        output, status = parse_file(filename)
        if status:
            f = open("parsed/tailard_" + filename + ".parsed", "w")
            f.write(output)
            f.close()
        else:
            print("File:", filename, "is broken.", output)

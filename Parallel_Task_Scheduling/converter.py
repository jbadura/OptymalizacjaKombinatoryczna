#!/usr/bin/python3
import os
import sys, traceback
import re


def parse_file(file_name, num):
    try:
        file = open(file_name)

        given_job_num = num
        max_jobs = -1
        max_nodes = -1

        jobs_and_nodes_written = False
        jobs_ignored = 0

        res = ""

        for line in file:
            l = line.strip()
            l = re.sub("\t", " ", l)
            l = re.sub(" +", " ", l)
            l = l.split(" ")

            # Read max jobs
            if len(l) > 2 and l[1] == "MaxJobs:":
                max_jobs = int(l[2])
                if given_job_num > max_jobs:
                    return "More jobs requsted than available in input file", False

            # Read max nodes
            if len(l) > 2 and l[1] == "MaxNodes:":
                max_nodes = int(l[2])

            if len(l) == 2 and l[0] == ";MaxNodes:":
                max_nodes = int(l[1])

            # Add max_jobs max_nodes to res
            if not jobs_and_nodes_written and max_jobs != -1 and max_nodes != -1:
                jobs_and_nodes_written = True
                res += ("%d %d\n" % (given_job_num, max_nodes))


            # Error in case job does not have all parameters
            if l[0][0] != ";" and len(l) != 18:
                return "File is broken, abort", False

            #Read job
            if l[0][0] != ";":
                # Error in case max jobs or max nodes did not appear
                if not jobs_and_nodes_written:
                    return "Jobs appeared without information about max jobs and max nodes", False

                id = int(l[0])
                start = 0
                time = 0
                proc = 0

                if int(l[1]) < 0:
                    jobs_ignored += 1
                    continue
                else:
                    start = int(l[1])

                if int(l[3]) <= 0:
                    jobs_ignored += 1
                    continue
                else:
                    time = int(l[3])

                if int(l[4]) <= 0 or int(l[4]) > max_nodes:
                    jobs_ignored += 1
                    continue
                else:
                    proc = int(l[4])

                res += ("%d %d %d %d\n" % (id - jobs_ignored, start, time, proc))

                if id - jobs_ignored == given_job_num:
                    break

        if max_jobs - jobs_ignored < given_job_num:
            return "Too little relevant jobs to meet given number", False

        print("Ignored jobs in", file_name, ":", jobs_ignored)
        file.close()
        return res, True
    except:
        print('-' * 60)
        traceback.print_exc(file=sys.stdout)
        print('-' * 60)
        return "Exception.", False


directory_in_str = "instances"
directory = os.fsencode(directory_in_str)

for i in [500, 2000, 5000, 10000]:
    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        output, status = parse_file("instances/" + filename, i)
        if status:
            f = open("parsed/" + filename + "." + str(i) + ".parsed", "w")
            f.write(output)
            f.close()
        else:
            print("File:", filename, "is broken.", output)

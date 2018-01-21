import os
import sys,time

import calendar 


COLUMN_SEP=""",,"""
FIELD_ID = 0
FIELD_DATE = 1
FIELD_JOBNAME = 2
FIELD_COMMENT = 3


class job_obj:
    def __init__(self, linevalue):
        self.idx = 0
        self.job_name = ""
        self.due_date = None
        self.comments = ""
        self.gid = 'new'
        self.actreq = 'none'
        if linevalue is None:
            return
        name_list = linevalue.strip().split(COLUMN_SEP)
        if len(name_list) < 3:
            return
        self.idx = int(name_list[FIELD_ID])
        self.job_name = name_list[FIELD_JOBNAME].strip()
        self.comments = name_list[FIELD_COMMENT].strip()
        self.datetime = time.strptime(name_list[FIELD_DATE].strip(), "%Y/%m/%d") 

    def show(self, mode=0):
        if mode is 0:
            #print self.idx, time.strftime("%Y/%m/%d", self.datetime), self.job_name, self.comments
            print "[{}] [{}] [{}] [{}]".format(self.idx, time.strftime("%Y/%m/%d", self.datetime),self.job_name, self.comments)
        elif mode is 1:
            print "{},, {},, {},, {}".format(self.idx, time.strftime("%Y/%m/%d", self.datetime),self.job_name, self.comments)

    def write2file(self, filename):
        with open(filename, "a") as f:
            tmp = sys.stdout
            sys.stdout = f
            print " {}, {}, ({}) -> {}".format(time.strftime("%Y/%m/%d", self.datetime),
                self.job_name, self.comments, time.strftime("%Y/%m/%d", time.localtime()))
            f.close()
            sys.stdout = tmp

        return 0


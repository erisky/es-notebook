#!/usr/bin/python

import os
import sys,time
import calendar 

COLUMN_SEP=""",,"""
FIELD_ID = 0
FIELD_DATE = 1
FIELD_JOBNAME = 2
FIELD_COMMENT = 3

my_notes_path = os.getenv("MYNOTE_PATH")
TODO_FILE = my_notes_path + "/" + "todo.txt"

def jdbg(string):
    #print string
    return 0

class job_obj:
    def __init__(self, linevalue):
        self.idx = 0
        self.job_name =""
        self.due_date = None
        self.comments = ""
        name_list = linevalue.strip().split(COLUMN_SEP)
        if len(name_list) < 3:
            return
        self.idx = int(name_list[FIELD_ID])
        self.job_name = name_list[FIELD_JOBNAME]
        self.comments = name_list[FIELD_COMMENT]
        self.datetime = time.strptime(name_list[FIELD_DATE].strip(), "%Y/%m/%d") 
        #print self.idx, self.job_name
#def
#        with open(filename, "r") as f:
#            _data_from_file = f.readlines()
#            f.close()



joblist = {}

#with open("todo.txt") as f:
#    for lines in f :
#        lstrip=lines.strip()
#        if not lstrip.startswith("#") :
#            test1 = job_obj(lstrip)
#            if test1.idx is 0:
#                continue
#            #print test1.job_name
#            joblist[test1.idx] = test1
#    f.close()


def joblist_load(loadfile = TODO_FILE):
    with open(loadfile) as f:
        for lines in f :
            lstrip=lines.strip()
            if not lstrip.startswith("#") :
                test1 = job_obj(lstrip)
                if test1.idx is 0:
                    continue
                #print test1.job_name
                joblist[test1.idx] = test1
        f.close()



def joblist_save():
    print("Are you sure to overwirte the current file? (y/n)")
    yn = raw_input()
    if yn is "Y" or yn is "y":
        print "Saving ..."
    jdbg ("joblist save")

def joblist_add():
    jdbg ("job adding ")
    print "Due Date? "
    test = raw_input()
    print test

def joblist_del(index): 
    jdbg ("job deleting ")
    print int(index)

    if joblist[int(index)]:
        print "YES", joblist[int(index)].job_name
        joblist.pop(int(index))
        joblist_display(7)
        joblist_save()
    else:
        print "No"

def joblist_display(days):
    now = time.time()
    print "####################################################"*2
    print "Today:", time.strftime("%Y/%m/%d", time.gmtime())
    for x in joblist.keys():
        jtime = calendar.timegm(joblist[x].datetime)
        # print "jobtime", jtime
        if (jtime < now + days*24*3600):
            print "#", joblist[x].idx, time.strftime("%Y/%m/%d", joblist[x].datetime), joblist[x].job_name
        #print x,joblist[x].job_name

    print "####################################################"*2
    jdbg ("job display ")


def bad_exit():
    print "Bad arguments"
    exit(-1)

if __name__ == '__main__':
    joblist_load()
    if len(sys.argv) == 1:
        # default display job due in one week
        joblist_display(7)
    else:
        if (sys.argv[1] == 'all'):
            joblist_display(365)
        elif (sys.argv[1] == 'add'):
            joblist_add()
        elif (sys.argv[1] == 'fin'):
            if len(sys.argv) > 2:
                joblist_del(sys.argv[2] )
            else:
                bad_exit

        else: 
            try: 
                joblist_display(int(sys.argv[1]))
            except:
                print "bad params"
                exit(0)

else:
    print __name__





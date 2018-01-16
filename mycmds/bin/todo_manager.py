#!/usr/bin/python

import os
import sys,time
from datetime import datetime
import calendar 
# from colorama import init
# init()

from termcolor import  cprint

print_alert = lambda x: cprint(x, 'red',  attrs=['bold'])
print_notice = lambda x: cprint(x, 'yellow',  attrs=['bold'])



COLUMN_SEP=""",,"""
FIELD_ID = 0
FIELD_DATE = 1
FIELD_JOBNAME = 2
FIELD_COMMENT = 3

my_notes_path = os.getenv("MYNOTE_PATH")
TODO_FILE = my_notes_path + "/" + "todo.txt"

TODO_DONE_FILE = my_notes_path + "/" + "todo_done.txt"


def jdbg(string):
    # print string
    return 0


def get_input():
    try:
        tests = raw_input()
    except KeyboardInterrupt:
        print "QUIT"
        exit(0)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        exit(0)
    return tests


class job_obj:
    def __init__(self, linevalue):
        self.idx = 0
        self.job_name = ""
        self.due_date = None
        self.comments = ""
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


# TODO: Modulize joblist

## joblist = {}


def joblist_new_idx():
    ret = 1
    for x in joblist.keys():
        if ret <= x:
            ret = x+1
    return ret


# with open("todo.txt") as f:
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
    joblist = {}
    with open(loadfile) as f:
        for lines in f:
            lstrip=lines.strip()
            if not lstrip.startswith("#") :
                test1 = job_obj(lstrip)
                if test1.idx is 0:
                    continue
                #print test1.job_name
                joblist[test1.idx] = test1
        f.close()
    return joblist


def joblist_save(joblist, ask = 0):
    if ask == 1:
        print("Are you sure to overwirte the current file? (y/n)")
        yn = get_input()
        if yn is "Y" or yn is "y":
            print "Saving ..."
        else:
            return
    with open(TODO_FILE, "w") as f:
        tmp = sys.stdout
        sys.stdout = f
        joblist.keys().sort()
        for j in joblist.keys():
            joblist[j].show(1)
        f.close()
        sys.stdout = tmp
    jdbg ("joblist save done")


def joblist_add(joblist):
    jdbg("job adding ")
    newjob = job_obj(None)
    now = time.time()
    print "Due Date? (date or days form today): ",
    test = get_input()
    if test == "":
        print "no due, use due today"
        print  time.strftime("%Y/%m/%d", time.localtime())
        jtime  = now
        print jtime
        datenew = time.strptime(time.strftime("%Y/%m/%d", time.localtime()),"%Y/%m/%d" )
    elif test.isdigit():
        days = int (test)
        jtime  = now + days * 24 * 3600
        #datenew = time.strptime(time.strftime("%Y/%m/%d", time.localtime(jtime)),"%Y/%m/%d" )
        datenew = time.localtime(jtime)
    else:
        datenew = time.strptime(test, "%Y/%m/%d")
        jtime = calendar.timegm(datenew)
        if (now > jtime):
            print "can't add a job due in the past"
            return -1

    print "Job name:",
    newjob.job_name = get_input()
    print "Job comment:",
    newjob.comments = get_input()
    newjob.datetime = datenew
    newjob.idx = joblist_new_idx()
    newjob.show()
    print "ok to add ?",
    got=get_input()
    if got is 'y' or got is 'Y':
        print "Add to List:",
        joblist[newjob.idx] = newjob
        ttest = newjob.show()
        joblist_save(joblist, 0)
    # print test,datenew


def joblist_del(joblist, index):
    jdbg ("job deleting ")
    
    if joblist[int(index)]:
        print "Done:", joblist[int(index)].job_name
        deljob = joblist.pop(int(index))
        # joblist_display(7)
        deljob.write2file(TODO_DONE_FILE)
        joblist_save()
    else:
        print "No"


def joblist_display(joblist, days):
    now = time.time()
    print "####################################################"*2
    print "Today:", time.strftime("%Y/%m/%d", time.localtime())
    for x in joblist.keys():
        jtime = calendar.timegm(joblist[x].datetime)
        # print "jobtime", jtime

        if (jtime < now):
            print_alert ("# {} {} {}".format(joblist[x].idx, time.strftime("%Y/%m/%d", joblist[x].datetime), joblist[x].job_name))
        elif (jtime < now + 7*24*3600):
            print_notice("# {} {} {}".format(joblist[x].idx, time.strftime("%Y/%m/%d", joblist[x].datetime), joblist[x].job_name))
        elif (jtime < now + days*24*3600):
            print ("# {} {} {}".format(joblist[x].idx, time.strftime("%Y/%m/%d", joblist[x].datetime), joblist[x].job_name))
            # print "#", joblist[x].idx, time.strftime("%Y/%m/%d", joblist[x].datetime), joblist[x].job_name
        #print x,joblist[x].job_name

    print "####################################################"*2
    jdbg("job display ")


def joblist_edit(index):
    if joblist[int(index)]:
        print "Editing job:", joblist[int(index)].job_name
        editjob = joblist[(int(index))]
        print 'new due:',
        duestr = get_input()
        if duestr == "":
            print "Due day not changed"
        else:
            datenew = time.strptime(duestr, "%Y/%m/%d")
            editjob.datetime = datenew

        print "Input the job name:",
        new_jobname = get_input()
        if new_jobname != "":
            editjob.job_name = new_jobname
        else:
            print "not chaged"
        print "Input the job comment:",
        new_cmmt = get_input()
        if new_cmmt != "":
            editjob.comments = new_cmmt
        else:
            print "not chaged"
        joblist_save(joblist)
    else:
        print "No job is found"

    return 0



def bad_exit():
    print_alert("Bad arguments:{}".format(123))
    exit(-1)


def todo_help():
    print """
    todo add
        - interactive job adding
    todo fin {id}
        - finish a job by id
    """


if __name__ == '__main__':
    joblist = joblist_load()
    if len(sys.argv) == 1:
        # default display job due in one week
        joblist_display(joblist, 31)
    else:
        if (sys.argv[1] == 'all'):
            joblist_display(joblist,365)
        elif (sys.argv[1] == 'add'):
            joblist_add(joblist)
            joblist_display(joblist, 31)
        elif (sys.argv[1] == 'fin') or (sys.argv[1] == 'del'):
            if len(sys.argv) > 2:
                joblist_del(joblist, sys.argv[2])
            else:
                bad_exit()
        elif sys.argv[1] == 'done':
            os.system('cat '+ TODO_DONE_FILE)
        elif sys.argv[1] == 'edit':
            if len(sys.argv) > 2:
                joblist_edit(joblist, sys.argv[2])
            else:
                bad_exit()

        elif sys.argv[1] == '-h':
            todo_help()
        else: 
            try: 
                joblist_display(joblist, int(sys.argv[1]))
            except:
                bad_exit()

else:
    print __name__





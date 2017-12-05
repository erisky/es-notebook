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
        if linevalue is None:
            return
        name_list = linevalue.strip().split(COLUMN_SEP)
        if len(name_list) < 3:
            return
        self.idx = int(name_list[FIELD_ID])
        self.job_name = name_list[FIELD_JOBNAME].strip()
        self.comments = name_list[FIELD_COMMENT].strip()
        self.datetime = time.strptime(name_list[FIELD_DATE].strip(), "%Y/%m/%d") 
        #print self.idx, self.job_name
#def
#        with open(filename, "r") as f:
#            _data_from_file = f.readlines()
#            f.close()

    def show(self, mode=0):
        if mode is 0:
            #print self.idx, time.strftime("%Y/%m/%d", self.datetime), self.job_name, self.comments
            print "[{}] [{}] [{}] [{}]".format(self.idx, time.strftime("%Y/%m/%d", self.datetime),self.job_name, self.comments)
        elif mode is 1:
            print "{},, {},, {},, {}".format(self.idx, time.strftime("%Y/%m/%d", self.datetime),self.job_name, self.comments)

joblist = {}


def joblist_new_idx():
    ret = 0
    for x in joblist.keys():
        if ret <= x:
            ret = x+1
    return ret


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
        for lines in f:
            lstrip=lines.strip()
            if not lstrip.startswith("#") :
                test1 = job_obj(lstrip)
                if test1.idx is 0:
                    continue
                #print test1.job_name
                joblist[test1.idx] = test1
        f.close()



def joblist_save(ask = 0):
    if ask == 1:
        print("Are you sure to overwirte the current file? (y/n)")
        yn = raw_input()
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


def joblist_add():
    jdbg("job adding ")
    newjob = job_obj(None)
    now = time.time()
    print "Due Date? ",
    test = raw_input()
    datenew = time.strptime(test, "%Y/%m/%d")
    jtime = calendar.timegm(datenew)
    if (now > jtime):
        print "can't add a job due in the past"
        return -1

    print "Job name:",
    newjob.job_name = raw_input()
    print "Job comment:",
    newjob.comments = raw_input()
    newjob.datetime = datenew
    newjob.idx = joblist_new_idx()
    newjob.show()
    print "ok to add ?",
    got=raw_input()
    if got is 'y' or got is 'Y':
        print "Add to List"
        joblist[newjob.idx] = newjob
        ttest = newjob.show()
        print "haha", ttest
        joblist_save(0)
    #print test,datenew


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





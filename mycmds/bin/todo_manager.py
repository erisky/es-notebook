#!/usr/bin/python

import os
import sys,time
from datetime import datetime
import calendar 
#import joblist
from joblist import joblist_load,joblist_save, joblist_new_idx, joblist_add, joblist_del, joblist_edit

# from colorama import init
# init()

from termcolor import  cprint

print_alert = lambda x: cprint(x, 'red',  attrs=['bold'])
print_notice = lambda x: cprint(x, 'yellow',  attrs=['bold'])


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




def jdbg(string):
    # print string
    return 0

# TODO: Modulize joblist

## joblist = {}

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





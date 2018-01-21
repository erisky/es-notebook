import os
import calendar
import time, sys
from job_obj import job_obj
import quick_task_list as ggtl 
my_notes_path = os.getenv("MYNOTE_PATH")

TODO_DONE_FILE = my_notes_path + "/" + "todo_done.txt"

TODO_FILE = my_notes_path + "/" + "todo.txt"

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


def joblist_new_idx(joblist):
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


def joblist_load_txt(loadfile):
    joblist = {}
    with open(loadfile) as f:
        for lines in f:
            lstrip = lines.strip()
            if not lstrip.startswith("#"):
                test1 = job_obj(lstrip)
                if test1.idx is 0:
                    continue
                # print test1.job_name
                joblist[test1.idx] = test1
        f.close()
    return joblist


def joblist_load_google(showDone = False):
    joblist = {}
    tasks = ggtl.load_all_task(showDone=showDone)
    tasks.sort()
    ji = 0
    for ti in tasks:
        if 'jobname' in ti.keys():
            newj = job_obj(None)
        else:
            continue

        newj.idx = ji
        newj.gid = ti['id']
        ji += 1
        newj.job_name = ti['jobname']

        if 'description' in ti.keys():
            newj.comments = ti['description']
        newj.datetime = time.strptime(ti['date'][0:10], "%Y-%m-%d")

        joblist[newj.idx] = newj

    #print joblist
    return joblist


def joblist_sync_google(joblist):
    itemlist = []
    for x in joblist.keys():
        job = joblist[x]
        newitem = {}
        newitem['jobname'] = job.job_name
        newitem['id'] = job.gid
        newitem['description'] = job.comments
        newitem['date'] = time.strftime("%Y-%m-%dT00:00:00.000Z", job.datetime)
        newitem['actreq'] = job.actreq
        itemlist.append(newitem)
    ggtl.sync_to_tasklist(itemlist)
    return


def joblist_load(loadfile = TODO_FILE):
    joblist = joblist_load_google()
    if joblist is None:
        joblist = joblist_load_txt(loadfile)
    return joblist

def joblist_load_done():
    joblist = joblist_load_google(showDone = True)
    print("done len:{}".format(len(joblist)))
    return joblist



def joblist_save(joblist, ask = 0):
    if ask == 1:
        print("Are you sure to overwirte the current file? (y/n)")
        yn = get_input()
        if yn is "Y" or yn is "y":
            print "Saving ..."
        else:
            return

    joblist = joblist_sync_google(joblist)
#    with open(TODO_FILE, "w") as f:
#        tmp = sys.stdout
#        sys.stdout = f
#        joblist.keys().sort()
#        for j in joblist.keys():
#            joblist[j].show(1)
#        f.close()
#        sys.stdout = tmp


def joblist_add(joblist):
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
    newjob.idx = joblist_new_idx(joblist)
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
    
    if joblist[int(index)]:
        print "Done:", joblist[int(index)].job_name
        joblist[int(index)].actreq = 'del'
        #deljob = joblist.pop(int(index))
        #deljob.write2file(TODO_DONE_FILE)
        joblist_save(joblist)
    else:
        print "No"


def joblist_edit(joblist, index):
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
        editjob.actreq = 'edit'
        joblist_save(joblist)
    else:
        print "No job is found"

    return 0


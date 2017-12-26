#!/usr/bin/python

###########################################################################
# Tool:
#    dirc - create folder for project / annaully folder
# Usage:
#    dirc project [name]
#       - create folder in assigned folder or directly in esnote path
#
#    dirc commpany [name]
#       - create folder for commpany specific folder 
#
###########################################################################

import os
import sys,time
from datetime import datetime
import calendar 
# from colorama import init
# init()

from termcolor import  cprint

print_alert = lambda x: cprint(x, 'red',  attrs=['bold'])
print_notice = lambda x: cprint(x, 'yellow',  attrs=['bold'])


esnote_root = os.getenv("ESNOTE_ROOT")
note_path = os.getenv("MYNOTE_PATH")


TEMPLATE=os.path.join(esnote_root, "annual_template.tgz")


def dirc_create_project(name):
    print "Mode: 1> directly in esnote or 2> softlink: ",
    mode = raw_input()
    if mode == '2':
        print "Directory to locate: ",
        prj_path = raw_input()
        # print prj_path
        prj_path = os.path.expanduser(prj_path)
        if not os.access(prj_path, os.F_OK) or not os.path.isdir(prj_path):
            print "please input correct directory name"
            exit ()
        
        print "create folder {} in {} ? ".format(name, prj_path)
        yn = raw_input()
        if yn != 'y':
            exit (0)
        os.system("tar zxvf "+ TEMPLATE + " -C /tmp/")
        os.system("mkdir -p "+ prj_path + "/" + name)
        os.system("cp -rf /tmp/annual_template/projects/sample_project/* " + prj_path +"/"+ name)
        os.system("ln -s " + prj_path + "/" + name + " " + note_path + "/projects" )
        
    elif mode == '1':
        print_notice("Do not put confidential data to git hub!!")
        os.system("tar zxvf " + TEMPLATE + " -C /tmp/")
        os.system("mkdir -p "+ note_path + "/projects/" + name)
        os.system("cp -rf /tmp/annual_template/projects/sample_project/* " + note_path + "/projects/" + name)


def dirc_create_company(name):
    print "Directory to locate: ",
    prj_path = raw_input()
    # print prj_path
    prj_path = os.path.expanduser(prj_path)
    if not os.access(prj_path, os.F_OK) or not os.path.isdir(prj_path):
        print "please input correct directory name"
        exit ()
    
    print "create folder {} in {} ? ".format(name, prj_path)
    yn = raw_input()
    if yn != 'y':
        exit (0)
    os.system("tar zxvf " + TEMPLATE + " -C /tmp/")
    os.system("mkdir -p "+ prj_path + "/" + name)
    os.system("cp -rf /tmp/annual_template/company/* " + prj_path +"/"+ name)
    os.system("ln -s " + prj_path + "/" + name + " " + note_path )



def usage():
    print "dirc project/company [name] or "
    print "dirc info - show the dirc readme"
    exit()

if __name__ == '__main__':

    if len(sys.argv) == 2 and sys.argv[1] == 'info':
        os.system('cat '+ esnote_root + '/' + 'annual_template/readme.txt')
        exit(0)
    if len(sys.argv) < 3:
        usage()
    

    elif sys.argv[1] == 'project':
        dirc_create_project(sys.argv[2])
    elif sys.argv[1] == 'company':
        dirc_create_company(sys.argv[2])
    
exit(0)


'''COLUMN_SEP=""",,"""
FIELD_ID = 0
FIELD_DATE = 1
FIELD_JOBNAME = 2
FIELD_COMMENT = 3

TODO_FILE = my_notes_path + "/" + "todo.txt"

TODO_DONE_FILE = my_notes_path + "/" + "todo_done.txt"


def jdbg(string):
    # print string
    return 0


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

joblist = {}


def joblist_new_idx():
    ret = 0
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
    if test == "":
        print "no due, use due today"
        print  time.strftime("%Y/%m/%d", time.localtime())
        jtime  = now
        datenew = time.strptime(time.strftime("%Y/%m/%d", time.localtime()),"%Y/%m/%d" )
    else:
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
        print "Add to List:",
        joblist[newjob.idx] = newjob
        ttest = newjob.show()
        joblist_save(0)
    # print test,datenew


def joblist_del(index):
    jdbg ("job deleting ")
    
    if joblist[int(index)]:
        print "Done:", joblist[int(index)].job_name
        deljob = joblist.pop(int(index))
        # joblist_display(7)
        deljob.write2file(TODO_DONE_FILE)
        joblist_save()
    else:
        print "No"


def joblist_display(days):
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
        duestr = raw_input()
        if duestr == "":
            print "Due day not changed"
        else:
            datenew = time.strptime(duestr, "%Y/%m/%d")
            editjob.datetime = datenew

        print "Input the job name:",
        new_jobname = raw_input()
        if new_jobname != "":
            editjob.job_name = new_jobname
        else:
            print "not chaged"
        print "Input the job comment:",
        new_cmmt = raw_input()
        if new_cmmt != "":
            editjob.comments = new_cmmt
        else:
            print "not chaged"
        joblist_save()
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




    joblist_load()
    if len(sys.argv) == 1:
        # default display job due in one week
        joblist_display(31)
    else:
        if (sys.argv[1] == 'all'):
            joblist_display(365)
        elif (sys.argv[1] == 'add'):
            joblist_add()
            joblist_display(31)
        elif (sys.argv[1] == 'fin') or (sys.argv[1] == 'del'):
            if len(sys.argv) > 2:
                joblist_del(sys.argv[2])
            else:
                bad_exit()
        elif sys.argv[1] == 'done':
            os.system('cat '+ TODO_DONE_FILE)
        elif sys.argv[1] == 'edit':
            if len(sys.argv) > 2:
                joblist_edit(sys.argv[2])
            else:
                bad_exit()

        elif sys.argv[1] == '-h':
            todo_help()
        else: 
            try: 
                joblist_display(int(sys.argv[1]))
            except:
                bad_exit()

else:
    print __name__



'''


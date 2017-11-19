#!/usr/bin/env python

import os,time
import sys

'''use the sublime as editor '''
editor_exec = "gedit"
#my_notes_path = """/home/eric/work/note/es-notebook/2017"""
my_notes_path=os.getenv("MYNOTE_PATH")

if not os.path.isdir(my_notes_path):
    print "$MYNOTE_PATH is not set correctly:", my_notes_path
    exit (0)


# get the path of the notes
def list_my_note():
    notepath = os.listdir(my_notes_path)
    notepath.sort()
    for i in xrange(len(notepath)):
        print "{}. {}".format(i+1, notepath[i])

    try:
        x = int(raw_input("File to show:"))
    except:
        return None
    if x <= len(notepath):
        print "input: {}".format(notepath[x-1])
        return my_notes_path +'/'+ notepath[x-1]
    else:
        return None


def run_edit(pathname):
    # if the targt file is a directoy, use vim to list the files
    print "{}".format(pathname)
    if os.path.isdir(pathname):
        cmdexec = "vim" + " " + pathname
        os.system(cmdexec)
    if os.path.isfile(pathname):
        cmdexec = editor_exec + " " + pathname
        os.system(cmdexec)






if len(sys.argv) == 2:
    notefile = my_notes_path + '/' + sys.argv[1]

    if sys.argv[1] == "path":
        os.chdir(my_notes_path)
        os.system("bash")
        exit()
    
    run_edit(notefile)
#    notefile = my_notes_path + '/' + sys.argv[1]
#    # if the targt file is a directoy, use vim to list the files
#    if os.path.isdir(notefile):
#        cmdexec = "vim" + " " + notefile
#        os.system(cmdexec)
#    if os.path.isfile(notefile):
#        cmdexec = editor_exec + " " + notefile
#        os.system(cmdexec)

    exit()

filepath = list_my_note()
if filepath is not None:
    run_edit(filepath)
#    cmdexec = editor_exec + " " + filepath
#    os.system(cmdexec)


#os.system("subl 123")

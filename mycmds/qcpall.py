#!/usr/bin/python

import os
import sys
import subprocess
GIT_CM="git"


#gcmd=GIT_CM+" "+"status"




def get_qualcomm_sdk_path():
    mypath=os.getcwd()
    pos = mypath.rfind("qualcomm_sdk")
    if pos != -1:
        return mypath[:pos+1+len("qualcom_sdk")]
    else:
        if os.path.isdir(mypath+"/"+"qualcomm_sdk"):
           return mypath+"/"+"qualcomm_sdk" 
        else: 
            return None



def relocate_files(filepath):
    topdirs = ["qsdk", "BOOT.BF.3.1.1", "meta-scripts", "IPQ4019.ILQ.5.0"]
    qualcomm_sdk_dir=get_qualcomm_sdk_path()
    targetpath = ""
    pos = 0
    for topdir in topdirs:
        pos = filepath.find(topdir)
        if pos != -1:
            targetpath = qualcomm_sdk_dir+"/"+ filepath[pos:]
            #print filepath, "-->", targetpath
            ret = subprocess.call(["cp", filepath, targetpath])
            print "ret",ret
            return 1
    print "Need Manaully Copy:", filepath
    return 0

try:

    status_raw=subprocess.check_output(["git", "status"])
    lines=status_raw.split("\n")
    line=""
except :
        print "not a git repo"

filecopied = 0
totalnum = 0
for line in lines:
    if line.strip().startswith("modified"):
        filepath=line.replace("modified:","").strip()
        filecopied+=relocate_files(filepath)
        totalnum+=1

print "Total num:", totalnum, "File copied:", filecopied
#print "qualcomm path:", get_qualcomm_sdk_path()


#os.system(gcmd)


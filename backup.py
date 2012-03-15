#!/usr/bin/python
'''
A simple script to handle GIT in daemon mode
'''

import os,time
from subprocess import Popen, PIPE

# function to handle newly untracked files
def gitUntracked():
    commit_msg='added'          # commit message, if require in case
    # list all untracked files
    untracked = Popen('git ls-files . --exclude-standard --others',shell=True, stdout=PIPE).stdout.readlines() 
    # go through every file and add
    for untrackedfile in untracked:
        gitAdd(untrackedfile,commit_msg)

# function to handle modification made to file(s)
def gitModified():
    commit_msg='modified'
    modified = Popen('git ls-files --modified',shell=True, stdout=PIPE).stdout.readlines()
    for modifiedfile in modified:
        gitAdd(modifiedfile,commit_msg)

# function to handle deleted file(s)
def gitDelete():
    commit_msg='deleted'
    deleted = Popen('git ls-files --deleted',shell=True, stdout=PIPE).stdout.readlines()
    for deletedfile in deleted:
        gitdelete='git rm ' + deletedfile
        os.system(gitdelete)

# function to show cached file(s)
def gitCached():
    cached = Popen('git ls-files --cached',shell=True, stdout=PIPE).stdout.readlines()
    for cachedfile in cached:
        print cachedfile

# function to add changes
def gitAdd(x,msg):
    #print msg
    gitadd = 'git add ' + x
    os.system(gitadd)

# commit changes
def gitCommit():
    #print "In function gitCommit " + msg
    myWeek = time.strftime("%a")
    myDate = time.strftime("%d-%B-%Y")
    myTime = time.strftime("%H-%M-%S")
    timeStamp='Commit on: ' + myWeek + ' ' + myDate + ' ' + myTime
    gitcommit='git commit -m ' + "'" + timeStamp + ' ' +  "'" 
    os.system(gitcommit)

# check if git is initiated, if not initiate it
def gitstart():
    # if not os.path.exists('.git'):
    if not os.path.isdir('.git'):
        print "No .git/ dir"
        os.system('git init')       
    else:
        #print ".git/ dir exist"

        # call functions
        gitUntracked()
        gitModified()
        gitDelete()
        gitCommit()


# go through inifinite loop, but wait for 15 sec before scanning any changes
while True:
    gitstart() 
    time.sleep(15)



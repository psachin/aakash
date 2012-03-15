#!/usr/bin/python

import os,time

from subprocess import Popen, PIPE
#eachfile = ''

def gitUntracked():
    commit_msg='added'
    untracked = Popen('git ls-files . --exclude-standard --others',shell=True, stdout=PIPE).stdout.readlines()
    for untrackedfile in untracked:
        gitAdd(untrackedfile,commit_msg)

def gitModified():
    commit_msg='modified'
    modified = Popen('git ls-files --modified',shell=True, stdout=PIPE).stdout.readlines()
    for modifiedfile in modified:
        gitAdd(modifiedfile,commit_msg)

def gitDelete():
    commit_msg='deleted'
    deleted = Popen('git ls-files --deleted',shell=True, stdout=PIPE).stdout.readlines()
    for deletedfile in deleted:
        gitdelete='git rm ' + deletedfile
        os.system(gitdelete)
        gitCommit(commit_msg)

def gitCached():
    cached = Popen('git ls-files --cached',shell=True, stdout=PIPE).stdout.readlines()
    for cachedfile in cached:
        print cachedfile

def gitAdd(x,msg):
    print msg
    gitadd = 'git add ' + x
    os.system(gitadd)
    gitCommit(msg)

def gitCommit(msg):
    #print "In function gitCommit " + msg
    myWeek = time.strftime("%a")
    myDate = time.strftime("%d-%B-%Y")
    myTime = time.strftime("%H-%M-%S")
    timeStamp='Commit on: ' + myWeek + ' ' + myDate + ' ' + myTime
    gitcommit='git commit -m ' + "'" + timeStamp + ' ' + '\nAction: ' + msg + "'" 
    os.system(gitcommit)
    
def gitstart():
    # if not os.path.exists('.git'):
    if not os.path.isdir('.git'):
        print "No .git/ dir"
        os.system('git init')       
    else:
        #print ".git/ dir exist"
        gitUntracked()
        gitModified()
        gitDelete()
        # gitCached()

        
while True:
    gitstart() 
    time.sleep(5)


#gitUntracked()
#gitCached()

'''
def sample():
    URL='www.google.com'
    callfunction(URL)

def callfunction(x):
    print x

sample()

'''


#print bashout[1]
            



    # captures git status from stdout, 'if' statement checks line2 from 
    # stdout with standard commit message


'''

if not bashout[1].strip() == 'nothing to commit (working directory clean)':
        userDeleted = Popen('git ls-files --deleted',shell=True, stdout=PIPE).stdout.readlines()
        for i in userDeleted:                                #for more than one deleted files                   
            eachfile = i.strip()
            rm = 'git rm ' + eachfile                        #adding all deleted files to staging area
            os.system(rm)             
        os.system('git add .')                               #adding all new files 
        commit = 'git commit -am ' + "'" + eachfile + "'"    #adding modified files
        os.system(commit)
        time.sleep(5)                                        #delay in seconds
    
else:    
    os.system('git add .')
    os.system("git commit -am 'added all files'")

'''

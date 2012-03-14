#!/usr/bin/bash +x

# read -p "Enter source name: " SRC
# echo $SRC


function gitadd() {
    git add .
}

function gitcommit() {
    git commit -m "initial commit"
}

function untracked() {

    # GIT_STATUS=$(git st | grep -i "Untracked files:" | cut -d " " -f 1)
#     echo $GIT_STATUS 
#     DATE=$(date +%d-%m-%Y-%T)
#     if [ ! -e $GIT_STATUS ];
#     then
# 	echo "there are Untracked files"
# 	git add .
# 	git commit -m 'added \"$DATE\"'
#     else    
# 	echo "NO Untracked files"
#     fi
    
    git ls-files --others
}

function gitrm() {

    DATE=$(date +%d-%m-%Y-%T)

    FILES=$(git ls-files --deleted)
    git rm $(git ls-files --deleted)
    git commit -m \"Deleted: $FILES $DATE\"
}

function gitmodified() {

    DATE=$(date +%d-%m-%Y-%T)

    FILES=$(git ls-files --modified)
    git add $(git ls-files --modified)
    git commit -m \"Modified: $FILES $DATE\"
}

function check-git() {

    if [ -d .git ];
    then
	echo -e ".git exist"
	untracked
	#gitmodified
    else
	echo -e ".git not exist "
	echo "demo.sh" > .gitignore
	git init
	gitadd
	gitcommit
    fi

}

check-git



# TODO
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#       modified:   sample
#
# no changes added to commit (use "git add" and/or "git commit -a")

# handling add and modified files together












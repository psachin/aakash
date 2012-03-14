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

    GIT_STATUS=$(git st | grep -i "Untracked files:" | cut -d " " -f 1)
    echo $GIT_STATUS 
    DATE=$(date +%d-%m-%Y-%T)
    if [ ! -e $GIT_STATUS ];
    then
	echo "there are Untracked files"
	git add .
	git commit -m \"$DATE\"
    else    
	echo "NO Untracked files"
    fi

}

function check-git() {

    if [ -d .git ];
    then
	echo -e ".git exist"
	untracked
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










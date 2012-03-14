#!/usr/bin/bash +x

# read -p "Enter source name: " SRC
echo $SRC


function gitadd() {
    git add .
}

function gitcommit() {
    git commit -m "initial commit"
}

function check-git() {

    if [ -d .git ];
    then
	echo -e ".git exist"
	gitadd
	gitcommit
    else
	echo -e ".git not exist "
	echo "demo.sh" > .gitignore
	git init
	gitadd
	gitcommit
    fi

}

#check-git

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







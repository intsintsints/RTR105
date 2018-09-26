#!/bin/bash
if [ $# == 1 ]
then
git config --global user.email teslak70@gmail.com
git add .
#git commit - m "20180926_13_50"
git commit -m $1
git push origin master
fi



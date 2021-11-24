#!/bin/bash
FILE=""
DIR="/home/rcunha/workspace/spyrk-cluster/test"
# init
# look for empty dira
if [ -d "$DIR" ]
then
	if [ "$(ls -A $DIR)" ]; then
     echo "Take action $DIR is not Empty"
	else
    echo "$DIR is Empty"
	fi
else
	echo "Directory $DIR not found."
fi

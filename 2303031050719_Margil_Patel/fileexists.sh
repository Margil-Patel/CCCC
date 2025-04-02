#!/bin/bash
echo "to check weather file exists or not"
if [ -f pattern.sh ]
then
	echo "File exists"
else
	echo "File does not exist"
fi

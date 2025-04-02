#!/bin/bash
h=$(date +"%H")
if [ $h -gt 6 -a $h -lt 12 ]
then
	echo good morning
elif [ $h -gt 12 -a $h -lt 16 ]
then
	echo good afternoon
elif [ $h -gt 16 -a $h -lt 20 ]
then
	echo good evening
else
	echo night
fi

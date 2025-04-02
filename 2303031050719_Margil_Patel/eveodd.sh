#!/bin/bash
read a
mod=$((a % 2))
if [ $mod -eq 0 ]
then
	echo even
else
	echo odd
fi

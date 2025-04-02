#!/bin/bash
read dd
read mm
read yy
if [ $dd -ge 1 ] && [ $dd -le 31 ] && [ $mm -ge 1 ] && [ $mm -le 12 ] && [ $yy -ge 1 ] && [ $yy -le 2025 ]
then
	echo true
else
	echo false
fi

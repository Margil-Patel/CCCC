#!/bin/bash
echo enter
read num
sd=0
sum=0
while [ $num -gt 0 ]
do
	sd=$((num % 10))
	num=$((num / 10))
	sum=$((sum + $sd))
done
echo $sum

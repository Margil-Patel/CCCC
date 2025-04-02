#!/bin/bash

echo "Give the limit upto which even number should be print"
read limit


echo "Even numbers up to $limit:"

for ((i=2; i<=limit; i+=2))
do
  echo "$i"
done

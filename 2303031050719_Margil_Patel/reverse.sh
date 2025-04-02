#!/bin/bash
read string

reverse=""

len=${#string}

for(( i=$len-1; i>=0; i-- ));do
	reverse=$reverse${string:$i:1}
done

if [ "$string" == "$reverse" ]
then
	echo true
else
	echo false
fi

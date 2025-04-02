!/bin/bash
echo margil patel
h=$(date +"%H")
echo Enter your username
read a
echo Enter your password
read b
if(( $a == "margil" && $b == "1234" ))
then
if [ $h -gt 6 -a $h -le 12 ]
then
echo good morning

elif [ $h -gt 12 -a $h -le 16 ]
then
echo good afternoon

elif [ $h -gt 16 -a -le 20 ]
then
echo good evening

else
echo good night

fi
else
echo Wrong password
fi

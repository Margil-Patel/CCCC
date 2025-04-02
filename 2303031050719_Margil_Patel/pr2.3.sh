#!bin/bash
read a
read b
a= $(( $a + $b ))
b = $(( $a - $b ))
a = $(( $a - $b ))

echo $a
echo $b

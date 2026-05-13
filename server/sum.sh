#!/bin/bash
sum=0
for k in $*
do
   sum=$(($sum + $k))
done
echo $sum

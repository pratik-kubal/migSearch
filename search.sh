#!/bin/bash
echo "---Local Search Module---"
sleep 2
echo
echo
echo "Finding"
sleep 3
find /home -name "$1">search.log
LOG="search.log" 
if [ -s ${LOG} ] ; then
	echo " "
	echo "$1 Found"
else
	echo " "
	echo "$1 Not Found"
fi
exit

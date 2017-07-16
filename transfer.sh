#!/bin/bash
echo "---Migrating---"
sleep 3
scp search.sh lillian@192.168.43.29:/home/lillian/Desktop/mig
SCRIPT="./Desktop/mig/search.sh $1 "
ssh -l lillian 192.168.43.29 "${SCRIPT}"
exit

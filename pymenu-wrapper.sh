#!/bin/bash

if [ "$#" -lt 1 ]; then
  echo "Missing menu file!"
  exit -1
fi
MENU_FILE=$1

commands=()
while read line; do
  # commands+=("$line")
  cmd=`echo $line | awk -F'> > >' '{print $2}'`
  commands+=("$cmd")
done < $MENU_FILE

MENU_FILE=$MENU_FILE pymenu-run.sh
result_index=$?

if [ "$result_index" -ne -1 ]; then
  ${commands[$result_index]}
fi

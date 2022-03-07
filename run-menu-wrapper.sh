#!/bin/bash

if [ $# < 1 ]; then
  echo "Missing menu file!"
  exit -1
fi
MENU_FILE=$1

options=()
while read line; do
  options+=("$line")
done < $MENU_FILE

MENU_FILE=$MENU_FILE ./run-menu.sh
result_index=$?

${options[$result_index]}

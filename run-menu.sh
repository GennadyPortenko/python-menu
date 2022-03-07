#!/bin/bash

if [[ -z "${MENU_FILE}" ]]; then  # if TOPIC undefined
  echo "Menu file undefined!"
  exit
fi

delimiter=':::'
options=()
while read line; do
  options+=("$line")
  opts+=$line$delimiter
done < $MENU_FILE

# echo "${options[@]}"
# opts="${options[@]}"

python3 main.py --logging-port 1299 --items "${opts}" --delimiter $delimiter

#python3 main.py --logging-port 1299 --items "[\
#  Element('Option 1'), \
#  Element('Option 2'), \
#]"

result_index=$?
#echo res index: $result_index
#echo res: ${options[$result_index]}
exit $result_index

#!/bin/bash

options=('Option 1;' 'Option 2;')

opts="${options[@]}"

python3 main.py --logging-port 1299 --items "${opts}"

#python3 main.py --logging-port 1299 --items "[\
#  Element('Option 1'), \
#  Element('Option 2'), \
#]"

echo res index: $?
echo res: ${options[$?]}
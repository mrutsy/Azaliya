#!/bin/bash

: '
Test
'


check_venv(){
  echo "Checking VENV..."
  if [ -d venv ];
    then
      echo "VENV - OK!"
      python3 -m pip install --user --upgrade pip
    else
      echo "Don't found VENV. Create VENV."
      python3 -m venv venv
      check_venv
  fi
}


check_venv

#exec python -m pip install --upgrade pip
#
#source venv/bin/activate
#python main.py
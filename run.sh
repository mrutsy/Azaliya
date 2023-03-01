#!/bin/bash

: '
Test
'


check_venv(){
  echo "Checking VENV..."
  if [ -d venv ];
    then
      echo "VENV - OK!"
      source venv/bin/activate
      python -m ensurepip --upgrade
      pip --version
      pip install -r /opt/Azaliya/modules.txt
      python /opt/Azaliya/main.py
    else
      echo "Don't found VENV. Create VENV."
      python -m venv venv
      check_venv
  fi
}


check_venv

#exec python -m pip install --upgrade pip
#
#source venv/bin/activate
#python main.py

import sys
import os

import subprocess

def main():
    path = r'config.txt'
    with open(path, 'r') as reader:
        directory = reader.readline().split(':')[1].strip()
        backup = reader.readline().split(':')[1].strip()
        user = reader.readline().split(':')[1].strip()
    os.system('##!/bin/bash \n cp -R '+directory+' '+backup + '\n'+
              'inotifywait -r -m '+directory+' -e modify --exclude "swp" | while read path '
              'action file;do \n echo "${file}" > recuento.txt\n python3 Watcher3.py "${file}" \n done ')






if __name__ == '__main__':
    main()

#!/bin/bash
sudo ln -s $(readlink -f mikara.py) ${PATH%%:*}/mikara

#!/usr/bin/env python

import os

files = os.listdir('.')
target = open('filename.txt', 'w')
for f in files:
    target.write(f)
    target.write('\n')

target.close()
#!/usr/bin/env python


import os
import sys

print 'environ:', os.environ['BRANCH']
print 'getenv:', os.getenv('BRANCH')


for k, v in os.environ.items():
    print k, v

#!/usr/bin/env python
import random, sys

if len(sys.argv) < 3:
  print 'Usage: python %s input output' % sys.argv[0]
   sys.exit(-1)

input, output = sys.argv[1], sys.argv[2]

itemList = open(input).readlines()
random.shuffle(itemList)
fd = open(output, 'w+')
for item in itemList:
  fd.write('%s' % item)
fd.close()

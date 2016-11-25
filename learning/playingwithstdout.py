#!/usr/bin/env python
from sys import stdout
import time

a = '-'
b = '\\'
c = '|'
d = '/'
e = 'WORKING'
f = 'FINISHING'
duration = .1
loop_count = 0


def workOut():
    stdout.write('\r%s %s %s' % (a, e, a))
    time.sleep(duration)
    
    stdout.write('\r%s %s %s' % (b, e, b))
    time.sleep(duration)
    
    stdout.write('\r%s %s %s' % (c, e, c))
    time.sleep(duration)
    
    stdout.write('\r%s %s %s' % (d, e, d))
    time.sleep(duration)


def finishOut():
    stdout.write('\r%s %s %s' % (a, f, a))
    time.sleep(duration)
    
    stdout.write('\r%s %s %s' % (b, f, b))
    time.sleep(duration)
    
    stdout.write('\r%s %s %s' % (c, f, c))
    time.sleep(duration)
    
    stdout.write('\r%s %s %s' % (d, f, d))
    time.sleep(duration)


stdout.write('\n')

while loop_count < 10:
    workOut()
    loop_count += 1

loop_count = 0

while loop_count < 10:
    finishOut()
    loop_count += 1

#!/usr/bin/env python
from math import *

#itera = 1
#iterb = 1

###################################
# the first loop for n is A Loop
# the second loop for x is B Loop
# This is to help figure out what values for n and x are at any given loop.
#
# Changed the formatting of the print statements so they look nicer.

for n in range(20000000, 20000100):
    # Show the A loop number and the value of n.
    """print 'ALoop# {0} : n={1}'.format(itera,n)
    itera = itera + 1"""
    #continue #Comment out this line once troubleshooting is done.
    factors = []
    limit = int(sqrt(n)) + 1
    for x in range(2, limit):
        # Show the B loop number and the value of x.
        """print 'BLoop# {0} : x={1}'.format(iterb,x)
        iterb = iterb + 1
        print ' [{0},{1}]'.format(n,x)"""
        #continue #Comment out this line once troubleshooting is done.
        if n % x == 0:
            factors.append(x)
    if len(factors) == 0:
        print n, 'is a prime number'
    else:
        print n, 'not prime', factors
        #print '    {0}/{1} = {2} r {3} == {0} IS PRIME'.format(n,x,n/x,n%x)

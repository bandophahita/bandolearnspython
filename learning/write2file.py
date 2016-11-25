#!/usr/bin/env python
import cPickle

__author__ = 'marcel.wilson'

d = {1: 'abc', 2: 'xyz'}
dict2 = {5: 'aasdgadhgahbc', 6: 'xsghnmsyz'}
dict3 = {'b': '232342', 'c': '29385039461'}

print "open - write"
fp = open('tempfile.txt', 'wb')

cPickle.dump(d, fp, -1)
cPickle.dump(dict2, fp, -1)
cPickle.dump(dict3, fp, -1)
#file.write(dict.__class__.__name__ + " = "+ str(dict))

fp.close()
print "closed write"

print "open - read"
fp = open('tempfile.txt', 'rb')
first = cPickle.load(fp)
print first
second = cPickle.load(fp)
print second
third = cPickle.load(fp)
print third

fp.close()
print "closed read"

print "end of script"

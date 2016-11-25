__author__ = 'marcel.wilson'
import cPickle
dict = {1: 'abc', 2: 'xyz'}
dict2 = {5: 'aasdgadhgahbc', 6: 'xsghnmsyz'}
dict3 = {'b':'232342', 'c':'29385039461'}

print "open - write"
file = open('tempfile.txt', 'wb')

cPickle.dump(dict, file, -1)
cPickle.dump(dict2, file, -1)
cPickle.dump(dict3, file, -1)
#file.write(dict.__class__.__name__ + " = "+ str(dict))

file.close()
print "closed write"



print "open - read"
file = open('tempfile.txt', 'rb')
first = cPickle.load(file)
print first
second = cPickle.load(file)
print second
third = cPickle.load(file)
print third

file.close()
print "closed read"



print "end of script"
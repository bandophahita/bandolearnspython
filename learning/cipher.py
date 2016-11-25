#!/usr/bin/env python
__author__ = 'marcel.wilson'

startstring = 'Iy uar ati tete akhn moyuf vr tFag elg reio ar ofea etcbmews hdencof'
otherstring = 'If you can read this tweet me back the name of your favorite Fraggle'

# for no other reason than 'because I can'.
# see http://borderreporter.com/wp-content/uploads/2010/02/funny-dog-pictures-loldogs-wharrgarbl.jpg
setbinding = 'WHARRGARBL'

class cipher:
	def __init__(self, string):
		self.string = string
		self.strlist = self.string.split()
		self.string = ''.join(self.strlist)
		# I have this nagging feeling I don't need to set all of these empty vars
		# but I don't see how else I can use them later without setting them now.
		# It just 'feels' like it's not the right thing to do.
		self.lendict = {}
		self.counter = 1
		self.lenlist = 0
		self.newstrlist = []
		self.wordlist = []

		# make dict of each word length in order -
		# I'm kinda proud of this one. Why, I'm not sure... It felt right.
		for word in self.strlist:
			self.lenlist += len(word)
			self.lendict[self.counter] = len(word)
			self.counter += 1

	#slice off letter from left side of string
	def sliceleft(self, chars):
		letter = self.string[:chars]
		self.string = self.string[chars:]
		return letter

	#slice off letter from right side of string
	def sliceright(self, chars):
		letter = self.string[-chars:]
		self.string = self.string[:-chars]
		return letter

	def decrypt_mthd(self):
		# There may be a better way to do this besides placing all the letters
		# in a list then .join'ing them into a single string. I just don't know it yet.
		#I felt it was easier to reorder the letter before breaking them up into words.
		while len(self.string) > 0:
			letter = self.sliceleft(1)
			self.newstrlist.append(letter)
			letter = self.sliceright(1)
			self.newstrlist.append(letter)

		self.string = ''.join(self.newstrlist)
		for wrd in sorted(self.lendict):
			word = self.sliceleft(self.lendict[wrd])
			self.wordlist.append(word)

		sentence = ",".join(self.wordlist).replace(",", " ")
		return sentence

	def encrypt_mthd(self):
		leftstr = []
		rightstr = []
		while len(self.string) > 0:
			letter = self.sliceleft(1)
			leftstr.append(letter)
			# I keep thinking I should be checking for len like this in the decrypt_mthd - but it works without it.
			if len(self.string) == 0:
				continue
			letter = self.sliceleft(1)
			rightstr.append(letter)
		rightstr.reverse()
		self.newstrlist = leftstr+rightstr

		self.string = ''.join(self.newstrlist)
		for wrd in sorted(self.lendict):
			word = self.sliceleft(self.lendict[wrd])
			self.wordlist.append(word)

		encrypted_sentence = ",".join(self.wordlist).replace(",", " ")
		return encrypted_sentence

# I like having a easy to read function rather than having to use a class method
# to encrypt/decrypt the strings.  Just looks nicer IMO.
def decrypt(string):
	cypher = cipher(string)
	result = cypher.decrypt_mthd()
	return result
def encrypt(string):
	cypher = cipher(string)
	result = cypher.encrypt_mthd()
	return result

# see? isn't that prettier than cipherobj.decrypt_mthd()
print decrypt(startstring)
print encrypt(otherstring)
print encrypt('I wrote a Python script to scramble sentences Good grief I am a really big nerd')

# just a place to break
print '  end of script'


############################
# David Leonard 		   #
# tutnese.py    		   #
# *~-drksephy.github.io*~- #
############################

import re

language = {
	'b': 'bub',
	'c': 'coch',
	'd': 'dud',
	'f': 'fuf',
	'g': 'gug',
	'h': 'hash',
	'j': 'jug',
	'k': 'kuck',
	'l': 'lul',
	'm': 'mum',
	'n': 'nun', 
	'p': 'pup',
	'q': 'quack',
	'r': 'rur',
	's': 'sus',
	't': 'tut',
	'v': 'vuv',
	'w': 'wack',
	'x': 'xux',
	'y': 'yub',
	'z': 'zug'
}

doubleLanguage = {
	'bb': 'squab',
	'cc': 'squac',
	'dd': 'squad',
	'ff': 'squaf',
	'gg': 'squag',
	'hh': 'squah',
	'jj': 'squaj',
	'kk': 'squak',
	'll': 'squal',
	'mm': 'squam',
	'nn': 'squan',
	'pp': 'squap',
	'qq': 'squaq',
	'rr': 'squar',
	'ss': 'squas',
	'tt': 'squat',
	'vv': 'squav',
	'ww': 'squaw',
	'xx': 'squax',
	'yy': 'squay',
	'zz': 'squaz',
}

vowels = ['a', 'o', 'e', 'i', 'u']
# Get all keys from language dictionary
languageKeys = language.keys()

# Create dictionary where key/values are reversed
languageReversed = dict (zip(language.values(), language.keys()))

# Get list of keys in reversed dictionary
languageReversedKeys = languageReversed.keys()

def encode(phrase):
	lowerPhrase = phrase.lower()
	words = lowerPhrase.split()
	# print words
	translation = []
	for word in words:
		currWord = ''
		for i in range(len(word)):
			# Store current letter
			currLetter = word[i]
			nextLetter = ''
			prevLetter = ''
			# Get the next letter
			if i < len(word) - 1:
				nextLetter = word[i + 1]
			# Get the previous letter if possible
			if i > 0:
				prevLetter = word[i - 1]
			# Handle double character case
			if currLetter == nextLetter and currLetter not in vowels:
				currWord += 'squa'
			# Previous character case
			# Now we insert the repeated character
			elif currLetter == prevLetter:
				currWord += currLetter
			elif currLetter in language.keys():
				currWord += language[currLetter]
			else:
				currWord += currLetter
		translation.append(currWord)
	return ' '.join(translation)

# print encode('Over hill, over dale, Thorough bush, thorough brier, Over park, over pale, Thorough flood, thorough fire!')
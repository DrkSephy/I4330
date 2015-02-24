import re

language = {
	'a': 'a',
	'b': 'bub',
	'c': 'coch',
	'd': 'dud',
	'e': 'e',
	'f': 'fuf',
	'g': 'gug',
	'h': 'hash',
	'j': 'jug',
	'k': 'kuck',
	'l': 'lul',
	'm': 'mum',
	'n': 'nun',
	'o': 'o', 
	'p': 'pup',
	'q': 'quack',
	'r': 'rur',
	's': 'sus',
	't': 'tut',
	'u': 'u',
	'v': 'vuv',
	'w': 'wack',
	'x': 'xux',
	'y': 'yub',
	'z': 'zug'
}

# Get all keys from language dictionary
languageKeys = language.keys()

# Create dictionary where key/values are reversed
languageReversed = dict (zip(language.values(), language.keys()))

# Get list of keys in reversed dictionary
languageReversedKeys = languageReversed.keys()

def encode(phrase):
	final_str = ''
	for char in phrase:
		# print languageReversed[char]
		pattern = re.compile(char)
		final_str += re.sub(pattern, language[char], char)
	return final_str

print encode('hello')
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

# Get all keys from language dictionary
languageKeys = language.keys()

# Create dictionary where key/values are reversed
languageReversed = dict (zip(language.values(), language.keys()))

# Get list of keys in reversed dictionary
languageReversedKeys = languageReversed.keys()

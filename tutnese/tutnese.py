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

# Get all keys from language dictionary
languageKeys = language.keys()

# Create dictionary where key/values are reversed
languageReversed = dict (zip(language.values(), language.keys()))

# Get list of keys in reversed dictionary
languageReversedKeys = languageReversed.keys()

def encode(phrase):

	final_str = ''
	for item in phrase: 
		pattern = re.compile(item)
		final_str += re.sub(pattern, language[item], item)
	return final_str

print encode('hello world')
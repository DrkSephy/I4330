############################
# David Leonard 		   #
# tests tutnese.py    	   #
# *~-drksephy.github.io*~- #
############################

import unittest
from tutnese import encode
from tutnese import decode
from tutnese import tutneseLexer
from tutnese import tutneseLex

class TestTutneseFunctions(unittest.TestCase):

	def setUp(self):
		self.string = 'Over hill, over dale, Thorough bush, thorough brier, Over park, over pale, Thorough flood, thorough fire!'
		self.encode = 'ovuverur hashisqual, ovuverur dudalule, tuthashorurougughash bubusushash, tuthashorurougughash bubrurierur, ovuverur puparurkuck, ovuverur pupalule, tuthashorurougughash fufluloodud, tuthashorurougughash fufirure!'
		self.decode = self.string.lower()

	def testEncode(self):
		self.assertEqual(encode(self.string), self.encode)

	def testDecode(self):
		self.assertEqual(decode('ovuverur hashisqual, ovuverur dudalule, tuthashorurougughash bubusushash, tuthashorurougughash bubrurierur, ovuverur puparurkuck, ovuverur pupalule, tuthashorurougughash fufluloodud, tuthashorurougughash fufirure!'), 'over hill, over dale, thorough bush, thorough brier, over park, over pale, thorough flood, thorough fire!')

if __name__ == '__main__':
	unittest.main()
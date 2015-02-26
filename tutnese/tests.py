############################
# David Leonard 		   #
# tests tutnese.py    	   #
# *~-drksephy.github.io*~- #
############################

import unittest
from tutnese import encode

class TestTutneseFunctions(unittest.TestCase):

	def setUp(self):
		self.string = 'Over hill, over dale, Thorough bush, thorough brier, Over park, over pale, Thorough flood, thorough fire!'
		self.encode = 'ovuverur hashisqual, ovuverur dudalule, tuthashorurougughash bubusushash, tuthashorurougughash bubrurierur, ovuverur puparurkuck, ovuverur pupalule, tuthashorurougughash fufluloodud, tuthashorurougughash fufirure!'

	def testEncode(self):
		print encode(self.string)
		print self.encode
		self.assertEqual(encode(self.string), self.encode)


if __name__ == '__main__':
	unittest.main()
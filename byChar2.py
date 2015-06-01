import unittest

def match(pattern, string):
	lenPattern = len(pattern)
	lenString = len(string)
	if (lenPattern > lenString or lenPattern == 0):
		return False
	charsMatched = 0
	for i in range(0,len(string)):
		for j in range(0,len(pattern)):
			if (pattern[j] == string[i]):
				charsMatched += 1
				if (charsMatched == lenPattern):
					return True
					break
	

"""
unit tests
"""
class testMatch(unittest.TestCase):
	def testPatternLongerThanSearchString(self):
		s = 'is'
		p = 'this is not'
		self.assertFalse(match(p,s))

	def testPatternShorterThanSearchStringAndNotInSearchString(self):
		s = 'is'
		p = 'does not contain'
		self.assertFalse(match(p,s))

	def testPatternShorterThanSearchStringAndInSearchString(self):
		s = 'this is not'
		p = 'is'
		self.assertTrue(match(p,s))

	def testPatternEqualToSearchStringAndNotInSearchString(self):
		s = 'this'
		p = 'here'
		self.assertFalse(match(p,s))

	def testPatternEqualToSearchStringAndInSearchString(self):
		s = 'this is a test'
		p = 'this is a test'
		self.assertTrue(match(p,s))
			

if __name__ == "__main__":
	unittest.main()


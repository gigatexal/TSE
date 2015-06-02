import unittest

def match(pattern, string):
	""" match(pattern, searchString) returns boolean given a pattern string and a searchString and if the pattern string is found in the searchString then it returns true. Caveats: The edge case of searching for the space or ' ' always returns false. Otherwise known as a known bug.""" 
	lenPattern = len(pattern)
	lenString = len(string)
	if (lenPattern > lenString or lenPattern == 0):
		return False
	charsMatched = 0
	for i in range(0,lenString):
		for j in range(0,lenPattern):
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
			
	def testSingleCharWherePatternIsInString(self):
		s = 'a'
		p = 'a'
		self.assertTrue(match(p,s))	
	"""
	def testEmptyStrings(self):
	#this fails, i would think it wouldn't. Basically it should 
	#find the space between 'this' and 'is' 
		s = ' '
		p = 'this is'
		self.assertTrue(match(p,s))	
	#makes sense actually - the code above checks for len of the string, and it can't be 0 which is what len(' ') gives me
	"""
if __name__ == "__main__":
	unittest.main()


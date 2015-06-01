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
	




if __name__ == "__main__":
	p = "is"
	s = "this is"

	print(match(p,s))



import sys

pattern = sys.argv[1]
strToSearch = sys.argv[2]

strToSearch = strToSearch.lower();

pattern = pattern.lower();

#create a function called match that takes two arguments, one the pattern, the other the string, returns true or false if the pattern is found or not found. use only functions to get the length of a string and one to return the nth character

lenStr = len(strToSearch)

lenPattern = len(pattern)


for i in xrange(0,len(strToSearch)+1):
	if pattern == strToSearch[i:i+lenPattern]:
		print "found: ", pattern
		break

	

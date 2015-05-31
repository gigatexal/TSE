import sys

pattern1 = sys.argv[1]
strToSearch = sys.argv[2]



strToSearch = "This is a test string"
pattern = "ring" 


strToSearch = strToSearch.lower();
pattern = pattern.lower();

#create a function called match that takes two arguments, one the pattern, the other the string, returns true or false if the pattern is found or not found. use only functions to get the length of a string and one to return the nth character

lenStr = len(strToSearch)
lenPattern = len(pattern)

strArr = []

for i in xrange(0,len(strToSearch)+1):
	strArr.append(strToSearch[i:i+lenPattern])

for i in strArr:
	if i == pattern:
		#print ("found")
		print (i)
		break
	else:#to see what and how many times it looped
		print (i)
#is this valid? i mean I don't find the nth character i am splitting the string array into an array of strings...



import sys

pattern = sys.argv[1]
strToSearch = sys.argv[2]

strToSearch = strToSearch.lower();

pattern = pattern.lower();


lenStr = len(strToSearch)

lenPattern = len(pattern)

strArr = []

for i in xrange(0,len(strToSearch)+1):
	strArr.append(strToSearch[i:i+lenPattern])

for i in strArr:
	if i == pattern:
		#print ("found")
		#print (i)
		print "found: ",i
		break


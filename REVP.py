#!/usr/bin/python

#Solution to REVP Rosalind problem - Locating Restriction Sites
#Author: Peter Vlasveld

#read in file and get contents
f1 = open("rosalind_revp.txt")
content = f1.readlines()
f1.close()

#get DNA string from content
DNAStr = ""
for i in xrange(1,len(content)):
    DNAStr += content[i].strip()

#function to return the DNA compliment
def DNACompliment(stri):
	rev = stri[::-1]
	revList = list(rev)
	for i in xrange(0, len(revList)):
		if revList[i] == "A":
			revList[i] = "T"
		elif revList[i] == "T":
			revList[i] = "A"
		elif revList[i] == "G":
			revList[i] = "C"
		elif revList[i] == "C":
			revList[i] = "G"
	revCompStr = "".join(revList)
	return revCompStr

#loop through DNA string
indexes = []
lengths = []
for j in xrange(0, len(DNAStr)-3):
	#evaluating 4 to 12 character sets, taking the reverse compliment and comparing,
	#if a match is found record the index and length and then break
	for k in xrange(4, 13):
		comp = DNACompliment(DNAStr[j:j+k])
		if comp == DNAStr[j:j+k]:
			indexes.extend([j+1])
			lengths.extend([k])
			print(DNAStr[j:j+k])
			break

#output results to a file
f2 = open("output.txt","w")			
for i in xrange(0,len(indexes)):
	f2.write(str(indexes[i]) + " " + str(lengths[i]) + "\n")
f2.close()
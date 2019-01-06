#!/usr/bin/python

#Solution to the ORF rosalind problem - 'Open Reading Frames'
#Author: Peter Vlasveld

#function to generate the orfs
def orfGen(stri):
	#dictionary for translation
	translate = { 
		"AAA":'K', "AAG":'K',
		"GAA":'E', "GAG":'E',
		"AAC":'N', "AAU":'N',
		"GAC":'D', "GAU":'D',
		"ACA":'T', "ACC":'T', "ACG":'T', "ACU":'T',
		"GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A",
		"GGA":"G", "GGC":"G", "GGG":"G", "GGU":"G",
		"GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V",
		"AUG":"M",
		"UAA":"*", "UAG":"*", "UGA":"*",
		"AUC":"I", "AUU":"I", "AUA":"I",
		"UAC":"Y", "UAU":"Y",
		"CAA":"Q", "CAG":"Q",
		"AGC":"S", "AGU":"S", "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S",
		"CAC":"H", "CAU":"H",
		"UGC":"C", "UGU":"C",
		"CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P",
		"UGG":"W",
		"AGA":"R", "AGG":"R", "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R",
		"UUA":"L", "UUG":"L", "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L",
		"UUC":"F", "UUU":"F"
	}
	
	#list to contain protein sequences
	proteins = []

	#loop that runs through the sequences from each amino acid in the sequence
	for i in xrange(0, len(stri)-2):
		tempStr = ""
		tempBool = False
		j = i
		#find an orf and break when it is finished
		while j < len(stri)-2:
			if translate[stri[j:j+3]] == "*":
				tempBool = False
			if translate[stri[j:j+3]] == "M":
				tempBool = True
			if tempBool:
				tempStr += translate[stri[j:j+3]]
			else:
				break
			j += 3
		#add the orf to proteins only if it ends with a stop codon
		if tempStr != "" and tempBool == False:
			proteins.extend([tempStr])
	#return the protein list			
	return proteins

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

#get file content
f = open("rosalind_orf.txt")
content = f.readlines()
f.close()

DNAStr = ""
#construct full DNA sequence
for i in xrange(1, len(content)):
	DNAStr += content[i]

#remove whitespace
noWhiteDNA = "".join(DNAStr.split())

#convert DNA to RNA
RNA = noWhiteDNA.replace("T", "U")

#get DNA compliment and convert that to RNA as well
revCompRNA = DNACompliment(noWhiteDNA).replace("T", "U")

#get orfs for both sequences
protList = orfGen(RNA)
protList.extend(orfGen(revCompRNA))

#get rid of duplicates
finalList = list(set(protList))

#print the list
for i in finalList:
	print(i)
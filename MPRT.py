#!/usr/bin/python
#MPRT - Finding a Protein Motif Solution
#Problem can be found at http://rosalind.info/problems/mprt/
#Author: Peter Vlasveld

import urllib2
import re

#declare motif
motif = "N[^P][ST][^P]"

#read in file
f0 = open("rosalind_mprt.txt", "r")
content = f0.read().splitlines()
f0.close()

#open output file
f1 = open("output.txt", "w+")
#loop through each accession ID
for i in content:
	#get fasta from url
	url = "http://www.uniprot.org/uniprot/" + i + ".fasta"
	response = urllib2.urlopen(url)
	fasta = response.read().splitlines()
	
	#format protein string
	protStr = ""
	for j in fasta:
		if not j.startswith('>'):
			protStr += j
	#construct output strings
	outStr = ""
	for j in range(0, len(protStr)-4):
		if re.match(motif,protStr[j:j+4]):
			outStr += str(j+1) + " "
	
	#output
	if not outStr == "":
		print i
		f1.write(i + "\n")
		print outStr
		f1.write(outStr + "\n")
#close output file
f1.close()

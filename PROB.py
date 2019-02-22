#!/usr/bin/python3
"""
Solutions to the PROB Rosalind Problem - Introduction to Random Strings
Author: Peter Vlasveld
Date: 20190222
"""
import math

#Read in file content into list
f1 = open("rosalind_prob.txt")
content = f1.readlines()
f1.close()

"""
Function to calculate the probability of the exact sequence given the GC-content
@param gc - the GC-content given 
@param seq - the sequence being studied

@return - the raw probability value
"""
def calcProb(gc, seq):
    # get probability for just one nucleotide
    gchalf = gc/2.0
    athalf = (1.0-gc)/2.0

    # multiply all of the probability values for each letter in the sequence
    prob = 1.0
    for i in range(0, len(seq)):
        if seq[i] == 'A' or seq[i] == 'T':
            prob *= athalf
        elif seq[i] == 'G' or seq[i] == 'C':
            prob *= gchalf
    
    # return the probability value
    return prob

# take the log of the probabilities returned by calcProb
# format them to 3 decimal places
gcCons = content[1].split( )
finalProbs = []
for i in gcCons:
    rawProb = calcProb(float(i), content[0])
    finalProbs.append("%.3f" % math.log10(rawProb))

# print the probabilities with spaces in between
print(" ".join(finalProbs))
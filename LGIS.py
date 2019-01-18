#!/usr/bin/python

# Solution to the LGIS Rosalind Problem - Longest Increasing Subsequence
# Author: Peter Vlasveld
# Date: 18/01/2019
import copy

#get input
f1 = open("rosalind_lgis.txt")
content = f1.readlines()
f1.close()

#get array out of content
arr = content[1].split( )

#function to find longest increasing subsequence of arr
def inc (arr):
    #set s array to a list of a list of the first value in arr
    s = [[arr[0]]]
    #loop through arr skipping the first value
    for i in xrange(1,len(arr)):
        #if this arr value is greater than the last element in the last list of s, 
        # then duplicate the last list and append the new value
        if int(arr[i]) > int(s[len(s)-1][len(s[len(s)-1])-1]):
            tempLis = copy.deepcopy(s[len(s)-1])
            tempLis.append(arr[i])
            s.append(tempLis)
        #else if the first list of s is greater than the arr value, make the arr value the new first list
        elif int(s[0][0]) > int(arr[i]):
            s[0] = copy.deepcopy([arr[i]])
        #otherwise, find the list in s where the last value is less greater than the arr value,
        # and replace it with the list before it, with the new value appended to the end
        else:
            for j in xrange(0, len(s)):
                if int(arr[i]) < int(s[j][len(s[j])-1]):
                    s[j] = copy.deepcopy(s[j-1])
                    s[j].append(arr[i])
                    break
    #return the last element of s which at this point is the longest increasing subsequence
    return s[len(s)-1]

#find the longest decreasing subsequence
#the logic is the exact same as the above increasing function, 
# just with all of the greater-than and less-than operators turned around
def dec (arr):
    s = [[arr[0]]]
    for i in xrange(1,len(arr)):
        if int(arr[i]) < int(s[len(s)-1][len(s[len(s)-1])-1]):
            tempLis = copy.deepcopy(s[len(s)-1])
            tempLis.append(arr[i])
            s.append(tempLis)
        elif int(s[0][0]) < int(arr[i]):
            s[0] = copy.deepcopy([arr[i]])
        else:
            for j in xrange(0, len(s)):
                if int(arr[i]) > int(s[j][len(s[j])-1]):
                    s[j] = copy.deepcopy(s[j-1])
                    s[j].append(arr[i])
                    break
    return s[len(s)-1]

#run the functions
inc = inc(arr)
dec = dec(arr)

#print the output to a file
f2 = open("output.txt", "w")
f2.write(" ".join(inc) + "\n")
f2.write(" ".join(dec))
f2.close() 
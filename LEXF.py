#!/usr/bin/python

#LEXF Rosalind.info Solution - Enumerating k-mers Lexicographically
#Author: Peter Vlasveld
#Date: 12/01/2019

#get dataset from file
f1 = open("rosalind_lexf.txt")
content = f1.readlines()
f1.close()

#duplicate the lex set r times
firstLex = content[0].split( )
lex = []
for i in xrange(0, int(content[1])):
    lex.extend(firstLex)

#recursive function to get all possible combinations within the lex set
def wordCombo (arr, data, start, end, index, r):
    if index == r:
        tempStr = ""
        for i in data:
            tempStr += i
        global comboList
        comboList.append(tempStr)
        return
    i = start
    while i <= end and end - i + 1 >= r - index:
        data[index] = arr[i]
        wordCombo(arr, data, i + 1, end, index + 1, r)
        i += 1

#empty lsit to be passed into function
data = [0]*int(content[1])

#global list to be filled with combinations
comboList = []

#run the function, remove duplicates, and sort it alhphabetically
wordCombo(lex,data,0,len(lex)-1,0,int(content[1]))
finalList = list(set(comboList))
sortedList = sorted(finalList)

#print the list to a file
f2 = open("output.txt", "w")
for i in sortedList:
    f2.writelines(i + "\n")
f2.close()

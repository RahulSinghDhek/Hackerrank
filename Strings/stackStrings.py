__author__ = 'rdhek'
import itertools
noOfTestCases = int(raw_input())
#print type(noOfTestCases)
strList =[]
finalList=[]
for x in range(noOfTestCases):
    x=str(raw_input())
    strList.append(x)
    x=str(raw_input())
    strList.append(x)
k=0
count = noOfTestCases
while(count):
    minlen=len(strList[k]) + len(strList[k+1])
    i=0
    j=0
    for x in range(minlen):
        #print strList[0][x], strList[1][x]
        if strList[k][i]<= strList[k+1][j]:
            #print strList[0][i],strList[1][j]
            finalList.append(strList[k][i])
            if ((i+1)< len(strList[k])):
                i= i+1
            else:
                i=len(strList[k])-1
                finalList.append(''.join(sorted(strList[k+1][j:])))
                break
        else:
            finalList.append(strList[k+1][j])
            if ((j+1)< len(strList[k+1])):
                j= j+1
            else:
                j=len(strList[k+1])-1
                finalList.append(''.join(sorted(strList[k][i:])))
                break
    fnl = ''.join(finalList)
    print( fnl)
    fnl =''
    finalList=[]
    k=k+2
    count=count-1


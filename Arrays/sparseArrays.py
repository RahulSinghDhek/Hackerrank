__author__ = 'rdhek'

noOfStrings=int(raw_input())
stringList=[]
queryList=[]
count=[]
for x in range(noOfStrings):
    stringList.append(raw_input())
noOfQueries=int(raw_input())
for y in range(noOfQueries):
    queryList.append(raw_input())
for temp in range(noOfQueries):
    count.append(stringList.count(queryList[temp]))

#print " ".join(map(str,count))
for x in range(len(count)):
    print count[x]


__author__ = 'rdhek'

(noOfsequences,noOfQueries)=map(int,raw_input().split())
sequencesList={}
queryList=[]
lastans=0
for x in range(noOfQueries):
    queryList.append(map(int,raw_input().split()))
i=0
for x in range(noOfQueries):
    compute=(queryList[x][1] ^ lastans) % noOfsequences
    if queryList[i][0]==1:
        #print compute
        if not compute in sequencesList:
            sequencesList[compute]=[queryList[i][2]]
        else:
            sequencesList[compute].append(queryList[i][2])
    else:
        index = queryList[x][2] % len(sequencesList[compute])
        indVal = sequencesList[compute][index]
        lastans = indVal
        print indVal
    i=i+1


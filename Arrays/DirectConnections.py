__author__ = 'rdhek'

noOfTestCases = int(raw_input())
arrLenList=[]
citiList=[]
distList=[]
total=[]
for x in range(noOfTestCases):
    total.append(0)
for x in range(noOfTestCases):
    arrLenList.append(int(raw_input()))
    citiList.append([int (y) for y in raw_input().split()])
    distList.append([int (k) for k in raw_input().split()])

for x in range(noOfTestCases):
    i=0
    j=1
    while i < arrLenList[x]:
        while j < arrLenList[x]:
            prod= distList[x][j] if (distList[x][j]>=distList[x][i]) else distList[x][i]
            #print total[x] , citiList[x][j] , citiList[x][i]
            total[x]= total[x] + abs(citiList[x][j]-citiList[x][i]) * prod
            j=j+1
        i=i+1
        j=i+1
    total[x]=total[x]%1000000007
for x in range(len(total)):
    print total[x]
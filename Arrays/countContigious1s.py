__author__ = 'rdhek'
n=int(raw_input())
arr=[int(y) for y in raw_input().split()]
path=[int(y) for y in raw_input().split()]
i=0
count=0
tempCount=0
while i<n:
    if arr[i]==1:
        while i<n and (arr[i]==1)  :
            tempCount=tempCount+1
            i = i + 1

        if tempCount > count:
            count=tempCount
        tempCount = 0
    else:
        i=i+1
print count

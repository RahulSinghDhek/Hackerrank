__author__ = 'rdhek'

noToBeFound = int(raw_input())
arrayLen = int(raw_input())
arr=[]
#arr = [int(x) for x in raw_input().split()]
for x in raw_input().split():
    arr.append(int(x))
for x in range(len(arr)):
    if arr[x]==noToBeFound:
        print x+1
        break

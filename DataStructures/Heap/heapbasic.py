__author__ = 'rdhek'
# Enter your code here. Read input from STDIN. Print output to STDOUT

import heapq

noOfQueries=int(raw_input())
h=[]
for x in range(noOfQueries):
    temp=[int(y) for y in raw_input().split()]
    if temp[0]==1:
        heapq.heappush(h,temp[1])
    if temp[0]==3:
        print h[0]
    if temp[0]==2:
        for el in range(len(h)):
            if h[el]==temp[1]:
                deleteIndex=el
                break
        h[deleteIndex]=h[-1]
        h.pop()
        heapq.heapify(h)

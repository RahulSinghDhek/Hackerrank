__author__ = 'rdhek'

import heapq

n=int(raw_input())
h=[]
count=0
for x in range(n):
    el = int(raw_input())
    h.append(el)
    heapq.heapify(h)
    count=count+1
    if count%2==1:
        ind = len(h)/2 + 1
        print "%.1f" % h[ind-1]
    else:
        ind= len(h)/2
        val=float((h[ind]+h[ind-1]))/2
        print "%.1f" % val
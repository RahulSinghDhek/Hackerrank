__author__ = 'rdhek'
(shots,stops)=map(int,raw_input().split())
shotList=[[]]
stopList=list
strength=0
for x in range(shots):
    temp=[int(y) for y in raw_input().split()]
    shotList.append(temp)
for x in range(stops):
    (i,j)=map(int, raw_input().split())
    k=1
    while k <= shots:
        if i<=shotList[k][1]<=j or shotList[k][0]<=j<=shotList[k][1]:
            strength=strength+1
        k=k+1
print strength
__author__ = 'rdhek'
noOfCommands= int(raw_input())
arr=[]
for x in range(noOfCommands):
    temp=[y for y in raw_input().split()]
    if temp[0]=='insert':
        arr.insert(int(temp[1]),int(temp[2]))
    if temp[0]=='print':
        print arr
    if temp[0]=='remove':
        arr.remove(int(temp[1]))
    if temp[0]=='append':
        arr.append(int(temp[1]))
    if temp[0]=='sort':
        arr.sort()
    if temp[0]=='pop':
        arr.pop()
    if temp[0]=='reverse':
        arr.reverse()



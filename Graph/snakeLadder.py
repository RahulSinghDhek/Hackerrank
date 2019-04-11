__author__ = 'rdhek'

noOfTestCases=int(raw_input())
ladderList=[]
snakeList=[]
for x in range(noOfTestCases):
    ladder = raw_input()
    for y in raw_input().split():
        ladderList.append(int(y))
    snake = int(raw_input())
    for z in raw_input().split():
        snakeList.append(int(z))
print snakeList
print ladderList

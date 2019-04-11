__author__ = 'rdhek'

dataArray=[ int(x) for x in raw_input().split()]
noOfNOdes=dataArray[0]
noOfQueries=dataArray[1]
rootOfTree=dataArray[2]
nodeColor=[]
treeDict={}
queryList=[]
for x in range(noOfNOdes-1):
    tempArray=[int(y) for y in raw_input().split()]
    if not tempArray[0] in treeDict:
        treeDict[tempArray[0]]=[tempArray[1]]
    else:
        treeDict[tempArray[0]].append(tempArray[1])
for x in range(noOfNOdes):
    nodeColor.append(int(raw_input()))
for x in range(noOfQueries):
    queryList.append(int(raw_input()))
valueList=treeDict[queryList[0]]
queryColor=[]
colorList=[]
for x in range(noOfQueries):
    colorList.append(nodeColor[queryList[x]-1])
    for el in treeDict[queryList[x]]:
        queryColor.append(el)
        if not el in treeDict:
            colorList.append(nodeColor[el-1])
        else:
            colorList.append(nodeColor[el-1])
    print queryColor,"mytrue"
    for el in queryColor:
        if el in treeDict:
            print el,treeDict[el] , "true"
            for a in treeDict[el]:
                colorList.append(nodeColor[a-1])

    #print queryColor
    print len(set(colorList))
    queryColor=[]
    colorList=[]

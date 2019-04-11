__author__ = 'rdhek'

noOfIndices=int(raw_input())
arr = [int(y) for y in raw_input().split()]



def findLeftIndex(element,curInd):
    while(curInd+1):
        if arr[curInd]>element:
            return curInd + 1
        curInd=curInd-1
    return 0

def findRightIndex(element,curInd):
    while(curInd<noOfIndices):
        if arr[curInd]>element:
            return curInd + 1
        curInd = curInd+1
    return 0

def main():
    maxProd=0
    i=1
    while((i)<noOfIndices):
       left=findLeftIndex(arr[i],i-1)
       if left != 0:
           right=findRightIndex(arr[i],i+1)
           if right !=0:
              prod=(left)*(right);
              if prod>maxProd:
                  maxProd=prod
       i=i+1
    print maxProd

if __name__ == '__main__':
    main()






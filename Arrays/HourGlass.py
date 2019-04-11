__author__ = 'rdhek'

import sys



arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)


def findHourGlassSum(startIndRow,startIndCol):
    return (arr[startIndRow][startIndCol]+ arr[startIndRow][startIndCol+1]+ arr[startIndRow][startIndCol+2] +
                arr[startIndRow+2][startIndCol]+ arr[startIndRow+2][startIndCol+1] + arr[startIndRow+2][startIndCol+2]+
                arr[startIndRow+1][startIndCol+1])

def maxHourGlassSum():
    maxSum=-99999
    i=0
    j=0
    while i < 4:
        while j <4:
            hourGlassSum=findHourGlassSum(i,j)
            if hourGlassSum>=maxSum:
                maxSum=hourGlassSum
            j=j+1
        i=i+1
        j=0
    return maxSum

def main():
    print maxHourGlassSum()

if __name__ == '__main__':
    main()




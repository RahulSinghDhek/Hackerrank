from __future__ import division
__author__ = 'rdhek'
# Enter your code here. Read input from STDIN. Print output to STDOUT


def maxSumSubArray(ar,el):
    temp=sum(ar[:el])
    tempSum=temp
    maxSum=temp
    x=el+1
    while el<len(ar):
        if tempSum+ar[x]>tempSum:
            tempSum=tempSum+ar[x]
        if tempSum<0:
            tempSum=0
        if tempSum>maxSum:
            maxSum=tempSum
        el=el+1
    return maxSum
def findMax(ar):
    maxEle=ar[0]
    i=1
    while i< len(ar):
        if ar[i]>maxEle:
            maxEle=ar[i]
        i=i+1
    return maxEle

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def outPut():
    totalSum=0
    g=0
    gcdNo=1
    noOfTestCases=int(raw_input())
    for x in range(noOfTestCases):
        (n,p,k)=map(int,raw_input().split())
        arr=[int(y) for y in raw_input().split()]
        if k>1:
            totalSum=maxSumSubArray(arr,k)
        if k==1:
            totalSum=findMax(arr)
        g=(totalSum % p)/n
        if g==(totalSum % p)//n:
            print int(g),"1"
        else:
            gcdNo=gcd(totalSum,n)
            print totalSum//gcdNo , n//gcdNo


def main():
    outPut()

if __name__ == '__main__':
    main()


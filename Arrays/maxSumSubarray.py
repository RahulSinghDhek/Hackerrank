__author__ = 'rdhek'
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
arr=[int(y) for y in raw_input().split()]
tempSum=0
maxSum=0
for x in range(n):
    if arr[x]==0:
        tempSum=0
    else:
        if tempSum+arr[x]>tempSum:
            tempSum=tempSum+arr[x]
        if tempSum<0:
            tempSum=0
        if tempSum>maxSum:
            maxSum=tempSum
print maxSum
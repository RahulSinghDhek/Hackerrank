__author__ = 'rdhek'

def gcd(x,y):
    while(1):
        temp=x%y
        if temp==0:
            return y
        x=y
        y=temp


arrayLen = int(raw_input())
arr1=[]
arr2=[]
count=0
for x in raw_input().split():
    arr1.append(int(x))
for y in raw_input().split():
    arr2.append(int(y))
i=0
j=0
while(i<arrayLen):
    while(j<arrayLen):
        if gcd(arr1[i],arr2[j])!=1 and arr2[j]!=-1:
            arr2[j]=-1
            i=i+1;
            j=j+1;
            count=count+1
            break
        j=j+1
    if arr2[j-1]!=-1:
        i=i+1
    j=0
print count




[n,k]=[int(n) for n in raw_input().split(' ')]
a=[int(n) for n in raw_input().split(' ')]
count=0
start=0
while start<len(a):
    for i in range(start+1,len(a)):
        if (a[start]+a[i])%k==0:
            count+=1
    
    start+=1
print count



n=input()
s=[int(n) for n in raw_input().split(' ')]
[d,m]=[int(n) for n in raw_input().split(' ')]
count=0
start=0
while (m+start)<=len(s):
    if sum(s[start:m+start])==d:
        count+=1
    
    start+=1
print count

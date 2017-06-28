

[n,m]=[int(n) for n in raw_input().split(' ')]

A=[int(n) for n in raw_input().split(' ')]
B=[int(n) for n in raw_input().split(' ')]
count=0

def testA(x):
    Ares=len([1 for i in A if x%i==0])
    if Ares==len(A):
        return 1
def testB(x):
    Bres=len([1 for i in B if i%x==0])
    if Bres==len(B):
        return 1
for j in range(A[len(A)-1],B[0]+1):
    if testA(j)==1 and testB(j)==1:
        count+=1
    else:
        continue
print count    

    

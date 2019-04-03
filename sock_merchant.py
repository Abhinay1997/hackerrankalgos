# Enter your code here. Read input from STDIN. Print output to STDOUT

x = input()
y = input().split(' ')
count = 0

for j in list(set(y)):
    temp = 0
    for k in y:
        if j==k:
            temp+=1
            print(j,k)
    count += temp//2
    print(temp//2)
print(count)
    
  

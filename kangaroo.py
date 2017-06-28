

[x1,v1,x2,v2]=[28,8,96,2]

try:
    y=(x1-x2)/(v2-v1)
    if y>0 and (x1-x2)%(v2-v1)==0:
        print 'YES'
    else:
        print 'NO'
except:
    print "NO"

  

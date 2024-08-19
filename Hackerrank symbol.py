n=int(input())
f=2*n-1
f1=n*3
f2=n*5
s=f-n
l=f2+s

#top
for i in range(0,n):
    #print(' '*(n-i-1),'H'*(i+(i+1)),' '*(n-i-1))
    # print('H'*(i+(i+1)).center(n+n-1,'-'))
    a='H'*(i+(i+1))
    print(a.center(f))
    
#top middle
for i in range(0,n+1):
    a=' '*f1
    b=a.center(f2,'H')
    print(b.center(l))
    #print('  ',a.center(f2,'H'))
    
#center
for i in range(0,n//2+1):
    a='H'*f2
    print(a.center(l))
    
#bottom middle
for i in range(0,n+1):
    a=' '*f1
    b=a.center(f2,'H')
    print(b.center(l))
    
#bottom
for i in range(n-1,0-1,-1):
    #print(' '*(n-i-1),'H'*(i+(i+1)),' '*(n-i-1))
    # print('H'*(i+(i+1)).center(n+n-1,'-'))
    a='H'*(i+(i+1))
    b=a.center(f)
    print(b.rjust(l))  

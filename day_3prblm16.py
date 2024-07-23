# reverse of a given n
n=123
sum=0
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
print(sum)    
#sum of given n
n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)    
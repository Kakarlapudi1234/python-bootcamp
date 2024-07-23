# find the sum of square of a digit
n=int(input())
sum=0
while n>0:
    r=n%10
    sum=sum+r**2
    n=n//10
print(sum)



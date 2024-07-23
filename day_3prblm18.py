#n=1234
#sum=0
##while n>0:
  #  r=n%10
   # if(r%2==0):
    #    sum=sum+r
     #   n=n//10
#print(sum)
#   reverse of a string
      
n=1234
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
    ans=int(rev)
    print(ans)
    print(type(ans))


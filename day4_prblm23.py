# write a program to check uf the given number id prime or not 
a=int(input(" enter a number"))
r=a**0.5
count=0
if a==1:
    print("not a prime number")
elif a==2:
    print("prime number")
for i in range(2,int(r+1)):
    if(r%i==0):
      print(" it is a prime number ")
    else:
      print(" it is not a prime number")    
   
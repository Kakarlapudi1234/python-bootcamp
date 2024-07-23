#Gcd of 2 numbers
a=int(input(" enter 1st nymber:"))
b=int(input(" enter 2nd number:"))
while b!=0:
    a,b=b,a%b
print("the gcd of two numbers is:",a)













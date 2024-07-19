# take a space seperated input from the user and print alternate elements
#my_list=list(map(int,input().split(" ")))
#for i in range(0,len(my_list),2):
 #   print(my_list[i],end=" ")
# you are given ith a comma seperated natural numbers 1 to 10, print only the even numbers
my_list=list(map(int,input().split(",")))
for i in range(1,len(my_list),2):
    print(my_list[i])

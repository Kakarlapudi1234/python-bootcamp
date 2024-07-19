#my_list=list(map(int,input().split(",")))
#count=0
#for i in range(1,len(my_list),2):
 #   count+=1
#print(count)
  
#Question-7.3:-> you are given with a space seperated integer list find no of even elements and no of od elements in a given list.
my_list=list(map(int,input().split(" ")))
even=0
odd=0
for i in range(0,len(my_list)):
    if(my_list[i]%2==0):
        even+=1
    else:
        odd+=1
print(even)
print(odd)

   
         
    

     
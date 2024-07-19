# given an space seperated integer list find the average if elements in the even index
my_list=list(map(int,input().split(" ")))
sum=0
count=0
for i in range(0,len(my_list),2):
   count+=1
   sum+=my_list[i]
avg=sum/count
print(avg)   


  

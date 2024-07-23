# Replace the elements in an array with average of max and min element
my_list=list(map(int,input().split()))
max=my_list[0]
min=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]
        print(max)
    
for i in range(len(my_list)):
    if(my_list[i]<min):
        min=my_list[i]
avg=(max+min)//2
for i in range(len(my_list)):
        my_list[i]=avg
print(my_list)    
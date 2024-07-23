check=['1','2','3','4','5','6','7','8','9']
str="hello123world"
sum=0
for i in str:
    if i in check:
        sum+=int(i)
print(sum)        
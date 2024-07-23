
inp=input()
vowel="aeiou"
consonent="bcdefghijklmnopqrstuvwxyz"
count=0
c=0
inp=i.lower()
for i in inp:
    if(i in vowel):
        count+=1
for i in inp:
    if(i in consonent):
        count+=1
print(count)       


vowel="aeiou"
consonents="bcdefghijklmnopqrstuvwxyz"
ans=" "
i="hello wOrld"
inp=i.lower()
for i in inp:
    if(i in vowel):
        ans+=i
for i in inp:
    if(i in consonents):
        ans+=1
print(count)        

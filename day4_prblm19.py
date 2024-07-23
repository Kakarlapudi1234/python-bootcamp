# password verifier
#Mr.x is trying to create a new passord for his instagram account.these are the required conditions for creating a ne password
# condition1: minimum length is 8,8 to 12 medium, maximum length is 15.
# conition 2: only @,/ are allowed in a password(these are must)
# condition3: no spaces are allowed
# condition4: only alphanumerics are allowed
# you are supposed to print weak if length is exact 8 , medium:length is between 8to 12, Strong: if length is between 12 to 15.
password=input()
n=len(password)
for i in password
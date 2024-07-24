class Animal:
   def speak():
        return "speaking ......."
class Dog(Animal):
    def speak():
       return "Dog is speaking...."
class Puppy(Dog):
    def speak():
       return "puppy is speaking...."
obj3=Puppy
print(obj3.speak())  


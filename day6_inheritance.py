class Animal:
    def speak():
        return "Animal is speaking"
# Single inh:
class Dog(Animal):
    def Bark():
        return "bow....."
#multiple inheritance    
class Puppy(Dog):
    def puppy_speak():
        return "I'm Puppy"       
obj1=Animal
print(obj1.speak())
obj2=Dog
print(obj2.speak())   
print(obj2.Bark())   
obj3=Puppy
print(obj3.speak())
print(obj3.Bark())
print(obj3.puppy_speak())

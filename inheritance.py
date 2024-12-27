# Base class
class Animal:
    def speak(self, sound):
        print(f"Animal speak {sound}")


class Pet:

    def speak(self, sound):
        print(f"Pet speaks {sound}")


# Derived class
class Dog(Pet, Animal):
    def action(self):
        print("Dog action")


# Creating objects of derived classes
dog = Dog()

print(dog.speak(""))
print(dog.speak("bhow"))


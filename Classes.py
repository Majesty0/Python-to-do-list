""" INDIVIDUAL ASSIGNMENT IST1025-A"""
# A python class with attributes "name" and "age" 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Method that returns the name of the person
    def __str__(self):
        return f"{self.name}"
    
# Created instance of the Class Person
instance_name = Person("Martin", 24)
# Prints the name of the person using the __str__ method 
print(instance_name)

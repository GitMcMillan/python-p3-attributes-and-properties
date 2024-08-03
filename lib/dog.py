#!/usr/bin/env python3

# class Human:
#     species = "Homo Sapiens"
#     def __init__(self, name):
#         self.name = name

# guido = Human("Guido")
# guido.species
# # => Homo sapiens
# guido.name
# # => Guido

# #changing the species and name using dot notation
# guido.species = "Python Programmer"
# guido.name = "Guido von Rossum"
# print(guido.species, guido.name)
# print(getattr(guido, "species"))
# print(getattr(guido, "name"))
# setattr(guido, "name", "Guido McButterpants")
# print(getattr(guido, "name"))

# my_attr = "is_a_friend"
# print(getattr(guido, my_attr, False)) #3rd arg returns if attr doesnt exist
# # => False
# setattr(guido, my_attr, True)
# print(getattr(guido, my_attr, False))
# # => True

class Human:
    species = "Homo sapiens"

    def __init__(self, age):
        self.age = age

    def get_age(self):
        print("Retrieving age.")
        return self._age

    def set_age(self, age):
        if (type(age) in (int, float)) and (0 <= age <= 120):
            print(f"Setting age to { age }.")
            self._age = age

        else:
            print("Age must be a number between 0 and 120.")

    age = property(get_age, set_age) #property = calls these functions when anyone accesses the age variable. 

guido = Human(age=67) 
# => Setting age to 67.
guido.age = 0
# => Setting age to 0.
print(guido.age)
guido.age = False
# => Age must be a number between 0 and 120
guido.age = 66
# => Setting age to 66.
print(guido.age)
# => Retrieving age.
# => 66





APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name = "Fido", breed = "Mastiff"):
        self.name = name
        self.breed= breed
        
    def get_name(self):
        return self._name
    
    def set_name(self, name): 
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Fido"
        
   

    name = property(get_name,set_name)
    

    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed,set_breed )




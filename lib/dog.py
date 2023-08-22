#!/usr/bin/env python3

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
    def __init__(self, name = "Ollie", breed = "Mastiff") :
        if type(name) == str and 1 <= len(name) <= 25 and name != "":
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
        
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
      if  type(new_name) == str and 1 <= len(new_name) <= 25 and new_name != "":
          self._name = new_name
      else:
          print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        return self._breed
    
    def set_breed(self, new_breed):
        if type(new_breed) == str and 1 <= len(new_breed) <= 25 and new_breed != "":
            self._breed = new_breed
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)  
    breed = property(get_breed, set_breed)

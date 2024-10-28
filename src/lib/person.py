"""Module for the Person class"""


class Person:
    """This is a person class"""


    def __init__(self, name: str, age: int):
        """Constructor"""
        self.name = name
        self.age = age

    def age_group(self):
        """Age group of person"""
        if self.age < 18:
            return "Kid"
        return "Adult"

    def take_a_walk(self):
        """Walk function"""
        print(f"{self.name} is going for a walk")

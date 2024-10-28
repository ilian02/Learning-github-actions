
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def age_group(self):
        if self.age < 18:
            return "Kid"
        else:
            return "Adult"
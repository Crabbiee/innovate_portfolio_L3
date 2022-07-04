from typing_extensions import Self


class Person():
    def __init__(self, name, age, height):
        self.name= name
        self.age = age
        self.height = height

    def set_hair(self, person_hair):
        self.hair = person_hair

    def get_hair(self):
        print(self.hair)
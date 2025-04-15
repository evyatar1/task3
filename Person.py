class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def printMyself(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def to_dict(self):
        return {
            "type": "Person",
            "name": self.name,
            "age": self.age
        }

from Person import Person

class Employee(Person):
    def __init__(self, name, age, field_of_work, salary):
        super().__init__(name, age)
        self.field_of_work = field_of_work
        self.salary = salary

    def printMyself(self):
        print(f"Name: {self.name}, Age: {self.age}, Field of Work: {self.field_of_work}, Salary: {self.salary}")

    def to_dict(self):
        return {
            "type": "Employee",
            "name": self.name,
            "age": self.age,
            "field_of_work": self.field_of_work,
            "salary": self.salary
        }

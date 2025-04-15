from Person import Person

class Student(Person):
    def __init__(self, name, age, field_of_study, year_of_study, score_avg):
        super().__init__(name, age)
        self.field_of_study = field_of_study
        self.year_of_study = year_of_study
        self.score_avg = score_avg

    def printMyself(self):
        print(f"Name: {self.name}, Age: {self.age}, Field of Study: {self.field_of_study}, "
              f"Year: {self.year_of_study}, Score Avg: {self.score_avg}")

    def to_dict(self):
        return {
            "type": "Student",
            "name": self.name,
            "age": self.age,
            "field_of_study": self.field_of_study,
            "year_of_study": self.year_of_study,
            "score_avg": self.score_avg
        }

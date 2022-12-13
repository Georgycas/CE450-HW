class Student:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def __add__(self, other):
        return Student(self.name + ', ' + other.name, self.courses + other.courses)

    def __str__(self):
        return f'{self.name} is taking {self.courses} courses all together.'

    def __repr__(self):
        return f'({self.name}, {self.courses})'

    def __lt__(self, other):
        return f'{self.name} with {self.courses} courses is taking less than {other.name} with {other.courses} courses '

    def __eq__(self, other):
        return f'Both {self.name} and {other.name} are taking {self.courses} courses)'

    def __ne__(self, other):
        return f'{self.name} with {self.courses} does not have the same courses {other.name} with {other.courses}'

    def __gt__(self, other):
        return f'{self.name} with {self.courses} courses is taking more than {other.name} with {other.courses} courses '


a = Student('Peter', 3)
b = Student('Mike', 4)
c = Student('John', 5)
d = Student('Kelvin', 3)

print(a + b + c)
print(a != d)
print(b < c)


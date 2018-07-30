# Example 1: without static
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(marks) / len(marks)

    def go_to_school(self):
        return "I'm going to school"

anna = Student("Anna", "Oxford")
rolf = Student("Rolf", "Harvard")

print(anna.go_to_school())
print(rolf.go_to_school())
print("\n")

# Example 2: With static
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(marks) / len(marks)

    @classmethod
    def is_this_equal(cls):
        print(cls("Anna", "Oxford")) # One way to create a object
        print(Student("Anna", "Oxford")) # The other way to create a object


    # You don't needa use class method most of the time.
    @classmethod
    def go_to_school_class(cls): # cls means the whole class object(Student)
        return "I'm going to school - classmethod"

    @staticmethod
    def go_to_school_static():
        return "I'm going to school - staticmethod"

anna = Student("Anna", "Oxford")
rolf = Student("Rolf", "Harvard")

Student.is_this_equal()
print(anna.go_to_school_class())
print(rolf.go_to_school_static())
print(Student.go_to_school_class())
print(Student.go_to_school_static())
print("\n")

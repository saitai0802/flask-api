# Example 1
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(marks) / len(marks)

    def friend(self, friend_name):
        return Student(friend_name, self.school)

anna = Student("Anna", "Oxford")

friend = anna.friend("Greg")
print(anna.name)
print(anna.school)
print(friend.name)
print(friend.school)
print("\n")

# Example 2 - Error Case, we don't have relationship there.
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school) # will call the Class parameter
        self.salary = salary

rolf = WorkingStudent("Rolf", "Harvard", 20.00)
sue = rolf.friend("Sue")
print(rolf.salary) # 20.00
# print(sue.salary)  # Error! Becuase Student.friend used self object.
print("\n")

# Example 3 -
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(marks) / len(marks)

    @classmethod
    # def friend(cls, origin, friend_name, *args, **kwargs): <== it is very comman to includ both args and kwargs.
    def friend(cls, origin, friend_name, *args):
        return cls(friend_name, origin.school, *args)
    # def friend(cls, origin, friend_name,salary):
        # return cls(friend_name, origin.school, salary)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

rolf = WorkingStudent("Rolf", "Harvard", 20.00)
sue = WorkingStudent.friend(rolf, "Sue", 15.00)
print(sue.salary)  # This works!

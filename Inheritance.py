class Student:

    def __init__(self):
        print("Student exists")

    def type(self):
        print("Type of student")

    def study(self):
        print("studies")


class Honors(Student):

    def __init__(self):
        super().__init__()
        
        print("Honors student created")

    def type(self):
        print("Honors student")

    def read(self):
        print("Reads books")

s = Honors()
s.type()
s.study()
s.read()

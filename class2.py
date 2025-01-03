class Student:
    def get(self):
        self.rollno=int(input("Enter Roll Number"))
        self.name=input("Enter name")
        self.totalmark=float(input("Enter Total mark"))

    def disp(self):
        print("\nStudents Details:")
        print(f"Roll no:{self.rollno}")
        print(f"Name:{self.name}")
        print(f"Total Marks:{self.totalmark}")

stud1=Student()
stud1.get()
stud1.disp()


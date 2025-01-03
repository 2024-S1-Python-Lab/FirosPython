class Student:
    def get(self,rollno,name,totalmark):
        self.rollno=rollno
        self.name=name
        self.totalmark=totalmark

    def disp(self):
        print(f"Roll no:{self.rollno}")
        print(f"Name:{self.name}")
        print(f"Total Marks:{self.totalmark}")

stud1=Student()
stud1.get(101,"firos",23)
stud1.disp()

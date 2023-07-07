class Student:

    def __init__(self,id,name):
        self.id=id
        self.name=name

    def display(self):
        print(self.id,self.name)


s1=Student(11,"pavan")
s1.display()

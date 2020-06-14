# Module 8
#   Programming Assignment 11
#     Prob-2.py

class Student:
    def __init__(self,name,IDnum,major,GPA):
        self._name = name
        self._IDnum = IDnum
        self._major = major
        self._GPA = GPA

    def set_name(self,name):
        self._name = name
    def get_name(self):
        return self._name
    def set_IDnum(self,IDnum):
        self._IDnum = IDnum
    def get_IDnum(self):
        return self._IDnum
    def set_major(self,major):
        self._major = major
    def get_major(self):
        return self._major 
    def set_GPA(self,GPA):
        self._GPA = GPA
    def get_GPA(self):
        return self._GPA
def studentprog ():
    studentlist = []
    studentlist.append(Student("Joe Bella", "9933","",""))
    studentlist.append(Student("Tucker Blank", "3399","",""))
    studentlist.append(Student("Gayle Ujifusa", "9875","",""))
    studentlist.append(Student("Edna Anker", "9875","",""))
#chose to set id number and student name as constant since these are not very often subject to change
    studentlist[0].set_major("Programmer")
    studentlist[0].set_GPA("2.5")
    studentlist[1].set_major("Basket Weaving")
    studentlist[1].set_GPA("3.9")
    studentlist[2].set_major("Janitor")
    studentlist[2].set_GPA("3.2")
    studentlist[3].set_major("Zoo Keeper")
    studentlist[3].set_GPA("1.9")
#since these are items subject to change and fluctuate it made more sent to set these seperately 

    for stu in studentlist:
        print(stu.get_name())
        print(stu.get_IDnum())
        print(stu.get_major())
        print(stu.get_GPA())
        
        print()

studentprog()


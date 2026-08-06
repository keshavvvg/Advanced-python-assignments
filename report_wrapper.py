def report_header(func):
    def wrapper(*args, **kwargs):
        print("="*50)
        print(" "*25,"STUDENT REPORT"," "*25)
        print("="*50)
        func(*args,**kwargs)
        print("="*50)
        print(" "*25,"THANK YOU"," "*25)
    return wrapper

class Report:
    college="MIT ADTU"
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    @classmethod
    def change_college(cls,new_name):
        cls.college=new_name

    def __str__(self):
        return f"NAME : {self.name}\nROLLNO : {self.rollno}\nMARKS : {self.marks}"

    @report_header
    def display_report(self):
        print("COLLEGE : ",Report.college)
        print(self)
        if self.marks>=40:
            print("RESULT : PASS!!!")
        else:
            print("RESUT : FAIl....")

student1=Report("Rahul",1001,85)
student1.display_report()
print()
Report.change_college("MIT WPU")
student2=Report("Priya",1002,36)
student2.display_report()



#OUTPUT
'''
==================================================
                          STUDENT REPORT                          
==================================================
COLLEGE :  MIT ADTU
NAME : Rahul
ROLLNO : 1001
MARKS : 85
RESULT : PASS!!!
==================================================
                          THANK YOU                          

==================================================
                          STUDENT REPORT                          
==================================================
COLLEGE :  MIT WPU
NAME : Priya
ROLLNO : 1002
MARKS : 36
RESUT : FAIl....
==================================================
                          THANK YOU                 
'''

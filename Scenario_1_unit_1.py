class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks
        self.grade = self._assign_grade()

    def _assign_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"

    def display_details(self):
        print(f"Roll No: {self.roll_number:<5} | Name: {self.name:<15} | Marks: {self.marks:<5.1f} | Grade: {self.grade}")


class College:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Added student: {student.name}")

    def display_all_students(self):
        print(f"\n{'=' * 15} {self.name} - Student Directory {'=' * 15}")
        if not self.students:
            print("No records found.")
            return
        for student in self.students:
            student.display_details()


# Demonstration
if __name__ == "__main__":
    # Create College Instance
    my_college = College("MIT ADTU")
    # Create Student Instances
    s1 = Student(101, "Alice Smith", 92.5)
    s2 = Student(102, "Bob Johnson", 78.0)
    s3 = Student(103, "Charlie Brown", 64.5)
    s4 = Student(104, "Diana Prince", 45.0)
    s5 = Student(105, "Eric Stanford", 39.0)
    # Add Students to College
    print("--- Registering Students ---")
    my_college.add_student(s1)
    my_college.add_student(s2)
    my_college.add_student(s3)
    my_college.add_student(s4)
    my_college.add_student(s5)
    # Display All Student Details
    my_college.display_all_students()




#OUTPUT

'''
--- Registering Students ---
Added student: Alice Smith
Added student: Bob Johnson
Added student: Charlie Brown
Added student: Diana Prince
Added student: Eric Stanford

=============== MIT ADTU - Student Directory ===============
Roll No: 101   | Name: Alice Smith     | Marks: 92.5  | Grade: A
Roll No: 102   | Name: Bob Johnson     | Marks: 78.0  | Grade: B
Roll No: 103   | Name: Charlie Brown   | Marks: 64.5  | Grade: C
Roll No: 104   | Name: Diana Prince    | Marks: 45.0  | Grade: F
Roll No: 105   | Name: Eric Stanford   | Marks: 39.0  | Grade: F
'''

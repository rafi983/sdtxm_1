class StudentNotFoundError(Exception):
    pass

class StudentAlreadyEnrolledError(Exception):
    pass

class StudentNotEnrolledError(Exception):
    pass


class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

    @classmethod
    def get_student(cls, student_id):
        for student in cls.student_list:
            if student.student_id == student_id:
                return student
        raise StudentNotFoundError(f"Invalid student ID. Student not found.")

class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.is_enrolled:
            raise StudentAlreadyEnrolledError(f"Student {self.name} is already enrolled.")
        self.is_enrolled = True

    def drop_student(self):
        if not self.is_enrolled:
            raise StudentNotEnrolledError(f"Student {self.name} is already dropped or not enrolled.")
        self.is_enrolled = False

    def view_student_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Enrollment Status: {'Enrolled' if self.is_enrolled else 'Not Enrolled'}")
        print("-" * 20)

def main():
    while True:
        print("\nMenu:")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            if not StudentDatabase.student_list:
                print("No students found.")
            else:
                for student in StudentDatabase.student_list:
                    student.view_student_info()
        elif choice == '2':
            student_id = input("Enter student ID to enroll: ")
            try:
                student = StudentDatabase.get_student(student_id)
                student.enroll_student()
                print(f"Student {student.name} has been enrolled.")
            except (StudentNotFoundError, StudentAlreadyEnrolledError) as e:
                print(f"Error: {e}")
        elif choice == '3':
            student_id = input("Enter student ID to drop: ")
            try:
                student = StudentDatabase.get_student(student_id)
                student.drop_student()
                print(f"Student {student.name} has been dropped.")
            except (StudentNotFoundError, StudentNotEnrolledError) as e:
                print(f"Error: {e}")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Create some dummy students for testing
    Student("1", "Alice", "CS", False)
    Student("2", "Bob", "Math", True)
    main()

class StudentNotFoundError(Exception):
    pass

class StudentAlreadyEnrolledError(Exception):
    pass

class StudentNotEnrolledError(Exception):
    pass


class StudentDatabase:
    __student_list = []

    @classmethod
    def add_student(cls, student):
        cls.__student_list.append(student)

    @classmethod
    def get_students(cls):
        return cls.__student_list

class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    @property
    def student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    def enroll_student(self):
        if self.__is_enrolled:
            raise StudentAlreadyEnrolledError(f"Student {self.__name} is already enrolled.")
        self.__is_enrolled = True

    def drop_student(self):
        if not self.__is_enrolled:
            raise StudentNotEnrolledError(f"Student {self.__name} is already dropped or not enrolled.")
        self.__is_enrolled = False

    def view_student_info(self):
        print(f"Student ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        print(f"Enrollment Status: {'Enrolled' if self.__is_enrolled else 'Not Enrolled'}")
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
            students = StudentDatabase.get_students()
            if not students:
                print("No students found.")
            else:
                for student in students:
                    student.view_student_info()
        elif choice == '2':
            student_id = input("Enter student ID to enroll: ")
            found = False
            for student in StudentDatabase.get_students():
                if student.student_id == student_id:
                    found = True
                    try:
                        student.enroll_student()
                        print(f"Student {student.name} has been enrolled.")
                    except StudentAlreadyEnrolledError as e:
                        print(e)
                    break
            if not found:
                print("Error: Invalid student ID. Student not found.")
        elif choice == '3':
            student_id = input("Enter student ID to drop: ")
            found = False
            for student in StudentDatabase.get_students():
                if student.student_id == student_id:
                    found = True
                    try:
                        student.drop_student()
                        print(f"Student {student.name} has been dropped.")
                    except StudentNotEnrolledError as e:
                        print(e)
                    break
            if not found:
                print("Error: Invalid student ID. Student not found.")
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

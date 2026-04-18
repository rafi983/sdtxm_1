class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.is_enrolled = False

    def __str__(self):
        status = "Enrolled" if self.is_enrolled else "Not Enrolled"
        return f"ID: {self.student_id}, Name: {self.name}, Status: {status}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def display_menu(self):
        print("\nMenu:")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_all_students()
            elif choice == '2':
                self.enroll_student()
            elif choice == '3':
                self.drop_student()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def view_all_students(self):
        if not self.students:
            print("No students found.")
        else:
            print("\n--- All Students ---")
            for student in self.students:
                print(student)
            print("--------------------")

    def enroll_student(self):
        student_id = input("Enter student ID: ")
        for student in self.students:
            if student.student_id == student_id:
                if student.is_enrolled:
                    print(f"Student {student.name} is already enrolled.")
                else:
                    student.is_enrolled = True
                    print(f"Student {student.name} enrolled successfully.")
                return

        # If student ID doesn't exist, create a new student
        name = input("Enter student name: ")
        new_student = Student(student_id, name)
        new_student.is_enrolled = True
        self.students.append(new_student)
        print(f"Student {name} added and enrolled successfully.")

    def drop_student(self):
        student_id = input("Enter student ID to drop: ")
        for student in self.students:
            if student.student_id == student_id:
                if student.is_enrolled:
                    student.is_enrolled = False
                    print(f"Student {student.name} dropped successfully.")
                else:
                    print(f"Student {student.name} is not currently enrolled.")
                return
        print("Student not found.")


def main(students=None):
    app = StudentManagementSystem()
    if students:
        app.students.extend(students)
    app.run()


if __name__ == "__main__":
    # Create some dummy students for testing
    s1 = Student("1", "Alice")
    s2 = Student("2", "Bob")
    s2.is_enrolled = True
    main([s1, s2])

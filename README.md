# Student Management System

A Python-based command-line application to manage student enrollments, allowing you to view, enroll, and drop students.

## Features

- **Create and Manage Students:** Define students with unique IDs and tracking of their enrollment status.
- **Menu-Driven Interface:** Interact via a simple console-based menu.
- **View Students:** Display a list of all students and their current enrollment status.
- **Enroll Students:** Create a new student profile and enroll them, or update the status of an existing but unenrolled student.
- **Drop Students:** Change the status of an enrolled student to 'Not Enrolled'.

## Project Structure

The workspace contains various Python scripts that represent the development steps and different aspects of the system:
- `Create the Student class.py`: Blueprint for the student object.
- `Create the StudentDatabase class.py`: Handles data logic for student storage.
- `Data Privacy.py`: Concepts related to data protection.
- `Error Handling.py`: Robust input and exception handling implementations.
- `Implement drop_student() method.py`: Focuses on the logic to remove a student from the active list.
- `Implement enroll_student() method.py`: Focuses on adding students to the system.
- `Implement view_student_info() method.py`: Displays individual and aggregate student details.
- `Initialize Student Object.py`: Simple initialization scripts.
- `Menu System.py`: The complete interactive system tying all components together.

## How to Run

To run the complete system, execute the `Menu System.py` file:

```bash
python "Menu System.py"
```

Follow the on-screen prompts to manage students.

## Requirements

- Python 3.x


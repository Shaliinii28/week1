import os

class Student:
    """Class to represent a student with ID, name, and department"""
    def __init__(self, student_id, name, department):
        self._student_id = student_id    
        self._name = name               
        self._department = department   

    def to_string(self):
        """Return student details as a string for file storage"""
        return f"{self._student_id}|{self._name}|{self._department}"

    def __str__(self):
        """String representation of the student"""
        return f"ID: {self._student_id}, Name: {self._name}, Department: {self._department}"

class StudentManagementSystem:
    """Class to manage student records with add, remove, search, and file operations"""
    def __init__(self, filename="students.txt"):
        self._students = {}  
        self._filename = filename
        self._valid_departments = {"CS", "Mechanical", "Civil"}
        self.load_students()

    def load_students(self):
        """Load student data from text file"""
        self._students.clear()  
        if os.path.exists(self._filename):
            try:
                with open(self._filename, 'r', encoding='utf-8') as file:
                    for line in file:
                        if line.strip():
                            try:
                                student_id, name, department = line.strip().split('|')
                                if department.upper() in [d.upper() for d in self._valid_departments]:
                                    student = Student(student_id, name, department)
                                    self._students[student_id] = student
                            except ValueError:
                                print(f"Warning: Skipping invalid line in file: {line.strip()}")
                print(f"Loaded {len(self._students)} students from {self._filename}")
            except Exception as e:
                print(f"Error loading students: {e}")
        else:
            print(f"No existing file found at {self._filename}. Starting with empty student list.")

    def save_students(self):
        """Save student data to text file"""
        try:
            with open(self._filename, 'w', encoding='utf-8') as file:
                for student in self._students.values():
                    file.write(f"{student.to_string()}\n")
            print(f"Student data saved successfully to {self._filename}")
        except Exception as e:
            print(f"Error saving students: {e}")

    def add_student(self, student_id, name, department):
        """Add a new student to the system"""
        try:
            student_id = student_id.strip()
            name = name.strip()
            department = department.strip()
            
            if not student_id or not name:
                print("Error: Student ID and name cannot be empty")
                return False
            if department.upper() not in [d.upper() for d in self._valid_departments]:
                print("Error: Department must be CS, Mechanical, or Civil")
                return False
            if student_id in self._students:
                print("Error: Student ID already exists")
                return False
                
            department = next(d for d in self._valid_departments if d.upper() == department.upper())
            student = Student(student_id, name, department)
            self._students[student_id] = student
            print(f"Added student: {student}")
            self.save_students()
            return True
        except Exception as e:
            print(f"Error adding student: {e}")
            return False

    def remove_student(self, student_id):
        """Remove a student by ID"""
        try:
            if student_id in self._students:
                student = self._students.pop(student_id)
                print(f"Removed student: {student}")
                self.save_students()
                return True
            else:
                print("Error: Student ID not found")
                return False
        except Exception as e:
            print(f"Error removing student: {e}")
            return False

    def search_student(self, student_id):
        """Search for a student by ID"""
        try:
            if student_id in self._students:
                print(f"Found student: {self._students[student_id]}")
                return self._students[student_id]
            else:
                print("Error: Student ID not found")
                return None
        except Exception as e:
            print(f"Error searching student: {e}")
            return None

    def display_all_students(self):
        """Display all students in the system"""
        if not self._students:
            print("No students in the system")
        else:
            print("\nAll Students:")
            for student in self._students.values():
                print(student)

def main():
    sms = StudentManagementSystem()
    
    while True:
        print("\nStudent Management System:")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '1':
            student_id = input("Enter student ID: ").strip()
            name = input("Enter student name: ").strip()
            department = input("Enter department (CS/Mechanical/Civil): ").strip()
            sms.add_student(student_id, name, department)
        
        elif choice == '2':
            student_id = input("Enter student ID to remove: ").strip()
            sms.remove_student(student_id)
        
        elif choice == '3':
            student_id = input("Enter student ID to search: ").strip()
            sms.search_student(student_id)
        
        elif choice == '4':
            sms.display_all_students()
        
        elif choice == '5':
            print("Exiting Student Management System")
            break
        
        else:
            print("Error: Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
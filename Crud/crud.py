import mysql.connector
from mysql.connector import Error

def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='Admin',  # Replace with your MySQL username
        password='admin@1A',  # Replace with your MySQL password
        database='studentdb'
    )

def insert_student(name, age, class_name, faculty, phone):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (name, age, class, faculty, phone) VALUES (%s, %s, %s, %s, %s)",
                   (name, age, class_name, faculty, phone))
    connection.commit()
    cursor.close()
    connection.close()

def view_students():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def update_student(student_id, name, age, class_name, faculty, phone):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE students SET name=%s, age=%s, class=%s, faculty=%s, phone=%s WHERE id=%s",
                   (name, age, class_name, faculty, phone, student_id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_student(student_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    connection.commit()
    cursor.close()
    connection.close()

# Main program loop with a switch-case-like structure
if __name__ == "__main__":
    while True:
        print("\n Choose an operation:")
        print("1. Insert Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            class_name = input("Enter class: ")
            faculty = input("Enter faculty: ")
            phone = input("Enter phone: ")
            insert_student(name, age, class_name, faculty, phone)
            print("Student inserted successfully.")

        elif choice == '2':
            students = view_students()
            print("Students:", students)

        elif choice == '3':
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            class_name = input("Enter new class: ")
            faculty = input("Enter new faculty: ")
            phone = input("Enter new phone: ")
            update_student(student_id, name, age, class_name, faculty, phone)
            print("Student updated successfully.")

        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
            print("Student deleted successfully.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

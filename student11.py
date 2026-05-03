students = []

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    students.append({"name": name, "roll": roll})
    print("Student added successfully!\n")
    print(roll)

def view_students():
    if not students:
        print("No students found\n")
        return
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}")
    print()

def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"Found: {s['name']}\n")
            return
    print("Student not found\n")

def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Deleted successfully\n")
            return
    print("Student not found\n")

while True:
    print("1.Add 2.View 3.Search 4.Delete 5.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice\n")

import csv
import os

FILE_NAME = "students.csv"
SUBJECTS = ["Python", "C", "Mathematics", "English", "Physics"]

# Load student records
def load_data():
    students = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

    return students


# Save student records
def save_data(students):
    with open(FILE_NAME, "w", newline="") as file:
        fields = ["roll", "name"] + SUBJECTS
        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()
        writer.writerows(students)


# Validate marks
def get_marks(subject):
    while True:
        try:
            mark = int(input(f"Enter {subject} marks (0-100): "))

            if 0 <= mark <= 100:
                return mark
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


# Add student
def add_student(students):
    print("\n--- Add Student ---")

    roll = input("Enter Roll Number: ").strip()

    if not roll:
        print("Roll number cannot be empty.")
        return

    for student in students:
        if student["roll"] == roll:
            print("Roll number already exists!")
            return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    student = {
        "roll": roll,
        "name": name
    }

    for subject in SUBJECTS:
        student[subject] = str(get_marks(subject))

    students.append(student)
    save_data(students)

    print("Student record added successfully!")


# Display all students
def display_students(students):
    print("\n--- Student Records ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\nRoll Number:", student["roll"])
        print("Name:", student["name"])

        for subject in SUBJECTS:
            print(subject + ":", student[subject])


# Search student
def search_student(students):
    roll = input("Enter Roll Number to search: ").strip()

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll"])

            for subject in SUBJECTS:
                print(subject + ":", student[subject])

            return

    print("Student not found!")


# Calculate student performance
def calculate_performance(students):
    print("\n--- Performance Summary ---")

    if not students:
        print("No records available.")
        return

    for student in students:
        marks = [int(student[s]) for s in SUBJECTS]

        total = sum(marks)
        average = total / len(SUBJECTS)

        status = "PASS" if all(m >= 35 for m in marks) else "FAIL"

        print("\nName:", student["name"])
        print("Roll Number:", student["roll"])
        print("Total Marks:", total, "/ 500")
        print("Average:", round(average, 2))
        print("Result:", status)


# Subject-wise summary
def subject_summary(students):
    print("\n--- Subject-wise Performance ---")

    if not students:
        print("No records available.")
        return

    for subject in SUBJECTS:
        marks = [int(s[subject]) for s in students]

        average = sum(marks) / len(marks)

        print(subject, "Average:", round(average, 2))


# Generate performance chart
def generate_chart(students):
    if not students:
        print("No records available.")
        return

    try:
        import matplotlib.pyplot as plt

        averages = []

        for subject in SUBJECTS:
            marks = [int(s[subject]) for s in students]
            averages.append(sum(marks) / len(marks))

        plt.bar(SUBJECTS, averages)
        plt.title("Subject-wise Academic Performance")
        plt.xlabel("Subjects")
        plt.ylabel("Average Marks")
        plt.ylim(0, 100)
        plt.grid(axis="y")
        plt.show()

    except ImportError:
        print("Please install matplotlib using pip install matplotlib")


# Export summary
def export_summary(students):
    if not students:
        print("No records available.")
        return

    with open("performance_report.txt", "w") as file:
        file.write("ACADEMIC PERFORMANCE REPORT\n")
        file.write("===========================\n\n")

        for student in students:
            marks = [int(student[s]) for s in SUBJECTS]
            total = sum(marks)
            average = total / len(SUBJECTS)

            status = "PASS" if all(m >= 35 for m in marks) else "FAIL"

            file.write(f"Name: {student['name']}\n")
            file.write(f"Roll Number: {student['roll']}\n")
            file.write(f"Total: {total}/500\n")
            file.write(f"Average: {average:.2f}\n")
            file.write(f"Result: {status}\n\n")

    print("Report exported successfully!")


# Main menu
def main():
    students = load_data()

    while True:
        print("\n================================")
        print("   ACADEMIC PERFORMANCE DASHBOARD")
        print("================================")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Performance Summary")
        print("5. Subject-wise Summary")
        print("6. Generate Performance Chart")
        print("7. Export Report")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            calculate_performance(students)

        elif choice == "5":
            subject_summary(students)

        elif choice == "6":
            generate_chart(students)

        elif choice == "7":
            export_summary(students)

        elif choice == "8":
            print("Thank you for using Academic Dashboard!")
            break

        else:
            print("Invalid choice! Please select 1 to 8.")


if __name__ == "__main__":
    main()
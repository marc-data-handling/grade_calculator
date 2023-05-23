# We asked chatgpt to provide us with a template for our user interface which we then adapted to our own classes. As demanded by you, we provide this template as our source.

def main():
    student_name = input("Enter student name: ")
    credits_needed = None
    while True:
        try:
            credits_needed = int(input("Enter total credits needed: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    student = Student(student_name, credits_needed)

    while True:
        print("\n-------- Student Menu --------")
        print("1. Add subject")
        print("2. Delete subject")
        print("3. Calculate GPA")
        print("4. View grade transcript")
        print("5. View grade distribution")
        print("6. View completed credits")
        print("7. View subject list")
        print("8. View subject details")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            name = input("Enter subject name: ")
            while True:
                try:
                    grade = float(input("Enter subject grade: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a floating-point number.")

            while True:
                try:
                    credits = int(input("Enter subject credits: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                mandatory_input = input("Is the subject mandatory? (yes/no): ").lower()
                if mandatory_input == "yes":
                    mandatory = True
                    break
                elif mandatory_input == "no":
                    mandatory = False
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            while True:
                try:
                    semester = int(input("Enter subject semester: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            subject = student.generate_subject(name, grade, credits, mandatory, semester)
            print(f"Subject '{subject.get_name()}' added successfully.")

        elif choice == "2":
            name = input("Enter subject name to delete: ")
            student.delete_subject(name)
            print(f"Subject '{name}' deleted successfully.")

        elif choice == "3":
            gpa = student.calculate_gpa()
            print(f"Current GPA: {gpa}")

        elif choice == "4":
            transcript = student.generate_grade_transcript()
            print("Grade Transcript:")
            print(transcript)

        elif choice == "5":
            plt.figure(figsize=(8, 6))
            plt = student.get_grade_distribution()
            plt.show()

        elif choice == "6":
            plt.figure(figsize=(8, 4))
            plt = student.plot_credits()
            plt.show()

        elif choice == "7":
            subject_list = student.get_subject_list()
            print("Subject List:")
            for subject in subject_list:
                print(subject)

        elif choice == "8":
            name = input("Enter subject name: ")
            subject = student.get_subject_details(name)
            if subject:
                print("Subject Details:")
                print(subject)
            else:
                print(f"Subject '{name}' not found.")

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

if __name__ == "__main__":
    main()

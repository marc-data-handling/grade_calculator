# This is the user interface for the terminal. The advantage of this code is, that he allows a user to work with our classes without understanding how Python works.
from student import Student

# This function the interface for a user
def main():
    
    # First we want to generate a Student and therefore the user can insert any characters that will be used as his name
    student_name = input("Enter student name: ")
    # The value of credits_needed has to be an integer and therefore we first initiate an endless while loop which will only be broken, when an integer or a float is insert
    while True:
        try:
            credits_needed = int(input("Enter total credits needed: ")) # The computer will try to execute this line and if he fails to do so he goes to the except statement
            break # This allows us to leave the while loop after a correct value is entered for credits_needed
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # We initialize an object student
    student = Student(student_name, credits_needed)

    # Now we want to define the actual interface. In order to ensure that we do not run in an error or the program runs out we will use a endless while loop which is only broken once the user wants to leave the application.
    while True:
        print("\n-------- Student Menu --------") 
        print("1. Add subject")   # The number 1 to 10 will be the commands from which the user can choose. Each is connected to one of our student methods.
        print("2. Delete subject")
        print("3. Calculate GPA")
        print("4. Calculate GPA by semester")
        print("5. Calculate GPA by mandatory status")
        print("6. Find minimum and maximum grades")
        print("7. Save grade transcript")
        print("8. Save grade distribution")
        print("9. Save completed credits")
        print("10. Load grade transcript")
        print("11. Exit")
        
        print("\nEnter at least 5 subjects before you start working with the option 8 in order to get a nice distribution\n") # We use \n (new line) to make the printed interface look nicer
        
        choice = input("Enter your choice (1-10): ") # The input of the user is stored and then used to trigger the right method

        if choice == "1": # The if and elif-statements ensure that the right method is called
            # In order to generate a subject we need all relevant inputs
            name = input("Enter subject name: ")
            
            # We build an endless while loops as described above and to ensure that the values of grade and credits are floats and of semester is integer. We run the code of the loops until the user entered such a value
            while True: 
                try:
                    grade = float(input("Enter subject grade: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a floating-point number.")

            while True:
                try:
                    credits = float(input("Enter subject credits: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            
            # This loops works the same but accepts two potential inputs that lead to a break and set the boolean value of mandatory accordingly
            while True:
                mandatory_input = input("Is the subject mandatory? (y/n): ").lower() # The lower method ensures that a big Y or N also lead to the same as a y or n.
                if mandatory_input == "y":
                    mandatory = True
                    break
                elif mandatory_input == "n":
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

            # We generate a object with the method generate_subject() so that we can assign the subject to the student
            subject = student.generate_subject(name, grade, credits, mandatory, semester)
            print(f"Subject '{subject.get_name()}' added successfully.")
   
        elif choice == "2":
            name = input("Enter subject name to delete: ")
            for subject in student.get_grades(): # We iterate through the subjects of the student
                if name == subject.get_name(): # If the attribute name of the subject equals the input of the user, we delete the corresponding subject
                    student.delete_subject(name)
                    print(f"Subject '{name}' deleted successfully.")
                else: # If the subject is not existing nothing gets deleted and we print another string
                    print(f"Subject '{name}' not found.")

        elif choice == "3":
            gpa = student.calculate_gpa() # We calculate the overall gpa with the corresponding method and print the float in a fstring
            print(f"Current GPA: {gpa}")

        elif choice == "4":
            gpa = student.calculate_gpa_by_semester() # We do the same as above but for each semester separately
            print(f"GPA by semester: {gpa}")

        elif choice == "5":
            gpa = student.calculate_gpa_by_mandatory_status() # We do the same as above but for mandatory and optional sujects separately
            print(f"GPA by mandatory status: {gpa}")

        # In order to get the best and worst grades we call the corresponding method and print the dict in our fstring
        elif choice == "6":
            gpa = student.get_best_and_worst_grades()
            print(f"Minimum and maximum grades: {gpa}")
            
        # In order to save all subjects in a csv and print the first five, we use the corresponding Python method
        elif choice == "7":
            transcript = student.generate_grade_transcript()
            print("Grade Transcript:")
            print(transcript.head())
        
        # In order to save the own grade distribution we call the respective method
        elif choice == "8":
            student.get_grade_distribution()
            
        # In order to save the progress we call the respective method
        elif choice == "9":
            student.plot_credits()
            
        # If the user enters a 10 he has to enter the name of the grade transcript and the corresponding method is then called
        elif choice == "10":
                file_name = input("Enter the name of your grade transcript: ")
                student.load_grade_transcript(file_name)          
                
        # If the user enters a 11 he breaks the while loop and the program is finished
        elif choice == "11":
            break
        
        # If our program did not receive a number between 1 and 10 as input the, the following statement will be printed and the options are printed again by the while loop
        else:
            print("Invalid choice. Please enter a number from 1 to 10.")

# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
# This is a common python notation and ensures that the main() function is only called when the file is run as main program 
if __name__ == "__main__":
    main()

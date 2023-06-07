import pandas as pd
import matplotlib.pyplot as plt
from subject import Subject

# This class Subjects allows us to generate students as objects, what will allow us to work the subjects in a more efficient way
# Since we have almost no experience in coding we decided to code our classes from scratch to ensure that we have the best possible learning effect. This is the reason why we cannot provide any sources for this file
class Student:
    def __init__(self, name, credits_needed):
        self._name = str(name)
        self._credits_needed = int(credits_needed)
        self._grades = []
       
    # We implement getter and setter methods to ensure that the attributes of the objects are not modified from outside the class manually
    @property
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = str(name)
    
    @property
    def get_credits_needed(self):
        return self._credits_needed
        
    def set_credits_needed(self, credits):
        self._credits_needed = int(credits)
    
    @property
    def get_grades(self):
        return self._grades

    def set_grades(self, grades):
        self._grades = grades
    
    # We define a str() (string representation) method for display purposes
    def __str__(self):
        return f"This is {self._name} with a gpa of {self.calculate_gpa()}"
    
    # We define a repr() (string representation) method that gives a overview over the object
    def __repr__(self):
        return f"Student(name : {self._name}, credits_needed : {self._credits_needed}, subjects : {self._grades})"

        
    #This function generates a new object of the self-written class subject and appends the object to the list that is the attribute grades and returns the object
    def generate_subject(self, name, grade, credits, mandatory, semester):
        subject = Subject(name, grade, credits, mandatory, semester)
        self._grades.append(subject)
        return subject
    
    
    def delete_subject(self, name):
        # The for-loop allows us to check if the input name is equal to the name of one of subjects names in the grades attibute of the Student
        for subject in self._grades:
            if subject.get_name() == name:
                self._grades.remove(subject) # We remove the inserted element of the list
                return self.generate_grade_transcript()
        print(f"There is not subject called {name}.")

    
    def find_subject_by_name(self, name):
        output = {}
        # We iterate over all subjects to find the one where the name matches the input given
        for subject in self._grades:
            if subject.get_name() == name:
                output[subject.get_name()] = {'Grade' : subject.get_grade(), 'Credits' : subject.get_grade()}
        return output
        
    def get_best_and_worst_grades(self):
        # We need two variable which allow us to find min and max
        best_grade = None
        worst_grade = None

        # We loop through all subjects and get the respective grade
        for subject in self._grades:
            
            # If it's a better grade than the previously checked, we store it in the variable and store the name in a list
            if best_grade is None or subject.get_grade() > best_grade.get_grade():
                best_grade = subject
                names_best = [subject.get_name()] # If we have a new worst grade, this list will be overwritten and the new list will only have one element
                
            # If another grade was as good as the best one we add the name of the subject to our list so that we will capture all our best subjects            
            elif best_grade.get_grade() == subject.get_grade():
                names_best.append(subject.get_name())
        
        # We adjust the above code to get the same for the worst grade 
        for subject in self._grades:

            if worst_grade is None or subject.get_grade() < worst_grade.get_grade():
                worst_grade = subject
                names_worst = [subject.get_name()]

            elif worst_grade.get_grade() == subject.get_grade():
                names_worst.append(subject.get_name())
                
        # We generate a dictionary to return the values. The grade is the key because keys cannot be of type lists
        result = {
            best_grade.get_grade() : names_best,
            worst_grade.get_grade() : names_worst
        }

        return result        
    
    def calculate_gpa(self):
        # We initiate two variables since we need them to calculate the the gpa
        total_credits = 0
        own_score = 0

        # We build a for loop that iterates over all elements of the list in attribute grades 
        for subject in self._grades:
            # We need the number of credits as well as the grade for each subject
            credits = subject.get_credits()
            grade = subject.get_grade()
            # We sum up the total credits as well as own_score that contains the grade muliplied by number of credits for each subject
            total_credits += credits
            own_score += grade * credits

        # We calculate the gpa by deviding the own_score by the total credits completed and round it to 3 decimal places
        overall_gpa = own_score / total_credits
        
        # We return the gpa as a float
        return round(overall_gpa, 3)
        
        
    def calculate_gpa_by_semester(self):
        # We will need two dictionaries compute the gpa per semester
        gpa_by_semester = {}
        semester_grades = {}
        
        # First we want to append all subjects to the right semester
        for subject in self._grades: # We iterate over all elements of the list that stores all subjects and thereby grades
            semester = subject.get_semester() # We want to get the semester of the grade to assign the grade correct
            
            # If the semester is not yet in the dictionary then we generate a key-value pair that has a tuple containing grade and credits as value
            if semester not in semester_grades: 
                semester_grades[semester] = []
            semester_grades[semester].append((subject.get_grade(), subject.get_credits()))
            
        # We iterate over the keys and values of the dictionary semester_grades
        for semester, grades in semester_grades.items():
            # We calculate the sum of the credits of the semester (_ should signal that we do not need the first value of the tuple placed in list grades)
            total_credits = sum(credits for _, credits in grades)
            # We calculate the own score by multiplication of grade and credits. We use the same loop as above
            own_score = sum(grade * credits for grade, credits in grades)
            # We get the gpa by dividing own_score by total_credits
            gpa = own_score / total_credits
            #We append the key of semester_grades to gpa_by_semester and the corresponding gpa as value rounded to three decimal places
            gpa_by_semester[semester] = round(gpa, 3)
            
        # We return the dictionary with as many elements as semesters in which subjects were completed
        return gpa_by_semester

    
    def calculate_gpa_by_mandatory_status(self):
        # We initialize the dictionary to return and a list for all mandatory subjects an one for all optional subjects
        gpa_by_mandatory_status = {"mandatory": None, "optional": None}
        mandatory_grades = []
        optional_grades = []
        
        # This for-loop distinguish between mandatory and optional subjects and append the subjects accordingly to the above generated lists
        # We use the fact that the attribute mandatory is of type boolean
        for subject in self._grades:
            if subject.is_mandatory():
                mandatory_grades.append((subject.get_grade(), subject.get_credits()))
            else:
                optional_grades.append((subject.get_grade(), subject.get_credits()))
        
        # Following code will be executed if the list mandatory_grades is not empty
        if mandatory_grades:
            # We use the same code as in the method above
            total_mandatory_credits = sum(credits for _, credits in mandatory_grades)
            weighted_mandatory_sum = sum(grade * credits for grade, credits in mandatory_grades)
            mandatory_gpa = weighted_mandatory_sum / total_mandatory_credits
            # We add the gpa in our dictionary that we want to return
            gpa_by_mandatory_status["mandatory"] = round(mandatory_gpa, 3)

        # This code block works the same way as the above
        if optional_grades:
            total_optional_credits = sum(credits for _, credits in optional_grades)
            weighted_optional_sum = sum(grade * credits for grade, credits in optional_grades)
            optional_gpa = weighted_optional_sum / total_optional_credits
            gpa_by_mandatory_status["optional"] = round(optional_gpa, 3)
        
        # We return the dictionary with two key-value pairs
        return gpa_by_mandatory_status

    
    def generate_grade_transcript(self):
        grade_transcript = []

        # For every subject in our attribute grades we store all attribute of the subject itself
        for subject in self._grades:
            subject_name = subject.get_name()
            grade = subject.get_grade()
            credits = subject.get_credits()
            mandatory = subject.is_mandatory()
            semester = subject.get_semester()
            # We generate a tuple that contains all attribute of the subject
            entry = (subject_name, grade, credits, mandatory, semester)
            # We append the tuble to our list as an element
            grade_transcript.append(entry)

        # We generate a list with our column names
        columns = ["Subject", "Grade", "Credits", "Mandatory", "Semester"]
        # We make a dataframe with the help of pandas library
        # Each list element is a row and each element of the tuple is a value in that row
        df = pd.DataFrame(grade_transcript, columns=columns)
        
        # We store the data frame and return it
        df.to_csv('grade_transcript.csv', index=False)
        return df
    
    # This method allows to read a previous generated grade_transcript that is stored in the same folder. ATTENTION: the grade transcript must have been generated with the method generate_grade_transcript()
    def load_grade_transcript(self, file_name = "grade_transcript.csv"): # The second argument is the file name, that allows the user to name different grade transcripts different.

        # We try to load the file with the corresponding name, if the program fails, except will be run and the user will learn that no such file is saved in the folder
        try:
            df = pd.read_csv(file_name)

            # We iterate over each row of the dataset with iterrows() that returns a series 
            for index, row in df.iterrows():
                # We save each value of the series in a corresponding variable
                subject_name = row['Subject']
                grade = row['Grade']
                credits = row['Credits']
                mandatory = row['Mandatory']
                semester = row['Semester']

                # We generate a new subject with each row using the corresponding method.
                self.generate_subject(subject_name, grade, credits, mandatory, semester)
                # We return student (the repr method) that the user can check if the new subjects are added
            print("The upload was successful")
            return self
        except:
                print(f"There is no file with the name {file_name}")

    def get_grade_distribution(self):
        
        # We use a list comprehension to get a list that contains all grades of a student
        grades = [subject.get_grade() for subject in self._grades]

        #We generate a dataframe with one column called Grades that contains all grades of the student
        df = pd.DataFrame(grades, columns=["Grades"])

        # We use this dataframe to plot a histogram
        # The calculation of the number of bins ensures that we have every 0.25 a tick on the x-axis no matter what the lowest grade is 
        histogram = plt.hist(df["Grades"], bins = max(1,int((6-min(df["Grades"]))*4)), edgecolor="black", alpha= 0.8) # We let the number of bins be the higher number between 1 and our own formula, so that a student that only writes grade 6 does not face an error

        # We add labels on both axis and give the plot a title
        plt.xlabel("Grades")
        plt.ylabel("Frequency")
        plt.title("Grade Distribution")

        # We costumize the ticks on the x axis in order to ensure that all possible sufficient grades as well as the lowest received grade are printed on the x-axis
        custom_ticks = [min(df["Grades"]), 4, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6]
        plt.xticks(custom_ticks)

        # We save the histogram and return it
        plt.savefig("grade_distribution.png")
        return plt.gcf()

    def plot_credits(self):
        
        # First we need the amount of credits completed, we get that by iterating over the objects that are elements of a list which is the attribute grades for a student
        completed = 0
        for subject in self._grades:
            done_credits = subject._credits
            completed += done_credits

        # First we plot a horizontal bar in red that has the length of the amount of credits needed
        plt.barh('progress', self._credits_needed, color="red", edgecolor="black", alpha=0.7)

        # We plot another bar on the first one but this one has the length of number of completed credits
        plt.barh('progress', completed, color="blue")

        # We set label for x-axis and title (in the title we show the progress in numbers)
        plt.xlabel('Credits')
        plt.title(f'ECTS: {int(completed)} / {self._credits_needed}')

        # Show the plot
        plt.savefig("progress_credits.png")
        return plt.gcf()

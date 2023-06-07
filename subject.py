# This class Subjects allows us to generate subjects as objects, what will allow us to work the subjects in a more efficient way
# Since we have almost no experience in coding we decided to code our classes from scratch to ensure that we have the best possible learning effect. This is the reason why we cannot provide any sources for this file
class Subject:
    def __init__(self, name, grade, credits, mandatory, semester):
        self._name = str(name)
        self._grade = float(grade)
        self._credits = float(credits)
        self._mandatory = bool(mandatory)
        self._semester = int(semester)

    # We implement getter and setter methods to ensure that the attributes of the objects are not modified from outside the class manually   
    def get_name(self):
        return self._name
   
    def get_grade(self):
        return self._grade

    def get_credits(self):
        return self._credits
    
    def is_mandatory(self):
        return self._mandatory
    
    def get_semester(self):
        return self._semester

    def set_name(self, name):
        self._name = str(name)

    def set_grade(self, grade):
        self._grade = float(grade)

    def set_credits(self, credits):
        self._credits = float(credits)

    def set_mandatory(self, mandatory):
        self._mandatory = bool(mandatory)

    def set_semester(self, semester):
        self._semester = int(semester)
        
    # We define a str() (string representation) method for display purposes
    def __str__(self):
        return f"This subject is called {self._name} and was completed with a {self._grade}"
    
    # We define a repr() (string representation) method that gives a overview over the object
    def __repr__(self):
        return f"Subject(name : {self._name}, grade : {self._grade}, credits : {self._credits}, mandatory : {self._mandatory}, semester: {self._semester})"
 

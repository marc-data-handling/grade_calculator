# In order to let people use our classes in a web application
# we tried to develop such an app with tha help of chatgpt, the documentation
# and https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
# To create the corresponding html files were again created with chatgpt
# and https://www.w3schools.com/html/html_intro.asp


from flask import Flask, render_template, request, redirect

from student import Student

app = Flask(__name__)
student = None

@app.route("/")
def index():
    # Render the index.html template
    return render_template("index.html")

@app.route("/create_student", methods=["GET", "POST"])
def create_student():
    # Handle GET request to render the create_student.html template
    if request.method == "GET":
        # Render the create_student.html template
        return render_template("create_student.html")

    # Handle POST request when the form is submitted
    if request.method == "POST":
        # Retrieve student name and credits needed from form data
        student_name = request.form["student_name"]
        credits_needed = int(request.form["credits_needed"])

        # Update the global student variable with a new Student instance
        # using the provided name and credits needed
        global student
        student = Student(student_name, credits_needed)

        # Redirect the user to the menu route
        return redirect("/menu")

@app.route("/menu")
def menu():
    # If student is not created, redirect to create_student route
    if student is None:
        return redirect("/create_student")

    # Render the menu.html template and pass the student object to it
    return render_template("menu.html", student=student)

@app.route("/add_subject", methods=["GET", "POST"])
def add_subject():
    # If student is not created, redirect to create_student route
    if student is None:
        return redirect("/create_student")

    # Handle GET request to render the add_subject.html template
    if request.method == "GET":
        # Render the add_subject.html template
        return render_template("add_subject.html")

    # Handle POST request when the form is submitted
    if request.method == "POST":
        # Retrieve subject information from form data
        name = request.form["name"]
        grade = float(request.form["grade"])
        credits = float(request.form["credits"])
        mandatory_input = request.form["mandatory"]
        mandatory = True if mandatory_input == "yes" else False
        semester = int(request.form["semester"])

        # Generate a subject using the student's generate_subject method
        student.generate_subject(name, grade, credits, mandatory, semester)

        # Redirect the user to the menu route
        return redirect("/menu")

@app.route("/delete_subject", methods=["GET", "POST"])
def delete_subject():
    # If student is not created, redirect to create_student route
    if student is None:
        return redirect("/create_student")

    # Handle GET request to render the delete_subject.html template
    if request.method == "GET":
        # Render the delete_subject.html template
        return render_template("delete_subject.html")

    # Handle POST request when the form is submitted
    if request.method == "POST":
        # Retrieve subject name to be deleted from form data
        name = request.form["name"]

        # Delete the subject using the student's delete_subject method
        student.delete_subject(name)

        # Redirect the user to the menu route
        return redirect("/menu")

@app.route("/calculate_gpa")
def calculate_gpa():
    # If student is not created, redirect to create_student route
    if student is None:
        return redirect("/create_student")

    # Calculate the GPA using the student's calculate_gpa method
    gpa = student.calculate_gpa()

    # Render the calculate_gpa.html template and pass the GPA value to it
    return render_template("calculate_gpa.html", gpa=gpa)

@app.route("/calculate_gpa_by_semester")
def calculate_gpa_by_semester():
    # If student is not created, redirect to create_student route
    if student is None:
        return redirect("/create_student")

    # Calculate the GPA by semester using the student's calculate_gpa_by_semester method
    gpa_by_semester = student.calculate_gpa_by_semester()

    # Render the calculate_gpa_by_semester.html template and pass the GPA by semester to it
    return render_template("calculate_gpa_by_semester.html", gpa_by_semester=gpa_by_semester)

if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)

''' Using form in html and retrieving the data in the form in python variables:

* The values from form are retrieved from the class request from module flask itself
* set the 'name' attribute of the tag form to some value eg:"abc"
* now use request.form['abc'] to get the value inputed in the form with name : "abc"
* also it should be inside the if condition ( if request.method == 'POST' )
* and the app route should have @app.route('/', methods=['GET', 'POST'])
'''


from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve the selected radio button value (student or course)
        id_type = request.form['ID']
        
        if id_type == 'student':
            # Retrieve the values for student ID and name
            student_id = request.form['student_id']
            student_name = request.form['student_name']
            
            # Print values (for demonstration purposes)
            print(f"Student ID: {student_id}, Student Name: {student_name}")
            
            # Redirect to the student details page (student_details.index) with the provided details
            return redirect(url_for('student_details', student_id=student_id, student_name=student_name))
        
        elif id_type == 'course':
            # Retrieve the values for course ID and name
            course_id = request.form['course_id']
            course_name = request.form['course_name']
            # Print values (for demonstration purposes)
            print(f"Course ID: {course_id}, Course Name: {course_name}")
            # Redirect to the course details page (course_details.index) with the provided details
            return redirect(url_for('course_details', course_id=course_id, course_name=course_name))
    
    # Render the index.html template for GET requests
    return render_template('index.html')
    
@app.route('/student/<student_id>/<student_name>')
def student_details(student_id, student_name):
    # This is where you would fetch and process student details based on student_id and student_name
    # For now, we just print the details to the console and render a template
    print(f"Student ID: {student_id}, Student Name: {student_name}")
    return render_template('student_details.html', student_id=student_id, student_name=student_name)

@app.route('/course/<course_id>/<course_name>')
def course_details(course_id, course_name):
    # This is where you would fetch and process course details based on course_id and course_name
    # For now, we just print the details to the console and render a template
    print(f"Course ID: {course_id}, Course Name: {course_name}")
    return render_template('course_details.html', course_id=course_id, course_name=course_name)

# Error handler for page not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message="Page not found."), 404

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
    

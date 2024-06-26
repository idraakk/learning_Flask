# Learning Flask and Jinja2

This repository contains various tutorial files that I used to learn Flask, Jinja2, and related technologies. Each tutorial is organized into separate files, and this README provides a comprehensive overview of the syntax, techniques, and methods covered in each tutorial.

## Tutorials Overview

### `tut 1-2.py`
**Learnings:**
- **Setting up a basic Flask application:**
  - Importing the Flask class from the flask module.
  - Initializing a Flask application object.
  - Defining routes using the `@app.route` decorator.
  - Running the Flask development server.
  
- **Flask Project Structure:**
  - Static folder to store project-related files.
  - Templates folder for HTML files.

- **Jinja Templating:**
  - Embedding static file paths directly in HTML using Jinja syntax.
  - Example: 
    ```html
    <img src="{{ url_for('static', filename='image1.jpg') }}">
    ```

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask and Idraak"

@app.route("/idraak")
def idraak():
    return "Hello Idraak's page"

app.run(debug=True)
```

### `tut 3.py`

**Learnings:**
- **Using Templates with Jinja2:**
  - Creating HTML templates and storing them in the templates folder.
  - Rendering templates using `render_template`.
  - Passing dynamic data to templates.

- **Jinja2 Syntax:**
  - Embedding Python-like expressions in HTML.
  - Using control structures like loops and conditionals within templates.

**Code Example:**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/user/<name>")
def user(name):
    return render_template('user.html', username=name)

if __name__ == "__main__":
    app.run(debug=True)
```

### `tut 4-5.py`

**Learnings:**
- **Handling Form Data in Flask:**
  - Using `request` objects to retrieve form data.
  - Validating form data.
  - Redirecting users and flashing messages for feedback.

- **Form Handling Techniques:**
  - GET and POST methods.
  - Accessing form data using `request.form`.

**Code Example:**
```python
from flask import Flask, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    if name:
        flash(f'Successfully submitted name: {name}')
        return redirect(url_for('index'))
    else:
        flash('Name is required!')
        return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
```

### tut 6.html

Learnings:

-   Creating HTML Forms:

-   Integrating forms with Flask routes.

-   Submitting form data to Flask routes.

-   Handling form submissions with POST method.

Code Example:

html

Copy code

<!DOCTYPE html>

<html>

<head>

    <title>Form Example</title>

</head>

<body>

    <form action="/submit" method="post">

        <label for="name">Name:</label>

        <input type="text" id="name" name="name" required>

        <button type="submit">Submit</button>

    </form>

</body>

</html>

### jinja2_week3sreencast.py

Learnings:

-   Advanced Jinja2 Templating:

-   Using control structures like loops and conditionals in templates.

-   Template inheritance and layout templates.

-   Example:

-   Creating a base template and extending it in other templates.

-   Using for loops and if conditions within templates.

Code Example:

python

Copy code

from jinja2 import Template

template = Template('''

{% for item in items %}

  {% if item.active %}

    <p>{{ item.name }}</p>

  {% endif %}

{% endfor %}

''')

items = [{'name': 'Item 1', 'active': True}, {'name': 'Item 2', 'active': False}]

print(template.render(items=items))

### csv_to_dictionary.py

Learnings:

-   Reading CSV Files in Python:

-   Using the csv module to read CSV files.

-   Converting CSV data to dictionaries.

-   Using CSV data in Flask applications.

Code Example:

python

Copy code

import csv

def csv_to_dict(filename):

    with open(filename, mode='r') as file:

        csv_reader = csv.DictReader(file)

        return [row for row in csv_reader]

data = csv_to_dict('data.csv')

print(data)

### HTMLForms-ConnectingFlask/

Learnings:

-   Building a Complete Flask Application:

-   Multiple routes and templates.

-   Organizing templates in a Flask application.

-   Handling different types of form data (e.g., text, dropdowns, checkboxes).

-   Using Jinja2 templates to create dynamic HTML content.

app.py:

-   Learnings:

-   Setting up a Flask application with multiple routes.

-   Handling form submissions and rendering different templates based on routes.

Code Example:

python

Copy code

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():

    if request.method == "POST":

        if request.form["ID"] == "student":

            student_id = request.form["student_id"]

            student_name = request.form["student_name"]

            return render_template("student_details.html", student_id=student_id, student_name=student_name)

        elif request.form["ID"] == "course":

            course_id = request.form["course_id"]

            course_name = request.form["course_name"]

            return render_template("course_details.html", course_id=course_id, course_name=course_name)

    return render_template("index.html")

if __name__ == "__main__":

    app.run(debug=True)

templates/index.html:

-   Learnings:

-   Creating the main page with forms for student and course details.

Code Example:

html

Copy code

<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <title>Index Page</title>

</head>

<body>

    <h1>Select ID and Enter Details</h1>

    <!-- Form for Student ID and Name -->

    <form method="POST" action="/" id="student-form">

        <input type="radio" name="ID" value="student" required/>

        <label>Student ID</label>

        <input type="text" name="student_id" placeholder="Enter Student ID" required/>

        <input type="text" name="student_name" placeholder="Enter Student Name" required/>

        <input type="submit" value="Submit"/>

    </form>

    <!-- Form for Course ID and Name -->

    <form method="POST" action="/" id="course-form">

        <input type="radio" name="ID" value="course" required/>

        <label>Course ID </label>

        <input type="text" name="course_id" placeholder="Enter Course ID" required/>

        <input type="text" name="course_name" placeholder="Enter Course Name" required/>

        <input type="submit" value="Submit"/>

    </form>

</body>

</html>

templates/course_details.html:

-   Learnings:

-   Displaying course details dynamically based on form input.

Code Example:

html

Copy code

<html>

    <h1> {{course_id}} and {{course_name}} </h1>

</html>

templates/student_details.html:

-   Learnings:

-   Displaying student details dynamically based on form input.

Code Example:

html

Copy code

<html>

    <h1> {{student_id}} and {{student_name}} </h1>

</html>

How to Run the Code
-------------------

Clone the repository:\
sh\
Copy code\
git clone https://github.com/yourusername/learning_Flask.git

cd learning_Flask

1.

Create a virtual environment and install dependencies:\
sh\
Copy code\
python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

1.

Run the Flask application:\
sh\
Copy code\
export FLASK_APP=app.py  # On Windows use `set FLASK_APP=app.py`

flask run

1.

2.  Open your web browser and go to http://127.0.0.1:5000 to see the application in action.

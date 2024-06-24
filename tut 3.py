'''
* Showed using Templates and jinja templating within flask
'''

from flask import Flask, render_template #render_template to do templating in flask

app = Flask(__name__)

@app.route("/")
def Hello():
    return render_template("index.html") #Tempalting

@app.route("/about")
def idraak():
    return render_template("about.html", name="IDRAAK") #JINJA2 Templating

app.run(debug=True)

'''
index.html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Title</title>
</head>
<body>
  <h1>Hello index.html</h1>
  <h2>Created a flask app using templates. Used render_template function from the flask module</h2>
</body>
</html>
'''

'''
about.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About</title>
</head>
<body>
    <h1>Flask has inbuilt jinja2 templating</h1>
    <h2>See this will say my name {{name}}</h2>
</body>
</html>
'''


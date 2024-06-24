'''
* Jinja templating in Flask allows user to use static folder path directly in html (which cream html doesn't allow)
  Eg: keep the image.jpg in static folder
  - <img src="static/image1.jpg>
    or better as
  - <img src=" {{url_for('static' , filename='image1.jpg') }} ">

* We can also run for loops in jinja templating
'''

# content of index.html file
index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About</title>
</head>
<body>
    <h1>Flask has inbuilt jinja2 templating</h1>
    {% for user in users %}
    <h2>See this will say my name {{user[0]}} and {{user[1]}} </h2>
    {% endfor %}
</body>
</html>

#content of main.py

from flask import Flask, render_template

app = Flask(__name__)
@app.route("/a")
                 
def idraak():
    list=[ ["idraak","khan"] , ["suresh","singh"] , ["rajesh","yadav"] ]
    return render_template("about.html", users=list)

app.run(debug=True)



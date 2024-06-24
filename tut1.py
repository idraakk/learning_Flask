'''
* Basic demonstration of running a flask app on local host.
* The Flask projects have two folders - static(to store project related files and templates(for all html files)
'''
from flask import Flask #import Flask class from flask module

app = Flask(__name__) #define app

#set end point for the following function
#will deploy the following function on 127.0.0.1:5000
@app.route("/")
def Hello():
    return ("Hello flask and Idraak")


#to deplow on 127.0.0.1:5000/idraak
@app.route("/idraak")
def idraak():
    return ("Hello idraak's page")

app.run(debug=True) #to run the flask app and debug=True to enable debug support


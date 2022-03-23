# include Flask class from file flask
from flask import Flask

# create an instance of Flask class
# __name__ is a predefined setup variable
myapp_obj = Flask(__name__)


# different URL the app will implement
@myapp_obj.route("/")
# called view function
def home():
    name = {'username': 'Bao'}
    city_name = 'San Jose, San Diego, San Francisco'
    return '''
<html>
    <head>
        <title>Home Page - my blog</title>
    </head>
    <body>
        <h1>Welcome, ''' + name + ['username'] + '''!</h1>

        <a href="google.com/"< Not Google</a>

        <ol>
            <li>''' + city_name[0] + '''</li>
            <li>''' + city_name[1] + '''</li>
            <li>''' + city_name[2] + '''</li>
        </ol>
    <p>City name </p>
    <input type = "text" maxlength=<"32">
    <br><br>
    <button type ="button">Submit</button>

    </body>
    </html>'''


myapp_obj.run()
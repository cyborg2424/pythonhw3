# include Flask class from file flask
from flask import Flask

# create an instance of Flask class
# __name__ is a predefined setup variable
myapp_obj = Flask(__name__)


# different URL the app will implement
@myapp_obj.route("/")
# called view function
def home():
    name = 'Bao'
    city_names = 'San Jose, San Diego, San Francisco'
    return '''
<html>
    <head>
        <title>Home Page - my blog</title>
    </head>
    <body>
        <h1>Welcome, ''' + name + '''!</h1>
        <a href="www.google.com/">not google!</a>
        <ol>
            <li>''' + city_names[0] + city_names[1] + city_names[2] + city_names[3] + city_names [4] + city_names[5] + city_names[6] + city_names[7] + '''</li>
            <li>''' + city_names[9] + city_names[10] + city_names[11] + city_names[12] + city_names [13] + city_names[14] + city_names[15] + city_names[16] + city_names[17] + city_names[18] +'''</li>
            <li>''' + city_names[20] + city_names[21] + city_names[22] + city_names[23] + city_names [24] + city_names[25] + city_names[26] + city_names[27] + city_names[28] + city_names[29] + city_names[30]+city_names[31]+city_names[32]+city_names[33]+'''</li>
        </ol>

    <p>City name </p>
    <input type = "text" maxlength=<"32">
    <br><br>
    <button type ="button">Submit</button>

    </body>
    </html>'''


myapp_obj.run()
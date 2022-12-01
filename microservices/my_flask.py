# flask is a library provided by Python which enables a simple web server
# a web server (microservice) can handle web content - i.e. html pages

# we may need to pip install Flask (it is not part of the default Python install)
from flask import Flask
from flask import render_template # lets us use html web pages
import requests

# in this case we will
# - explore flask architecture
# - implement 4-5 web content routes

app = Flask(__name__)
# we declare one or more routes for our app
# NB remember every 'route' is using 'get'
# see https://pythonbasics.org/flask-http-methods/ about post, put, delete etc.
@app.route('/') # root or our web service
def root():
    return 'Hello welcome to our Flask web server running on localhost port 5000'

@app.route('/home') # we can invent any text for our routes
def home():
    content = '''
    <h2>Flask Home Content</h2>
    '''
    # we could make a request to some other API
    # r = requests.get('some.com/data')
    # then when we get the data fro mthat API
    #send it back to our client
    return content

@app.route('/about')
def about():
    content = ('''
    Visit the root <a href='http://localhost:5000'>Home</a>
    ''')
    return content

# we can pass data as web content
@app.route('/data')
def data():
    # we can pass ANY structure 
    struct = {"name":"Deidre", "age":42, "member":True}
    return struct # Flask will parse the structure into JSON

@app.route('/greet') # we can have several routes all using the same function
@app.route('/greet/<name>') # here we expect a parameter to be added to the URL
def greet(name='Grommit'):
    # return f'Hello {name}'
    return render_template('greet.html', name=name)


if __name__ == '__main__':
    app.run() # this starts our flask web server

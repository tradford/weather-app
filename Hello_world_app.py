from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello World';

@app.route("/goodbye")
def goodbye():
    return 'goodbye World!';  

@app.route("/hello/<name>/<int:age>")#decorator for url that is dynamic
#you must have as many generic decorators as you do string formats
#but you can have as many as you would like
def hello_name(name, age):
    return "Hello, {}. You are {} years old".format(name, age); 

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port=port, debug=True)
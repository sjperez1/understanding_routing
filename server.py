from flask import Flask
app = Flask(__name__)

@app.route('/')
def say_hello_world():
    return "Hello World!"

# Use print when things should show up just in terminal and use return when things should display on the webpage.
@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:title>')
def hi_name(title):
    return "Hi " + title + "!"

@app.route('/<int:number>/<string:word>')
def multiply(number, word):
    return word * number

if __name__=="__main__":
    app.run(debug=True)
# The following is not correct
else:
    print("Sorry! No response. Try again.")
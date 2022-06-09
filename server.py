from flask import Flask
app = Flask(__name__)

@app.route('/')
def say_hello_world():
    return "Hello World!"

# For the functions, how do you know when to use print vs return in these?
@app.route('/dojo')
def dojo():
    return "Dojo!"

# is adding string:  what it meant when saying to make sure the names are strings in the bonus?
@app.route('/say/<string:title>')
def hi_name(title):
    return "Hi " + title + "!"

# is this what it meant in the bonus by saying make sure one is an integer and one is a string?
@app.route('/<int:number>/<string:word>')
def multiply(number, word):
    return word * number

# When is the following if line needed? Is this how you add that very last else statement?
if __name__=="__main__":
    app.run(debug=True)
else:
    print("Sorry! No response. Try again.")
from flask import Flask
app = Flask(__name__)

@app.route('/')
def say_hello_world():
    return "Hello World!"

# For the functions, how do you know when to use print vs return in these?
# When is the following if line needed?
if __name__=="__main__":
    @app.route('/dojo')
    def dojo():
        return "Dojo!"

    @app.route('/say/<title>')
    def hi_name(title):
        return "Hi " + title + "!"

    @app.route('/<int:number>/<string:word>')
    def multiply(number, word):
        return word * number

    app.run(debug=True)
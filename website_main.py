from flask import Flask
from flask import send_file
from flask import request
from flask import render_template
import socket

local_ip = socket.gethostbyname(socket.gethostname())

# app = Flask(__name__)
app = Flask(__name__, static_folder="C:/Users/2005s/Documents/Visual Studio Code/Flask, HTML, CSS, JS/Sooraj-Website/static")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/')
def main():
    return send_file("templates/mainpage.html")

@app.route('/examplepage')
def page2():
    return ("<h1>This is an example page!</h1>")

@app.route('/number-adder')
def number_adder():
    return send_file("templates/numberadder.html")

@app.route('/number-adder/answer', methods=["post"])
def number_adder_answer():
    num1 = request.form["number1"]
    num2 = request.form["number2"]
    # if num1.isnumeric() and num2.isnumeric():
    try:
        num1 = int(num1)
        num2 = int(num2)
        total = num1 + num2
        return send_file("templates/numberadderresult.html")
    # else:
    except:
        total = "One or both of the inputs are not a number!"
        return f"Sorry! {total}"

if __name__ == '__main__':
    app.run(host=f"{local_ip}", port=8080, debug=True)
    # app.run(host='localhost', port=8080, debug=True)

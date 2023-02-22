from flask import Flask, request, jsonify
import tools.sql_queries as sql
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/multiply/<num1>/<num2>")
def speak(num1,num2):
    result=int(num1)*int(num2)
    return f"{num1} times {num2} is {result}"

@app.route("/random-number")
def random_int():
    return str(random.randint(0, 10))

@app.route("/everything-employees")
def example ():
    return jsonify(sql.get_everything())

@app.route("/table/<one_table>")
def query_table (one_table):
    return jsonify(sql.table_ten(one_table))

@app.route("/insert-into-employees", methods = ["POST"])
def insert_into_employees ():

    my_params = request.args

    sql.insert_params(my_params)
    return "Inserted!"



if __name__ == "__main__":
    app.run(port=7070, debug=True)

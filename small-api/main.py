from flask import Flask, jsonify, request
import random
import tools.sql_queries as sqll

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/random-number")
def random_number ():
    return str(random.randint(0, 10))

@app.route("/everything-employees")
def example ():
    return jsonify(sqll.get_everything())

@app.route("/table/<one_table>")
def tabletable (one_table):
    return jsonify(sqll.table_ten(one_table))

@app.route("/insert-into-employees", methods = ["POST"])
def insert ():
    my_params=request.args
    a=my_params["emp_no"]
    b=my_params["birth_date"]
    c=my_params["first_name"]
    d=my_params["last_name"]
    e=my_params["gender"]
    f=my_params["hire_date"]
    sqll.insert_into_emp(a,b,c,d,e,f)
    return "Success"


@app.route("/higher/<dollars>")
def money (dollars):
    return jsonify(sqll.money(dollars))

if __name__ == "__main__":
     app.run(port=7070, debug=True)

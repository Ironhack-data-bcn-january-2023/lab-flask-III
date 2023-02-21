import requests
import random
from flask import Flask, request, jsonify
import tools.sql_queries as sql
from config.sql_connection import engine

app = Flask(__name__)
@app.route("/")
def hello_world():
    return f"Hello world!"

@app.route("/random")
def random_int():
    return str(random.randint(0, 10))

@app.route("/everything-employees")
def example ():
    return jsonify(sql.get_everything())

@app.route("/table/<table>")
def table_ten (table):
    return jsonify(sql.table_ten(table))

@app.route("/insert-into-employees", methods=['POST'])
def insert_1():
    emp_no = request.args['emp_no']
    birth_date = request.args['birth_date']
    first_name =request.args['first_name']
    last_name =request.args ['last_name']
    gender =request.args ['gender']
    hire_date = request.args['hire_date']
    sql.insert_one(emp_no, birth_date, first_name, last_name, gender, hire_date)
    return "Inserted!"

@app.route("/insert-into-departments", methods=['POST'])
def insert_dept():
    dept_no = request.args['dept_no']
    dept_name = request.args['dept_name']
    sql.insert_dpment(dept_no, dept_name)
    return "Inserted!"

if __name__ == "__main__":
    app.run(port=7070, debug=True)



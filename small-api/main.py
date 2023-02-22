from flask import Flask, request, jsonify
import random
import config.sql_connection as engine
import tools.sql_queries as sql

app = Flask(__name__)
@app.route("/", methods=["GET"])
def hello_this_works ():
    return f"Hello world!"

@app.route("/random-number", methods=["GET"])
def random_no():
    return str(random.randint(0,10))

@app.route("/everything-employees", methods=["GET"])
def example():
    return jsonify(sql.get_everything())

@app.route("/table/<tbl>", methods = ['GET'])
def table_ten(tbl):
    return jsonify(sql.tbl_tn(tbl))

@app.route("/insert-into-employees", methods=['POST'])
def insert_params_():
    emp_no = request.args['emp_no']
    birth_date = request.args['birth_date']
    first_name =request.args['first_name']
    last_name =request.args ['last_name']
    gender =request.args ['gender']
    hire_date = request.args['hire_date']

    sql.insert_params (emp_no, birth_date, first_name, last_name, gender, hire_date)
    return "Inserted!"

@app.route("/insert-departments", methods = ["POST"])
def department_():
    dept_no= request.args['dept_no']
    dept_name=request.args['dept_name']
    sql.insert_dept(dept_no, dept_name)
    return 'Inserted'

if __name__ == "__main__":
    app.run(port=9000, debug=True)
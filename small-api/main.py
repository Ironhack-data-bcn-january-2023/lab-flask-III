from flask import Flask, request, jsonify
import random
from tools import sql_queries as sql

app = Flask (__name__)


@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/random-number")
def random_int():
    return str(random.randint(0,10))


@app.route("/everything-employees")
def example ():
    return jsonify(sql.get_everything_table())

@app.route("/table/<one_table>")
def get_one_table (one_table):
    return jsonify(sql.table_ten(one_table))

@app.route("/insert-into-employees-table", methods=["POST"])
def insert_by_passing_params ():
  
    id_ = request.args["id"]
    date = request.args["date"]
    name = request.args["name"] 
    fname = request.args["fname"]
    gender = request.args["gender"] 
    date_2 = request.args["date_2"] 

    sql.insert_params (id_, date, name, fname, gender, date_2)
    return "ok"

@app.route("/insert-into-<table>", methods=["POST"])
def insert_by_passing_params_to_table (table):
    dict_ = request.args
    sql.insert_params_to_table (table, dict_)
    return "ok"

if __name__ == '__main__':
    app.run(port=9000, debug=True)
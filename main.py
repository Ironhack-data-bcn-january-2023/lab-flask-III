from flask import Flask
from flask import jsonify
from flask import request

import sys
sys.path.append(r"small_api")

import random
import small_api.tools.sql_queries as sql

app = Flask(__name__)


@app.route("/hello-world")
def hello ():
    return f"Hello world!"


@app.route("/random/<therange>")
def random_number (therange):
    therange = int(therange)
    return str(random.randint(0, therange))


@app.route("/table/everything-employees")
def get_everything_table ():
    return jsonify(sql.get_everything_table())

@app.route("/table/<one_table>")
def table_ten (table_q):
    return jsonify(sql.table_ten(table_q))



@app.route("/insert-into-employees", methods = ["POST"])
def insert_into_employees ():
    my_params = request.args
    sql.insert_params(my_params)
    return "Inserted!"

app.run(port=51814 , debug=True)
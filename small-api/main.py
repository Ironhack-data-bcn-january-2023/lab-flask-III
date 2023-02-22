
from flask import Flask, request, jsonify
import random
import sql_queries as esql

# your code here
app = Flask(__name__)

@app.route("/")
def hello_world ():
    return f"Hello World"

@app.route("/random-number")
def random_int():
     return str(random.randint(0, 10))

@app.route("/everything.employees")
def example():
     data = esql.get_everything_()
     response = jsonify(data=data, orient='records')
     return response

from sql_queries import table_ten


@app.route('/table/<one_table>')
def select_ten(one_table):
    # call the table_ten function to select 10 rows from the specified table
    data = table_ten(one_table)
    
    # stringify the dataframe and return the result as a JSON response
    response = jsonify(data=data, orient='records')
    
    return response

@app.route("/insert-into-employees", methods = ["POST"])
def insert_into_employees ():

     my_params = request.args
     esql.insert_params(my_params)
     return "Inserted!"

if __name__ == "__main__":
     app.run(port=81814, debug= True)
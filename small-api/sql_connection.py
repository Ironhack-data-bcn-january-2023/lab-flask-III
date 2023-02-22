import sqlalchemy as alch
import os 
from dotenv import load_dotenv
import pandas as pd

# Loading env variables
load_dotenv()
password = os.getenv("sql_pass")

# Connection to database
dbName = "employees"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)

# def insert_params (my_params):
#     query = f"""
#         REPLACE INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date)
#         VALUES ("{my_params['emp_no']}", "{my_params['birth_date']}", "{my_params['first_name']}", "{my_params['last_name']}", "{my_params['gender']}", "{my_params['hire_date']}")
#         ;
#         """
#     engine.execute(query)
#     return "Done"

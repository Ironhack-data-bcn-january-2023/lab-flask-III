import pandas as pd

import sys
sys.path.append(r"small_api")
from config.sql_connection import engine



def get_everything_table ():
    query = f"SELECT * FROM salaries LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def table_ten (table_q):
    query = f"SELECT * FROM {table_q} LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def insert_params (my_params):
    query = f"""
        REPLACE INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date)
        VALUES ("{my_params['emp_no']}", "{my_params['birth_date']}", "{my_params['first_name']}", "{my_params['last_name']}", "{my_params['gender']}", "{my_params['hire_date']}")
        ;
        """
    engine.execute(query)
    return "Done"


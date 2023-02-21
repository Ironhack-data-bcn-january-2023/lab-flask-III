import pandas as pd
from tools.sql_connection import engine


def get_everything ():
    query = f"SELECT * FROM salaries LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def table_ten (table):
    query = f"SELECT * FROM  {table} LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def insert_into_emp(a,b,c,d,e,f):
    query = f"""INSERT INTO employees 
    (emp_no, birth_date, first_name, last_name, gender, hire_date) VALUES ('{a}','{b}','{c}','{d}','{e}','{f}');
    """

def money(dollars):
    query = f'''SELECT count(salary) FROM Salaries
    WHERE salary>{dollars};'''
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")



    engine.execute(query)
    return 
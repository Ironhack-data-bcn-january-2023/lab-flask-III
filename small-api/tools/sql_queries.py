from config.sql_connection import engine
import pandas as pd

def get_everything ():
    query = '''
    SELECT *
        from salaries
        LIMIT 10;
    '''
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def table_ten (one_table):
    query = f'''
    SELECT *
        from {one_table}
        LIMIT 10;
    '''
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient='records')

def argument_receiver (**kwargs):
    params = {}
    for key, value in kwargs.items():
        params[key] = value
    return params

def insert_params (emp_no, birth_date, first_name, last_name, gender, hire_date):
    query = f"""
    INSERT INTO employees
    VALUES ("{emp_no}", "{birth_date}", "{first_name}", "{last_name}", "{gender}", "{hire_date}");
    """
    engine.execute(query)


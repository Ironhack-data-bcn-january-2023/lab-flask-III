import pandas as pd
from config.sql_connection import engine

# request queries

def get_everything_table ():
    query = f"SELECT * FROM  salaries LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def table_ten (table_q):
    query = f"SELECT * FROM  {table_q} LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


# post queries 

def insert_params (id_, date, name, fname, gender, date_2):
    query = f"""
    INSERT INTO employees
    VALUES ("{id_}", "{date}", "{name}", "{fname}", "{gender}", "{date_2}");
    """
    engine.execute(query)

def insert_params_to_table (table, dict_):
    columns = ", ".join(list(dict_.keys()))
    values = "', '".join(list(dict_.values()))
    query = f"""
            INSERT INTO {table}
                ({columns})
                VALUES ('{values}')
                """
    engine.execute(query)
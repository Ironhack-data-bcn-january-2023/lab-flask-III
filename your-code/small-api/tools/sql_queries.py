from config.sql_connection import engine
from flask import Flask, jsonify, request
import random
import tools.sql_queries as sql
import sqlalchemy as alch
import os 
from dotenv import load_dotenv
import pandas as pd

def get_everything ():
    query = "SELECT * FROM salaries LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def table_ten(table):
    query = f"SELECT * FROM {table} LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def insert_one (emp_no, birth_date, first_name, last_name, gender, hire_date):
    query = f"""
    INSERT INTO employees
        VALUES (
            "{emp_no}", "{birth_date}", "{first_name}", "{last_name}", "{gender}", "{hire_date}");
    """
    engine.execute(query)

def insert_dpment (dept_no, dept_name):
    query = f"""
    INSERT INTO departments
        VALUES (
            "{dept_no}", "{dept_name}");
    """
    engine.execute(query)
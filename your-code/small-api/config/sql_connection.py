from flask import Flask, jsonify, request
import random
import tools.sql_queries as sql
import sqlalchemy as alch
import os 
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
password = os.getenv("password_sql")

dbName = "employees"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)


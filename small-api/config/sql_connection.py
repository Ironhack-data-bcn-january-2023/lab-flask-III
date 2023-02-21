import sqlalchemy as alch
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
token = os.getenv('password')

db = "employees"
connectionData=f"mysql+pymysql://root:{token}@localhost/{db}"
engine = alch.create_engine(connectionData)
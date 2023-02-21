import sqlalchemy 
import os 
from dotenv import load_dotenv


# Loading env variables
load_dotenv()
password = os.getenv("password")

# Connection to database
dbName = "employees"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = sqlalchemy.create_engine(connectionData)
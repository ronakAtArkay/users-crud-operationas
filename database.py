from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote


sqlalchemy_database_url = "mysql+mysqlconnector://root:%s@localhost:3306/demo_db"%quote("Arkay@210")

engine = create_engine(sqlalchemy_database_url)

sessionLocal = sessionmaker(autocommit= False, autoflush= False, bind=engine)

Base = declarative_base()
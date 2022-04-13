import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import pymysql

load_dotenv("./config/.env")


pymysql.install_as_MySQLdb()


DATABASE_URL = f"mysql://{os.getenv('DB_LOCAL_USER')}:{os.getenv('DB_LOCAL_PASSWORD')}@{os.getenv('DB_LOCAL_HOST')}/{os.getenv('DB_LOCAL_NAME')}"

SQLALCHEMY_DATABASE_URL = DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

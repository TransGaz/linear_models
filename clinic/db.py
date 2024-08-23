from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, declarative_base
import psycopg2

import config


connection_string = config.bd_key
engine = create_engine(connection_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
import os
import sys
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class LocalUser(Base):
	__tablename__='local_users'
	id=Column(Integer, primary_key=True, autoincrement=True)
	first_name=Column(String(250), nullable=False)
	last_name=Column(String(250), nullable=False)
	email=Column(String(250), nullable=False)
	password=Column(String, nullable=False)
	created=Column(String, nullable=False)

engine=create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)
	
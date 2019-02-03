from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user_database_setup import Base, LocalUser

engine=create_engine('sqlite:///users.db')
Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)

def get_user(r_email):
	session=DBSession()
	q=session.query(LocalUser).filter(r_email == LocalUser.email).first()
	session.close()
	if q:
		resulted_user=LocalUser(id=q.id, first_name=q.first_name, last_name=q.last_name, email=q.email, password=q.password, created=q.created)
		return resulted_user
	else:
		return None

def if_user_exists(r_email):
	session=DBSession()
	q=session.query(LocalUser).filter(r_email == LocalUser.email).first()
	session.close()
	if q is None:
		return False
	else:
		return True

def add_user(new_user):
	try:
		session=DBSession()
		session.add(new_user)
		session.flush()
		session.commit()
		session.close()
		return True
	except SQLAlchemyError as e:
		return False

def get_user(r_email):
	session=DBSession()
	q=session.query(LocalUser).filter(r_email == LocalUser.email).first()
	session.close()

	if q:
		result=LocalUser(id=q.id, first_name=q.first_name, last_name=q.last_name, email=q.email, password=q.password, created=q.created)
		return result
	else:
		return None
#Amin Esfandiyari
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a base class for our database models
Base = declarative_base()

# Define a model for a user table
class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))
    email = sa.Column(sa.String(255), unique=True)

# Establish a connection to the database
engine = sa.create_engine('sqlite:///elmofarhang.db')

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a sessionmaker to manage database transactions
SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()

while True:
    print('1- insert')
    print('2- update')
    print('3- delete')
    print('4- view')
    print('5-exit')
    try:
        n=int(input("enter 1,2,3,4 or 5: "))
        if n == 1:
            name = input("please enter the name: ")
            email = input("please enter the email: ")
            new_user = User(name=name, email=email)
            session.add(new_user)
            session.commit()
        elif n == 2:
            id = int(input("please enter the user id: "))
            new_name = input("please enter the new name for the user: ")
            new_email = input("please enter the new email for the user: ")
            user_to_update = session.get(User, id)
            user_to_update.name = new_name
            user_to_update.email = new_email
            session.commit()
        elif n == 3:
            del_id = int(input("please enter the user id: "))
            user_to_delete = session.get(User, del_id)
            session.delete(user_to_delete)
            session.commit()
        elif n == 4:
            users = session.query(User).all()
            for user in users:
                print(f"Userid={user.id}, Username={user.name}, Email={user.email}")
        elif n == 5:
            print("Good Bye!")
            break
    except:
        print("Bad input! Try again")

session.close()
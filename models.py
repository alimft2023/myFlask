import sqlalchemy as sa 
from sqlalchemy.orm import declarative_base ,sessionmaker

Base=declarative_base()

class Student(Base):
    __tablename__='Student'
    id=sa.Column(sa.Integer,primary_key=True)
    name = sa.Column(sa.String(255))
    email = sa.Column(sa.String(255)) 
    
engine = sa.create_engine('sqlite:///school.db')
    
Base.metadata.create_all(engine)
SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()

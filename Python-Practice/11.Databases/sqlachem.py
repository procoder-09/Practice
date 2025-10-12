from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create SQLite database
engine = create_engine("sqlite:///employees.db", echo=True)

# Base class for models
Base = declarative_base()

# Session
Session = sessionmaker(bind=engine)
session = Session()

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)

# Create table
Base.metadata.create_all(engine)

emp1 = Employee(name="Alice", position="Manager")
emp2 = Employee(name="Bob", position="Developer")
emp3 =Employee(name="Amma",position="engineer")

session.add(emp1)
session.add(emp2)
session.add(emp3)
session.commit()

employees = session.query(Employee).all()
for emp in employees:
    print(emp.id, emp.name, emp.position)

# Filter
devs = session.query(Employee).filter_by(position="Developer").all()
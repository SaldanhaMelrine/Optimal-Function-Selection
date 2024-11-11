from sqlalchemy import create_engine, Column, Integer, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# SQLite database connection
DATABASE_URL = "sqlite:///C:/Users/dell/Desktop/M.Sc. Data Science/Programming wih Python/Ideal Function Selection/ideal-function-selector/ideal_function_selector.db"
engine = create_engine(DATABASE_URL, echo=True)

# Base class 
Base = declarative_base()

# Table for the training data
class TrainingData(Base):
    __tablename__ = 'training_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    x = Column(Float, nullable=False)
    y1 = Column(Float, nullable=False)
    y2 = Column(Float, nullable=False)
    y3 = Column(Float, nullable=False)
    y4 = Column(Float, nullable=False)

# Table for the ideal functions
class IdealFunctions(Base):
    __tablename__ = 'ideal_functions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    x = Column(Float, nullable=False)
    y1 = Column(Float, nullable=False)
    y2 = Column(Float, nullable=False)
    y3 = Column(Float, nullable=False)
    y4 = Column(Float, nullable=False)
    y5 = Column(Float, nullable=False)
    y6 = Column(Float, nullable=False)
    y7 = Column(Float, nullable=False)
    y8 = Column(Float, nullable=False)
    y9 = Column(Float, nullable=False)
    y10 = Column(Float, nullable=False)
    y11 = Column(Float, nullable=False)
    y12 = Column(Float, nullable=False)
    y13 = Column(Float, nullable=False)
    y14 = Column(Float, nullable=False)
    y15 = Column(Float, nullable=False)
    y16 = Column(Float, nullable=False)
    y17 = Column(Float, nullable=False)
    y18 = Column(Float, nullable=False)
    y19 = Column(Float, nullable=False)
    y20 = Column(Float, nullable=False)
    y21 = Column(Float, nullable=False)
    y22 = Column(Float, nullable=False)
    y23 = Column(Float, nullable=False)
    y24 = Column(Float, nullable=False)
    y25 = Column(Float, nullable=False)
    y26 = Column(Float, nullable=False)
    y27 = Column(Float, nullable=False)
    y28 = Column(Float, nullable=False)
    y29 = Column(Float, nullable=False)
    y30 = Column(Float, nullable=False)
    y31 = Column(Float, nullable=False)
    y32 = Column(Float, nullable=False)
    y33 = Column(Float, nullable=False)
    y34 = Column(Float, nullable=False)
    y35 = Column(Float, nullable=False)
    y36 = Column(Float, nullable=False)
    y37 = Column(Float, nullable=False)
    y38 = Column(Float, nullable=False)
    y39 = Column(Float, nullable=False)
    y40 = Column(Float, nullable=False)
    y41 = Column(Float, nullable=False)
    y42 = Column(Float, nullable=False)
    y43 = Column(Float, nullable=False)
    y44 = Column(Float, nullable=False)
    y45 = Column(Float, nullable=False)
    y46 = Column(Float, nullable=False)
    y47 = Column(Float, nullable=False)
    y48 = Column(Float, nullable=False)
    y49 = Column(Float, nullable=False)
    y50 = Column(Float, nullable=False)

# Table for the test data
class TestDataModel(Base):
    __tablename__ = 'test_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    ideal_function_id = Column(Integer, ForeignKey('ideal_functions.id'))  
    deviation = Column(Float)  

# Table for Mapped Test Data
class MappedTestData(Base):
    __tablename__ = 'mapped_test_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    ideal_function_id = Column(Integer, ForeignKey('ideal_functions.id'))
    deviation = Column(Float, nullable=False)

    # Relationship to link mapped test data to ideal functions
    ideal_function = relationship("IdealFunctions", backref="mapped_test_data")

# Create all tables in the database
Base.metadata.create_all(engine)

# Set up the session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

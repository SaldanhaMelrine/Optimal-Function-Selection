import pytest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import Base, TrainingData, IdealFunctions, TestDataModel
from src.data_loader import load_training_data, load_ideal_functions, load_test_data

# Temporary SQLite database for testing
TEST_DATABASE_URL = "sqlite:///./test_database.db"
engine = create_engine(TEST_DATABASE_URL)
Session = sessionmaker(bind=engine)

@pytest.fixture(scope="module")
def setup_database():
    """Create tables and provide a session for tests."""
    # Create all tables
    Base.metadata.create_all(engine)
    session = Session()
    yield session  # Provide the session to tests
    session.close()
    # Drop all tables after tests
    Base.metadata.drop_all(engine)
    # Remove the test database file after closing all connections
    engine.dispose()  # Ensures all connections are closed
    try:
        os.remove("test_database.db")
    except PermissionError:
        print("Could not delete the database file; it may be open in another process.")


def test_load_training_data(setup_database):
    """Test loading training data into the database."""
    session = setup_database
    load_training_data(session, "C:/Users/dell/Desktop/M.Sc. Data Science/Programming wih Python/Ideal Function Selection/ideal-function-selector/data/train.csv")  

    training_data_count = session.query(TrainingData).count()
    assert training_data_count > 0, "Training data was not loaded correctly."

def test_load_ideal_functions(setup_database):
    """Test loading ideal functions data into the database."""
    session = setup_database
    load_ideal_functions(session, "C:/Users/dell/Desktop/M.Sc. Data Science/Programming wih Python/Ideal Function Selection/ideal-function-selector/data/ideal.csv")  
 
    ideal_data_count = session.query(IdealFunctions).count()
    assert ideal_data_count > 0, "Ideal functions data was not loaded correctly."

def test_load_test_data(setup_database):
    """Test loading test data into the database."""
    session = setup_database
    load_test_data(session, "C:/Users/dell/Desktop/M.Sc. Data Science/Programming wih Python/Ideal Function Selection/ideal-function-selector/data/test.csv")  

    test_data_count = session.query(TestDataModel).count()
    print(f"Test data count: {test_data_count}")  # Debugging line
    assert test_data_count > 0, "Test data was not loaded correctly."

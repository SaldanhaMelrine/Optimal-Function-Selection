# tests/test_database.py 

import pytest
from sqlalchemy.orm import Session
from src.database import Base, engine, IdealFunctions, TestDataModel, MappedTestData

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to set up and tear down the database for tests."""
    # Create tables
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Adding mock ideal function data with default values for all columns y1 to y50
    ideal_functions_data = [
        IdealFunctions(x=1.0, y1=1.0, y2=2.0, y3=3.0, y4=4.0, **{f'y{i}': 0 for i in range(5, 51)}),
        IdealFunctions(x=2.0, y1=1.1, y2=2.1, y3=3.1, y4=4.1, **{f'y{i}': 0 for i in range(5, 51)}),
        IdealFunctions(x=3.0, y1=1.2, y2=2.2, y3=3.2, y4=4.2, **{f'y{i}': 0 for i in range(5, 51)})
    ]
    session.add_all(ideal_functions_data)
    session.commit()

    # Adding mock test data
    test_data = [
        TestDataModel(x=1.0, y=1.05),
        TestDataModel(x=2.0, y=2.05),
        TestDataModel(x=3.0, y=3.05)
    ]
    session.add_all(test_data)
    session.commit()

    # Adding mock mapped test data
    mapped_test_data = [
        MappedTestData(x=1.0, y=1.05, ideal_function_id=1, deviation=0.05),
        MappedTestData(x=2.0, y=2.05, ideal_function_id=2, deviation=0.05),
        MappedTestData(x=3.0, y=3.05, ideal_function_id=3, deviation=0.05)
    ]
    session.add_all(mapped_test_data)
    session.commit()

    yield session  # Provide the session to the test

    session.close()
    Base.metadata.drop_all(engine)

def test_query_ideal_functions(setup_database):
    """Test to ensure the ideal functions data is correctly inserted and can be queried."""
    session = setup_database
    ideal_functions = session.query(IdealFunctions).all()
    
    # Assert that the ideal functions table is populated
    assert len(ideal_functions) == 3, "Database should contain ideal function data"
    
    # Further checks (e.g., values of the first record)
    assert ideal_functions[0].y1 == 1.0
    assert ideal_functions[0].y41 == 0  # Default value used in test setup

def test_query_test_data(setup_database):
    """Test to ensure the test data is correctly inserted and can be queried."""
    session = setup_database
    test_data = session.query(TestDataModel).all()
    
    # Assert that the test data table is populated
    assert len(test_data) == 3, "Database should contain test data"
    
    # Further checks (e.g., values of the first record)
    assert test_data[0].x == 1.0
    assert test_data[0].y == 1.05

def test_query_mapped_test_data(setup_database):
    """Test to ensure the mapped test data is correctly inserted and can be queried."""
    session = setup_database
    mapped_test_data = session.query(MappedTestData).all()
    
    # Assert that the mapped test data table is populated
    assert len(mapped_test_data) == 3, "Database should contain mapped test data"
    
    # Further checks (e.g., values of the first record)
    assert mapped_test_data[0].x == 1.0
    assert mapped_test_data[0].y == 1.05
    assert mapped_test_data[0].ideal_function_id == 1
    assert mapped_test_data[0].deviation == 0.05

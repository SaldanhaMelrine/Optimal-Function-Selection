import pytest
import numpy as np
from sqlalchemy.orm import Session
from src.database import Base, engine, TrainingData, IdealFunctions, TestDataModel, MappedTestData
from src.data_processor import select_ideal_functions, map_test_data

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to set up and tear down the database for tests."""
    # Create tables
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Adding mock training data
    training_data = [
        TrainingData(x=1.0, y1=1.0, y2=2.0, y3=3.0, y4=4.0),
        TrainingData(x=2.0, y1=1.1, y2=2.1, y3=3.1, y4=4.1),
        TrainingData(x=3.0, y1=1.2, y2=2.2, y3=3.2, y4=4.2)
    ]
    session.add_all(training_data)

    # Adding mock ideal function data with default values for y1 to y50
    ideal_functions_data = [
        IdealFunctions(x=1.0, y1=1.0, y2=2.0, y3=3.0, y4=4.0, **{f'y{i}': 0 for i in range(5, 51)}),
        IdealFunctions(x=2.0, y1=1.1, y2=2.1, y3=3.1, y4=4.1, **{f'y{i}': 0 for i in range(5, 51)}),
        IdealFunctions(x=3.0, y1=1.2, y2=2.2, y3=3.2, y4=4.2, **{f'y{i}': 0 for i in range(5, 51)})
    ]
    session.add_all(ideal_functions_data)

    # Adding mock test data
    test_data = [
        TestDataModel(x=1.0, y=1.05),
        TestDataModel(x=2.0, y=2.05),
        TestDataModel(x=3.0, y=3.05)
    ]
    session.add_all(test_data)
    session.commit()

    yield session  # Provide the session to the test

    session.close()
    Base.metadata.drop_all(engine)

def test_select_ideal_functions(setup_database):
    """Test the select_ideal_functions function to ensure it selects the ideal functions with minimum error."""
    selected_functions = select_ideal_functions()
    
    # Check if the output is a dictionary and contains keys for all training functions
    assert isinstance(selected_functions, dict), "select_ideal_functions should return a dictionary"
    assert set(selected_functions.keys()) == {'y1', 'y2', 'y3', 'y4'}, "selected_functions should contain keys for y1 to y4"

    # Assert that each selected ideal function key is among ideal function names y1 to y50
    for key in selected_functions.values():
        assert key in [f'y{i}' for i in range(1, 51)], f"{key} should be a valid ideal function key"

def test_map_test_data(setup_database):
    """Test the map_test_data function to ensure it maps test data correctly to the selected ideal functions."""
    # Mock selected functions output from select_ideal_functions
    selected_functions = {
        'y1': 'y1',
        'y2': 'y2',
        'y3': 'y3',
        'y4': 'y4'
    }
    
    # Mock training data format
    training_df = {
        'x': np.array([1.0, 2.0, 3.0]),
        'y1': np.array([1.0, 1.1, 1.2]),
        'y2': np.array([2.0, 2.1, 2.2]),
        'y3': np.array([3.0, 3.1, 3.2]),
        'y4': np.array([4.0, 4.1, 4.2])
    }

    # Run the map_test_data function
    mappings = map_test_data(selected_functions, training_df)

    # Check if mappings is a list and not empty
    assert isinstance(mappings, list), "map_test_data should return a list of mappings"
    assert len(mappings) > 0, "Mappings should contain data points"

    # Verify data in the mapped_test_data table
    session = setup_database
    mapped_data = session.query(MappedTestData).all()

    # Check if mappings were stored in the database
    assert len(mapped_data) == len(mappings), "All mappings should be saved in the database"

    # Check specific values for the first mapping (assuming sorted input data)
    assert mapped_data[0].x == 1.0, "First mapped x should match test data"
    assert mapped_data[0].y == 1.05, "First mapped y should match test data"
    assert mapped_data[0].ideal_function_id is not None, "Ideal function ID should be assigned"
    assert mapped_data[0].deviation is not None, "Deviation should be calculated and stored"

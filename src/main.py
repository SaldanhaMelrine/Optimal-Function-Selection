from sqlalchemy.orm import sessionmaker
from src.database import engine, TrainingData, IdealFunctions, TestDataModel
from data_loader import load_training_data, load_ideal_functions, load_test_data
from data_processor import select_ideal_functions, map_test_data
from data_visualizer import plot_data

# SQLAlchemy session
SessionLocal = sessionmaker(bind=engine)

def main():
    # Step 1: Load data into the database
    with SessionLocal() as session:
        load_training_data(session, 'data/train.csv')
        load_ideal_functions(session, 'data/ideal.csv')
        load_test_data(session, 'data/test.csv')

    # Step 2: Select ideal functions based on loaded data
    selected_functions = select_ideal_functions()
    print("Type of selected_functions in main:", type(selected_functions))  # Debugging output
    print("Contents of selected_functions in main:", selected_functions)  # Debugging output

    # Confirm `selected_functions` is a dictionary before passing to `map_test_data`
    assert isinstance(selected_functions, dict), "selected_functions is expected to be a dictionary"

    # Step 3: Retrieve training data in the correct dictionary format for processing
    with SessionLocal() as session:
        # Query and convert training data to dictionary format
        training_data = session.query(TrainingData).all()
        training_df = {
            'x': [row.x for row in training_data]
        }
        training_df.update({
            f'y{i+1}': [getattr(row, f'y{i+1}') for row in training_data]
            for i in range(4)  # Adjust the range if there are more columns in training_data
        })

    # Step 4: Map test data using the selected ideal functions and training data
    test_mappings = map_test_data(selected_functions, training_df)
    print("Test mappings:", test_mappings)  # Debugging output

    # Step 5: Retrieve test functions data in dictionary format for visualization
    with SessionLocal() as session:
        test_data = session.query(TestDataModel).all()
        test_df = {
            'x': [row.x for row in test_data],
            'y': [row.y for row in test_data]
        }


    # Step 6: Visualize the data
    plot_data(training_df, test_df, test_mappings)

if __name__ == "__main__":
    main()

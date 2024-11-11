import numpy as np
from sqlalchemy.orm import Session
from src.database import TestDataModel, TrainingData, IdealFunctions,MappedTestData, engine

def select_ideal_functions():
    """Select ideal functions that best fit each training function based on the Least Squares method."""
    selected_functions = {}
    with Session(engine) as session:
        # Load training and ideal data from the database
        training_data = session.query(TrainingData).all()
        ideal_data = session.query(IdealFunctions).all()

        # Convert training data and ideal functions to dictionaries
        training_df = {
            'x': np.array([row.x for row in training_data]),
            'y1': np.array([row.y1 for row in training_data]),
            'y2': np.array([row.y2 for row in training_data]),
            'y3': np.array([row.y3 for row in training_data]),
            'y4': np.array([row.y4 for row in training_data])
        }
        
        ideal_df = {'x': np.array([row.x for row in ideal_data])}
        ideal_df.update({
            f'y{i+1}': np.array([getattr(row, f'y{i+1}') for row in ideal_data])
            for i in range(50)
        })

        # Find the ideal function with the minimum least-squares error for each training function
        for train_key in ['y1', 'y2', 'y3', 'y4']:
            min_error = float('inf')
            best_fit = None
            training_values = training_df[train_key]

            for ideal_key, ideal_values in ideal_df.items():
                if ideal_key == 'x':
                    continue

                if training_values.shape != ideal_values.shape:
                    continue

                # Calculate error using least squares
                error = np.sum((training_values - ideal_values) ** 2)
                print(f"Error for {train_key} with {ideal_key}: {error}")  # Debugging checkpoint
                if error < min_error:
                    min_error = error
                    best_fit = ideal_key

            if best_fit:
                selected_functions[train_key] = best_fit
                print(f"Selected best fit for {train_key}: {best_fit} with error {min_error}")

        return selected_functions

def map_test_data(selected_functions, training_df, tolerance=1e-5):
    """Map test data to selected ideal functions based on closest x value match in training data."""
    mappings = []
    with Session(engine) as session:
        # Load test data and ideal functions from the database
        test_data = session.query(TestDataModel).all()
        ideal_data = session.query(IdealFunctions).all()

        # Convert ideal data to dictionary for easy access
        ideal_df = {
            f'y{i+1}': np.array([getattr(row, f'y{i+1}') for row in ideal_data])
            for i in range(50)
        }

        # Ensure training data x values are in a NumPy array
        x_train_array = np.array(training_df['x'])

        # Process each test data point
        for test in test_data:
            x_test, y_test = test.x, test.y

            # Find the closest x value in the training data
            closest_index = np.abs(x_train_array - x_test).argmin()
            closest_diff = np.abs(x_train_array[closest_index] - x_test)

            # Skip if no close match found within tolerance
            if closest_diff > tolerance:
                print(f"No close match for x_test={x_test} in training data within tolerance.")
                continue

            # Track the best mapping with the smallest error
            best_mapping = None
            min_error = float('inf')

            # Map test data point to ideal function based on selected function for each training y
            for train_key, ideal_key in selected_functions.items():
                ideal_y_value = ideal_df[ideal_key][closest_index]
                mapping_error = abs(y_test - ideal_y_value)

                # Update best mapping if this one has a smaller error
                if mapping_error < min_error:
                    min_error = mapping_error
                    if min_error < np.sqrt(2):
                        best_mapping = {
                            'x': x_test,
                            'y': y_test,
                            'ideal_function_id': ideal_key,  # assuming ideal_key corresponds to an ID
                            'deviation': mapping_error
                        }

            # Append and save the best mapping for this test point
            if best_mapping:
                mappings.append(best_mapping)
                # Insert mapping into database
                mapped_data = MappedTestData(
                    x=best_mapping['x'],
                    y=best_mapping['y'],
                    ideal_function_id=best_mapping['ideal_function_id'],
                    deviation=best_mapping['deviation']
                )
                session.add(mapped_data)
                print(f"Best mapping for x_test={x_test}, y_test={y_test}: ideal_function_id={mapped_data.ideal_function_id}, deviation={mapped_data.deviation}")

        # Commit all mapped data to the database
        session.commit()

    return mappings

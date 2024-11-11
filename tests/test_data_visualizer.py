import pandas as pd
import pytest
from src.data_visualizer import plot_data

def test_plot_data_with_valid_data():
    """Test plot_data with valid training, test, and mapped test data to ensure no errors are raised."""
    # Create mock training data
    training_data = {
        'x': [1.0, 2.0, 3.0],
        'y1': [1.0, 1.1, 1.2],
        'y2': [2.0, 2.1, 2.2],
        'y3': [3.0, 3.1, 3.2],
        'y4': [4.0, 4.1, 4.2]
    }

    # Create mock test data
    test_data = {
        'x': [1.0, 2.0, 3.0],
        'y': [1.05, 2.05, 3.05]
    }

    # Create mock mapped test data
    mapped_test_data = [
        {'x': 1.0, 'y': 1.05, 'ideal_function': 'y1', 'deviation': 0.05},
        {'x': 2.0, 'y': 2.05, 'ideal_function': 'y2', 'deviation': 0.05},
        {'x': 3.0, 'y': 3.05, 'ideal_function': 'y3', 'deviation': 0.05}
    ]

    # Call plot_data to ensure no errors are raised
    try:
        plot_data(training_data, test_data, mapped_test_data)
    except Exception as e:
        pytest.fail(f"plot_data raised an exception with valid data: {e}")

def test_plot_data_with_empty_data():
    """Test plot_data with empty data inputs to ensure it handles them gracefully."""
    # Empty training data
    training_data = {'x': [], 'y1': [], 'y2': [], 'y3': [], 'y4': []}
    # Empty test data
    test_data = {'x': [], 'y': []}
    # Empty mapped test data
    mapped_test_data = []

    # Call plot_data to ensure no errors are raised with empty data
    try:
        plot_data(training_data, test_data, mapped_test_data)
    except Exception as e:
        pytest.fail(f"plot_data raised an exception with empty data: {e}")

def test_plot_data_with_inconsistent_data_lengths():
    """Test plot_data with inconsistent data lengths to ensure it handles them gracefully."""
    # Training data with inconsistent lengths
    training_data = {
        'x': [1.0, 2.0, 3.0],
        'y1': [1.0, 1.1],
        'y2': [2.0, 2.1, 2.2],
        'y3': [3.0],
        'y4': [4.0, 4.1, 4.2]
    }

    # Consistent test and mapped test data
    test_data = {'x': [1.0, 2.0, 3.0], 'y': [1.05, 2.05, 3.05]}
    mapped_test_data = [
        {'x': 1.0, 'y': 1.05, 'ideal_function': 'y1', 'deviation': 0.05},
        {'x': 2.0, 'y': 2.05, 'ideal_function': 'y2', 'deviation': 0.05},
        {'x': 3.0, 'y': 3.05, 'ideal_function': 'y3', 'deviation': 0.05}
    ]

    # Call plot_data to ensure no errors are raised
    try:
        plot_data(training_data, test_data, mapped_test_data)
    except Exception as e:
        pytest.fail(f"plot_data raised an exception with inconsistent data lengths: {e}")

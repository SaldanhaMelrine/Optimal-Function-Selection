import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot

def plot_data(training_data, test_data, mapped_test_data):
    """Creates Bokeh plots to visualize training data, test data, and mapped test data in the desired format."""
    output_file("plot.html")

    # Convert dictionaries to DataFrames if lengths are consistent
    if not isinstance(training_data, pd.DataFrame):
        training_data = pd.DataFrame(training_data)
    if not isinstance(test_data, pd.DataFrame):
        test_data = pd.DataFrame(test_data)
    if isinstance(mapped_test_data, list) and len(mapped_test_data) > 0:
        mapped_test_data = pd.DataFrame(mapped_test_data)  # Convert list of dicts to DataFrame
    else:
        mapped_test_data = pd.DataFrame(columns=["x", "y", "ideal_function", "deviation"])  # Empty DataFrame

   
    # Convert data to ColumnDataSource for Bokeh
    train_source = ColumnDataSource(training_data)
    test_source = ColumnDataSource(test_data)
    mapped_test_source = ColumnDataSource(mapped_test_data)

    # Plot 1: Training Data
    p1 = figure(title="Training Data", x_axis_label="x", y_axis_label="y", width=300, height=300)
    p1.line('x', 'y1', source=train_source, line_width=2, color="blue", legend_label="y1")
    p1.line('x', 'y2', source=train_source, line_width=2, color="blue", legend_label="y2")
    p1.line('x', 'y3', source=train_source, line_width=2, color="blue", legend_label="y3")
    p1.line('x', 'y4', source=train_source, line_width=2, color="blue", legend_label="y4")

    # Plot 2: Test Data
    p2 = figure(title="Test Data", x_axis_label="x", y_axis_label="y", width=300, height=300)
    if not test_data.empty:
        p2.scatter('x', 'y', source=test_source, color="green", size=6, marker="circle", legend_label="Test Data")

    # Plot 3: Mapped Test Data
    p3 = figure(title="Mapped Test Data", x_axis_label="x", y_axis_label="y", width=300, height=300)
    if not mapped_test_data.empty:
        p3.scatter('x', 'y', source=mapped_test_source, color="red", size=6, marker="circle", legend_label="Mapped Test Data")

    # Arrange plots in a grid layout
    grid = gridplot([[p1, p2, p3]])

    # Show all plots in one HTML file
    show(grid)

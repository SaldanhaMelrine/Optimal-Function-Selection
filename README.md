# Ideal Function Selector

This project automates the selection of ideal functions based on training data and maps test data to these functions using Python, SQLAlchemy, and Bokeh. It applies deviation and threshold analysis to match test data points to the closest ideal functions, providing a streamlined approach for data analysis and visualization.

## Project Structure

- `data/`: Contains the data files (e.g., train.csv, ideal.csv, test.csv) for training, ideal functions, and test data.
- `src/`: Core Python code modules for data loading, processing, and visualization.
- `database.py`: Sets up the SQLite database and defines data tables using SQLAlchemy.
- `data_loader.py`: Loads data from CSV files into the database.
- `data_processor.py`: Processes data, selects ideal functions, and maps test data based on deviation.
- `data_visualizer.py`: Generates Bokeh visualizations for training data, test data, and mapped data.
- `tests/`: Unit tests for each module to ensure code reliability.
- `README.md`: Project overview and usage guide (this file).
- `requirements.txt`: Lists Python dependencies for easy installation.

## Project Overview
This project employs Python and SQL to analyze and map data using deviation and threshold analysis. With a structured database, it organizes and processes training, ideal, and test datasets, identifying optimal functions and mapping test data based on minimum deviation. Interactive Bokeh visualizations provide insights into data alignment and accuracy, making the Ideal Function Selector a valuable tool for data science applications.

## Dependencies
Python 3.8+
SQLAlchemy: Database ORM for managing SQLite data.
Pandas: Data manipulation library.
Bokeh: Visualization library for interactive data plots.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/ideal-function-selector.git
cd ideal-function-selector
pip install -r requirements.txt

 

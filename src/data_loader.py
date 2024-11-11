import pandas as pd
from sqlalchemy.orm import sessionmaker
from src.database import engine, TrainingData, IdealFunctions, TestDataModel

# Set up the SQLAlchemy session
Session = sessionmaker(bind=engine)

def load_training_data(session, training_file_path):
    """Load training data from a CSV file into the TrainingData table."""
    print("Loading file:", training_file_path)  # Debugging print
    data = pd.read_csv(training_file_path)
    for index, row in data.iterrows():
        training_data = TrainingData(
            x=row['x'],
            y1=row['y1'],
            y2=row['y2'],
            y3=row['y3'],
            y4=row['y4']
        )
        session.add(training_data)
    session.commit()

def load_ideal_functions(session, ideal_file_path):
    """Load ideal functions data from a CSV file into the IdealFunctions table."""
    data = pd.read_csv(ideal_file_path)
    for index, row in data.iterrows():
        print(row)
        ideal_data = IdealFunctions(
            x=row['x'],
            y1=row['y1'],
            y2=row['y2'],
            y3=row['y3'],
            y4=row['y4'],
            y5=row['y5'],
            y6=row['y6'],
            y7=row['y7'],
            y8=row['y8'],
            y9=row['y9'],
            y10=row['y10'],
            y11=row['y11'],
            y12=row['y12'],
            y13=row['y13'],
            y14=row['y14'],
            y15=row['y15'],
            y16=row['y16'],
            y17=row['y17'],
            y18=row['y18'],
            y19=row['y19'],
            y20=row['y20'],
            y21=row['y21'],
            y22=row['y22'],
            y23=row['y23'],
            y24=row['y24'],
            y25=row['y25'],
            y26=row['y26'],
            y27=row['y27'],
            y28=row['y28'],
            y29=row['y29'],
            y30=row['y30'],
            y31=row['y31'],
            y32=row['y32'],
            y33=row['y33'],
            y34=row['y34'],
            y35=row['y35'],
            y36=row['y36'],
            y37=row['y37'],
            y38=row['y38'],
            y39=row['y39'],
            y40=row['y40'],
            y41=row['y41'],
            y42=row['y42'],
            y43=row['y43'],
            y44=row['y44'],
            y45=row['y45'],
            y46=row['y46'],
            y47=row['y47'],
            y48=row['y48'],
            y49=row['y49'],
            y50=row['y50']
        )
        session.add(ideal_data)  
    session.commit()  

def load_test_data(session, test_file_path):
    """Load test data into the TestDataModel table."""
    data = pd.read_csv(test_file_path)
    for index, row in data.iterrows():
        test_data = TestDataModel(
            x=row['x'],
            y=row['y']
        )
        session.add(test_data)
    session.commit()  # Use the passed session to commit changes


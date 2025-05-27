import pandas as pd

def feature_engineering ():
    # 불러오기
    EDA_data = pd.read_csv('data/EDA/data_EDA.csv')
    print(EDA_data.head())
    return print("Finished engineering. save the file to csv")

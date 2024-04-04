import pandas as pd

def extract_data():
    #data= pd.concat(map(pd.read_csv, ['train_oil.csv', 'oil_test.csv']), ignore_index=True) 
    train_data = pd.read_csv('train_oil.csv')
    #test_data = pd.read_csv('oil_test.csv')
    print("Train_data:",train_data.head()) 
    #print("Test_data:", test_data.head())
    return train_data     #, test_data

extract_data()
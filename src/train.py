from data_cleaning import *
from sklearn.linear_model import LinearRegression
import pickle

def train_model():
    df = cleaned_data()
    x = df.drop('price', axis=1)
    y = df['price']
    regressor = LinearRegression()
    regressor.fit(x, y)
    return regressor

def save_model(regressor):
    with open('../models/model.pkl', 'wb') as f:
        pickle.dump(regressor, f)

def features():
    df = cleaned_data()
    su = statezip_values()
    df = df.drop('price', axis=1)
    lst = df.columns
    with open('../models/features.pkl', 'wb') as f:
        pickle.dump(lst, f)
    with open('../models/statezip.pkl', 'wb') as f:
        pickle.dump(su, f)

if __name__ == '__main__':
    save_model(train_model())
    features()

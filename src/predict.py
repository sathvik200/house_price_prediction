import pandas as pd
from src.load_model import load_saved_model, load_features

model = load_saved_model()

def create_dataframe():
    features = load_features()
    df = pd.DataFrame([[0 for x in range(len(features))]], columns = features)
    return df

def state_zip(statezip):
    statezip = "statezip_"+str(statezip)
    return statezip

def predict(input_dict):
    df = create_dataframe()
    for key, value in input_dict.items():
        if key!='statezip':
            df.at[0, key] = value

        zip_col = state_zip(value)
        if zip_col in df.columns:
            df.at[0, zip_col] = 1

    prediction = model.predict(df)
    return prediction

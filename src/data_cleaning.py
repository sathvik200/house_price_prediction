import pandas as pd

def cleaned_data():
    data = pd.read_csv('../data/data.csv')
    df = data.drop(columns=["date", "country", "street"])
    new_df = df[df['price'] != 0]
    new_df = new_df[new_df["price"] <= new_df['price'].quantile(0.99)]
    new_df = new_df.drop('city', axis=1)
    df_encoded = pd.get_dummies(new_df, columns=['statezip'], drop_first=True, dtype="int")
    return df_encoded

def statezip_values():
    data = pd.read_csv('../data/data.csv')
    statezip_unique = data['statezip'].unique().tolist()
    return statezip_unique
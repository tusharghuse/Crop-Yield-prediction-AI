import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess(path):
    df = pd.read_csv(path)

    # Encode soil type
    le = LabelEncoder()
    df['soil_type'] = le.fit_transform(df['soil_type'])

    X = df.drop('yield', axis=1)
    y = df['yield']

    return X, y
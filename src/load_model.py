import pickle

def load_saved_model():
    with open('models/model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def load_features():
    with open('models/features.pkl', 'rb') as f:
        features = pickle.load(f)
        return features

def state_features():
    with open('models/statezip.pkl', 'rb') as f:
        statezip = pickle.load(f)
        return statezip
from pathlib import Path
import pickle

def predict(df):
    # Load the model and scaler from the saved file
    # Load model
    file_name = 'model/used_car_price_model_mae.sav'
    model = pickle.load(open(file_name, 'rb'))
    
    pred = model.predict(df)
    return pred

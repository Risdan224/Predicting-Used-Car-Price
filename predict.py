from pathlib import Path
import pickle
# # Import Libraries for modelling
# from sklearn.linear_model import LinearRegression, ElasticNet, Lasso
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
# from xgboost.sklearn import XGBRegressor
# from sklearn.kernel_ridge import KernelRidge

# # Import library for tranformed data's features
# from sklearn.compose import TransformedTargetRegressor

# # Import Matrix for evaluation
# from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, mean_squared_log_error
# from sklearn.metrics import mean_absolute_percentage_error

# # Import Libraries for Feature Engineering

# import category_encoders as ce
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline

# from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV, GridSearchCV, KFold

# from sklearn.preprocessing import StandardScaler


def predict(df):
    # Load the model and scaler from the saved file
    # Load model
    file_name = 'model/used_car_price_model_mae.sav'
    model = pickle.load(open(file_name, 'rb'))
    
    pred = model.predict(df)
    return pred
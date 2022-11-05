import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from matplotlib import rcParams
from matplotlib.cm import rainbow
import warnings
warnings.filterwarnings('ignore')

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

def initialize_dataset():
    global df
    df = pd.read_csv('heart.csv')

def get_user_data():
    print("get_user_data")
    
def get_data():
    return df

def get_info():
    return df.info()

def describe():
    return df.describe()

def get_head():
    return df.head()

def get_histogram():
    return df.hist()
   
def train_model():
    from sklearn.ensemble import RandomForestRegressor
    
    initialize_dataset()
    
    X = df.drop("target", axis=1)
    y = df["target"]
    
    model = RandomForestRegressor()
    model.fit(X, y)
    
    pickle.dump(model, open('model.pkl', 'wb'))
     
def get_prediction(age=0, sex=0, cp=0, trestbps=0, chol=0, fbs=0, restecg=0, thalach=0, exang=0, oldpeak=0, slope=0, ca=0, thal=0):
    
    initialize_dataset()
    
    X_test = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
    X_test = X_test.reshape((1,-1))
    
    pickled_model = pickle.load(open('model.pkl', 'rb'))
    
    val = pickled_model.predict(X_test)
    
    add_data(X_test, int(val), df)
    
    return val

def add_data(X_test, val, df):
    temp = np.append(X_test, val)
    temp = temp.reshape((1,-1))
    temp = pd.DataFrame(temp, columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'])
    df = df.append(temp)
    open("heart.csv", "w").close()
    df.to_csv('heart.csv', mode='a', index=False, header=True)
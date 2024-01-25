import os

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import warnings


from sklearn.preprocessing import LabelEncoder
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score


# data preprocessing
def preprocess_data(filename):
    os.getcwd()
    dataset_path = os.getcwd() +"\Datasets\\"+ filename
    dataset = pd.read_csv(dataset_path) 
    return dataset
    

dllDf = preprocess_data("TUANDROMD.csv")
print(dllDf)
dllDf.info()
print("Column Names:")
print(dllDf.columns[-1])
#prediction
features = pd.get_dummies(dllDf.iloc[:, :-1])
target = dllDf.iloc[:, -1]

print(features)
np.array(target)
features_lst = list(features.columns)
print(features_lst)
features = np.array(features)


train_features,test_features, train_target, test_target = train_test_split(features,target,test_size = 0.24, random_state = 42)
print('train_features shape: ',train_features.shape)
print('test_features shape: ',test_features.shape)
print('train_target shape: ',train_target.shape)
print('test_target shape: ',test_target.shape)

"""

x_categorical = dllDf.select_dtypes(include=['object']).apply(label_encoder.fit_transform)
x_numerical = dllDf.select_dtypes(exclude=['object']).values
x = pd.concat([pd.DataFrame(x_numerical), x_categorical], axis=1).values

#decide the prediction
y = dllDS['kernel32.dll']
x = dllDS.drop(['kernel32.dll',"SHA256"], axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)





# Regression
random_forest_c = RandomForestRegressor(n_estimators=10, max_depth=3, random_state=42)
random_forest_c .fit(x_train, y_train)
y_pred = RandomForestRegressor.predict(x_test)

# Predict
f = x.columns
the_first = RandomForestRegressor.estimators_[0]
plt.figure(figsize=(15,6))
tree.sample_tree(the_first, feature_names=f, fontsize=10, filled=True, rounded=True)
"""

# Importing the libraries
import pickle
import scipy as sp
import numpy as np
import pandas as pd
import statsmodels as st
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
sns.set()

# Import datasets
df = pd.read_csv('LoanStats3a.csv')

# Separate target variable from training set
# Target variable
y = df["loan_status"]
# delete target variable from training set, in this case training is whole dataframe -> df
df.drop('loan_status', axis=1, inplace=True)

#Splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=4)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_train = StandardScaler()
X_train = sc_train.fit_transform(X_train)
X_test = sc_train.transform(X_test)

#Model Training
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Saving model to disk
pickle.dump(clf, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict(X_test))
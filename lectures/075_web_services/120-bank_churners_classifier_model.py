#!/usr/bin/env python
# coding: utf-8

# # Bank Churners Classifier Model

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#pre-training
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer

#training
from sklearn import ensemble
from sklearn import pipeline


#post training 
from sklearn.metrics import accuracy_score
from joblib import dump


# #### Read data

# In[ ]:


data_df = pd.read_csv('../../datasets/credit-card-customers/BankChurners.zip')
data_df.shape


# In[ ]:


data_df.head()


# In[ ]:


data_df.columns


# In[ ]:


data_df.isna().sum()


# #### Remove columns which should not go into the model

# In[ ]:


data_df.drop([
    'CLIENTNUM',
    'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1',
    'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'
], axis=1, inplace=True)


# #### Convert categorical columns

# In[ ]:


#https://medium.com/@sami.yousuf.azad/one-hot-encoding-with-pandas-dataframe-49a304e8507a
CATEGORICAL_COLS = ['Gender', 'Education_Level', 'Marital_Status', 'Income_Category', 'Card_Category', ]
col_transformer = make_column_transformer(
  (OneHotEncoder(), CATEGORICAL_COLS),
  remainder='passthrough')

transformed = col_transformer.fit_transform(data_df)

transformed_df = pd.DataFrame(transformed, columns=col_transformer.get_feature_names_out())


# In[ ]:


transformed_df.head()


# In[ ]:


transformed_df.columns


# #### Build model

# In[ ]:


X_train, X_test, y_train, y_test = train_test_split(
    data_df.drop(['Attrition_Flag'], axis=1)
    , data_df.Attrition_Flag
    , random_state=1)


# In[ ]:


pipe = pipeline.make_pipeline(
    col_transformer
    ,ensemble.RandomForestClassifier(n_estimators=100, min_samples_split=2) # <== Classifier
)


# In[ ]:


#%%time
pipe.fit(X_train, y_train)

y_predict = pipe.predict(X_test)
pipe.score(X_test, y_test)


# In[ ]:


pipe


# In[ ]:


#pd.DataFrame({'feature':X_train.columns, 'importance':pipe.feature_importances_}).sort_values(by='importance')


# #### Save model

# In[ ]:


#%%time
dump(pipe, 'bank_churners_classifier_model.joblib')


# In[ ]:


#%ls


# #### Read model

# In[ ]:


from joblib import load


# In[ ]:


trained_model = load('bank_churners_classifier_model.joblib')


# In[ ]:


trained_model.feature_names_in_


# The following columns are categorical

# In[ ]:


CATEGORICAL_COLS


# In[ ]:


for col in CATEGORICAL_COLS:
    print(col, data_df[col].unique())


# In[ ]:


test_data_df = pd.Series({
    'Customer_Age'   : 30, 
    'Gender'         : 'M', 
    'Dependent_count': 3, 
    'Education_Level': 'Graduate',
    'Marital_Status' : 'Single', 
    'Income_Category': '$40K - $60K', 
    'Card_Category'  : 'Blue',
    'Months_on_book' : 5, 
    'Total_Relationship_Count' : 3,
    'Months_Inactive_12_mon'   : 1, 
    'Contacts_Count_12_mon'    : 2, 
    'Credit_Limit'             : 34000,
    'Total_Revolving_Bal'      : 40000, 
    'Avg_Open_To_Buy'          : 200, 
    'Total_Amt_Chng_Q4_Q1'     : 34,
    'Total_Trans_Amt'          : 500, 
    'Total_Trans_Ct'           : 3, 
    'Total_Ct_Chng_Q4_Q1'      : 23,
    'Avg_Utilization_Ratio'    : .1
}).to_frame().T


# In[ ]:


test_data_df


# In[ ]:


test_data_df.columns


# In[ ]:


trained_model.predict(test_data_df)


# In[ ]:


trained_model.classes_


# In[ ]:


trained_model.predict_proba(test_data_df)


# ### Convert this notebook to .py
# Some students having trouble reading the model so they can run a .py file in their own enviornment and generate the model file using the same env as their web services code

# In[ ]:


get_ipython().system('jupyter nbconvert --to python 120-bank_churners_classifier_model.ipynb')


# In[ ]:





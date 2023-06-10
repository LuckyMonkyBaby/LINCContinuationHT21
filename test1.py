
import numpy as np
import pandas as pd
from scipy import stats
import plotly.express as px
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import seaborn as sn
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


listt = ["Attrition_Flag", 'Customer_Age', 'Gender',
       'Dependent_count', 'Education_Level', 'Marital_Status',
       'Income_Category', 'Card_Category', 'Months_on_book',
       'Total_Relationship_Count', 'Months_Inactive_12_mon',
       'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
       'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt',
       'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1',
       'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2']

df1 = pd.read_excel("/Users/lukasandersson/Downloads/credit_card_customers.xlsx")

df1['Attrition_Flag'].replace(["Existing Customer", "Attrited Customer"], [1, 0], inplace=True)

d = defaultdict(LabelEncoder)

numvars = [
    'Credit_Limit', "Attrition_Flag",'Customer_Age', 'Months_on_book',
       'Total_Relationship_Count', 'Credit_Limit', 'Total_Revolving_Bal',
       'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt',
       'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio']
# ,'Total_Revolving_Bal', 'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 'Total_Trans_Ct',
#    'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio','Contacts_Count_12_mon', 'Months_Inactive_12_mon', 'Total_Relationship_Count', 'Months_on_book',
#    'Dependent_count', 'Customer_Age', 
catvars = [
    'Gender', 'Income_Category', 'Card_Category'
    ]

fig, ax = plt.subplots(figsize=(12,7))
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')
labeldata = df1[catvars].apply(lambda x: d[x.name].fit_transform(x))

#for x in range(len(catvars)):
#    print(catvars[x], ': ', df1[catvars[x]].unique())
#    print(catvars[x], ': ', labeldata[catvars[x]].unique())
max_iter = 150000

dummyv = pd.get_dummies(df1[catvars])

df_clean = pd.concat([df1[numvars], dummyv], axis=1)

X = df_clean.drop(['Attrition_Flag'], axis=1)
Y = df_clean['Attrition_Flag']


X_train, X_test, Y_train, Y_test = train_test_split(X,
                                                    Y,
                                                    test_size=0.01,
                                                    random_state=10
                                                    )

# Logistic regression:
clf = LogisticRegression(max_iter= 12000).fit(X_train, Y_train)
# Create a prediction:
y_pred = clf.predict(X_test)

# Calculate the confusion matrix.
confusion_matrix = pd.crosstab(Y_test, y_pred)
px.imshow(confusion_matrix, annot=True)
plt.show
from sklearn import metrics

print('Accuracy: ', metrics.accuracy_score(Y_test, y_pred))
import plotly.express as px
from scipy import stats
import pandas as pd
import numpy as np
import re
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
import plotly.graph_objects as go

df = pd.read_excel("/Users/lukasandersson/Downloads/credit_card_customers.xlsx")
d = defaultdict(LabelEncoder)

listt = ['Attrition_Flag', 'Customer_Age', 'Gender',
       'Dependent_count', 'Education_Level', 'Marital_Status',
       'Income_Category', 'Card_Category', 'Months_on_book',
       'Total_Relationship_Count', 'Months_Inactive_12_mon',
       'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
       'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt',
       'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio']
for i in range(0,len(df)):
    if df["Attrition_Flag"][i] == "Existing Customer":
        df['Attrition_Flag'] = df['Attrition_Flag'].replace(['Existing Customer'],1)
            
    elif df["Attrition_Flag"][i] == "Attrited Customer":
        df['Attrition_Flag'] = df['Attrition_Flag'].replace(['Attrited Customer'],0)
        
for i in range(0,len(df)):
    if df["Gender"][i] == "M":
        df['Gender'] = df['Gender'].replace(['M'],1)
            
    elif df["Gender"][i] == "F":
        df['Gender'] = df['Gender'].replace(['F'],0)
        
for i in range(0,len(df)):
    if df["Card_Category"][i] == "Blue":
        df['Card_Category'] = df['Card_Category'].replace(['Blue'],0)
            
    elif df["Card_Category"][i] == "Silver":
        df['Card_Category'] = df['Card_Category'].replace(['Silver'],1)
        
    elif df["Card_Category"][i] == "Gold":
        df['Card_Category'] = df['Card_Category'].replace(['Gold'],2)
        
    elif df["Card_Category"][i] == "Platinum":
        df['Card_Category'] = df['Card_Category'].replace(['Platinum'],3)
        
for i in range(0,len(df)):
    if df["Education_Level"][i] == "Uneducated":
        df['Education_Level'] = df['Education_Level'].replace(['Uneducated'],1)
            
    elif df["Education_Level"][i] == "High School":
        df['Education_Level'] = df['Education_Level'].replace(['High School'],2)
        
    elif df["Education_Level"][i] == "College":
        df['Education_Level'] = df['Education_Level'].replace(['College'],3)
        
    elif df["Education_Level"][i] == "Graduate":
        df['Education_Level'] = df['Education_Level'].replace(['Graduate'],4)
        
    elif df["Education_Level"][i] == "Post-Graduate":
        df['Education_Level'] = df['Education_Level'].replace(['Post-Graduate'],5)
        
    elif df["Education_Level"][i] == "Doctorate":
        df['Education_Level'] = df['Education_Level'].replace(['Doctorate'],6)
        
    elif df["Education_Level"][i] == "Unknown":
        df['Education_Level'] = df['Education_Level'].replace(['Unknown'],0)

for i in range(0,len(df)):
    if df["Income_Category"][i] == "Less than $40K":
        df['Income_Category'] = df['Income_Category'].replace(['Less than $40K'],1)
        
    elif df["Income_Category"][i] == "$40K - $60K":
        df['Income_Category'] = df['Income_Category'].replace(['$40K - $60K'],2)
        
    elif df["Income_Category"][i] == "$60K - $80K":
        df['Income_Category'] = df['Income_Category'].replace(['$60K - $80K'],3)
        
    elif df["Income_Category"][i] == "$80K - $120K":
        df['Income_Category'] = df['Income_Category'].replace(['$80K - $120K'],4)
        
    elif df["Income_Category"][i] == "$120K +":
        df['Income_Category'] = df['Income_Category'].replace(['$120K +'],5)
    
    elif df["Income_Category"][i] == "Unknown":
        df['Income_Category'] = df['Income_Category'].replace(['Unknown'],0)
        
for i in range(0,len(df)):
    if df["Marital_Status"][i] == "Married":
        df['Marital_Status'] = df['Marital_Status'].replace(['Married'],3)
            
    elif df["Marital_Status"][i] == "Single":
        df['Marital_Status'] = df['Marital_Status'].replace(['Single'],1)
        
    elif df["Marital_Status"][i] == "Divorced":
        df['Marital_Status'] = df['Marital_Status'].replace(["Divorced"],2)
        
    elif df["Marital_Status"][i] == "Unknown":
        df['Marital_Status'] = df['Marital_Status'].replace(['Unknown'],0)
c = []
d = []
for i in listt:
    a = np.array(df[i])
    for j in listt:
        b = np.array(df[j])
        Ding = stats.pearsonr(a,b)
        map(str, Ding)
        tuple(map(str, Ding))
        Mate = ' '.join(map(str, Ding))
        split_string = Mate.split(" ", 1)
        substring = split_string[0]
        d.append(round(float(substring), 6))
    c.append(d)
    d=[]
x = listt
y = listt
z = c
z_text = [[str(y) for y in x] for x in z]





import numpy as np
import pandas as pd
from scipy import stats
import plotly.express as px
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
df = pd.read_excel("/Users/lukasandersson/Downloads/credit_card_customers.xlsx")


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
        

mean = df.groupby('Attrition_Flag').mean()


ts = pd.crosstab(df.Customer_Age,df.Attrition_Flag).plot(kind='bar')
ts.plot()
plt.show()



#From the mean of consumers staying or leaving, the most impactful statics were: Gender, Relationship count, credit limit, total revolving balance, total trans amt, total trans ct, ct chnq q4, utilization rate





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
from scipy import stats
df = pd.read_excel("/Users/lukasandersson/Downloads/credit_card_customers.xlsx")
for i in range(0,len(df)):
    if df["Attrition_Flag"][i] == "Existing Customer":
        df['Attrition_Flag'] = df['Attrition_Flag'].replace(['Existing Customer'],'1')
            
    elif df["Attrition_Flag"][i] == "Attrited Customer":
        df['Attrition_Flag'] = df['Attrition_Flag'].replace(['Attrited Customer'],'0')
        
df.groupby('Attrition_Flag').mean()
            
def consumers():
    active,left,male,female = (0,0,0,0)
    listt =[]
    for i in range(0,len(df)):
        if df["Attrition_Flag"][i] == "1":
            active += 1
            
        elif df["Attrition_Flag"][i] == "0":
            left += 1
            listt.append(i)
            
    print(gender(listt))
    print(marriage(listt))
    print(income(listt))
    print(monthsonbook(listt))
    print(educationlevel(listt))
    
            
    print("customer that have left: " + str(left))
    print(str(left/active))
    return
        

def gender(rows):
    male,female = (0,0)
    for row in rows:
        if df["Gender"][row] == "M":
            male += 1
        if df["Gender"][row] == "F":
            female += 1
             
    return list([male,female])

def marriage(rows):
    married,single,divorced,unknown = (0,0,0,0)
    for row in rows:
        if df["Marital_Status"][row] == "Married":
            married +=1
        elif df["Marital_Status"][row] == "Single":
            single +=1
        elif df["Marital_Status"][row] == "Divorced":
            divorced +=1
        elif df["Marital_Status"][row] == "Unknown":
            unknown +=1
    return dict({"married" : married,
                 "single" : single,
                 "divorced" : divorced,
                 "unknown" : unknown})


def income(rows):
    Non,ulow,low,medium,high = (0,0,0,0,0)
    for row in rows:
        if df["Income_Category"][row] == "Less than $40K":
            Non +=1
        elif df["Income_Category"][row] == "$40K - $60K":
            ulow +=1
        elif df["Income_Category"][row] == "$60K - $80K":
            low +=1
        elif df["Income_Category"][row] == "$80K - $120K":
            medium +=1
        elif df["Income_Category"][row] == "$120K +":
            high +=1
    return dict({"None" : Non,
                 "ultra low": ulow,
                 "low": low,
                 "medium" : medium, 
                 "high" : high})

def monthsonbook(rows):
    Non,low,medium,high = (0,0,0,0)
    for row in rows:
        x = df["Months_on_book"][row]
        if x < 20:
            Non +=1
        elif 30 > x > 20:
            low +=1
        elif 40 > x > 30:
            medium +=1
        elif 50 > x > 40:
            high +=1
    return dict({"less than 20 months" : Non,
                 "20-30": low,
                 "30-40" : medium, 
                 "40-50" : high})

def educationlevel(rows):
    Uneducated,Graduate,College,HighSchool,Unknown, PostG, doctorate = (0,0,0,0,0,0,0)
    for row in rows:
        x = df["Education_Level"][row]
        if x == "Uneducated":
            Uneducated +=1
        elif x == "High School":
            HighSchool +=1
        elif x == "Graduate":
            Graduate +=1
        elif x == "College":
            College += 1
        elif x == "Post-Graduate":
            PostG += 1
        elif x == "Doctorate":
            doctorate += 1
        elif x == "Unknown":
            Unknown += 1
    return dict({"Unknown" : Unknown,
                 "Uneducated": Uneducated,
                 "Graduate" : Graduate, 
                 "High School" : HighSchool,
                 "College": College,
                 "Post-Graduate": PostG,
                 "Doctorate": doctorate})




consumers()

a = np.array(df["Months_on_book"])

b = np.arange(df["Attrition_Flag"])
print(a)
print(b)




    
import plotly.express as px
import pandas as pd
df = pd.read_excel("/Users/lukasandersson/Downloads/credit_card_customers.xlsx")
df['Attrition_Flag'].replace(["Existing Customer", "Attrited Customer"], [1, 0], inplace=True)

fig = px.histogram(df, x="Income_Category", color="Attrition_Flag", category_orders=dict(Income_Category=["Unknown","Less than $40K", "$40K - $60K", "$60K - $80K", "$80K - $120K", "$120K +"]))
fig.show()




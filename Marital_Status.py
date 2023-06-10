import plotly.express as px
import pandas as pd
df = pd.read_excel("/Users/lukasandersson/Downloads/credit_card_customers.xlsx")
df['Attrition_Flag'].replace(["Existing Customer", "Attrited Customer"], [1, 0], inplace=True)

fig = px.histogram(df, x="Marital_Status", color="Attrition_Flag")
fig.show()





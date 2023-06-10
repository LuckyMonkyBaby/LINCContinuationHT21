
import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
app = dash.Dash(__name__)

width1 = 600

df = pd.read_excel("/Users/lukasandersson/Downloads/credit_card_customers.xlsx")
df['Attrition_Flag'].replace(["Existing Customer", "Attrited Customer"], [1, 0], inplace=True)

#colors = {
#    'background': 'snow',
#    'text': ''
#}
333
fig4 = px.histogram(df, x="Months_on_book", color="Attrition_Flag", width=width1, height=400)
fig1 = px.histogram(df, x="Education_Level", color="Attrition_Flag", category_orders=dict(Education_Level=["Unknown", "Uneducated","High School", "Graduate", "College", "Post-Graduate", "Doctorate"]), width=width1, height=400)
fig2 = px.histogram(df, x="Income_Category", color="Attrition_Flag", category_orders=dict(Income_Category=["Unknown","Less than $40K", "$40K - $60K", "$60K - $80K", "$80K - $120K", "$120K +"]), width=width1, height=400)
fig3 = px.histogram(df, x="Marital_Status", color="Attrition_Flag", width=width1, height=400)
fig = px.histogram(df, x="Attrition_Flag", color="Attrition_Flag", width=width1, height=400)
fig5 = px.histogram(df, x="Gender", color="Attrition_Flag", width=width1, height=400)
#fig.layout.plot_bgcolor='snow'
#fig.layout.paper_bgcolor='snow'
fig.update_layout(bargap =0.2)
fig4.update_layout(bargap =0.02)

app.layout = html.Div( children=[
    html.H1(children='Advanced Workshop - Results', style={'textAlign': 'center'}),
    #html.Div(children='The best project you have seen.', style={'textAlign': 'center'}),
    html.Div(children=[
        dcc.Graph(
            id='Attrition_Flag',
            figure=fig, style={'display': 'inline-block'}
        ),
        dcc.Graph(
            id='Income_Category',
            figure=fig1, style={'display': 'inline-block'}
        )]), 
    html.Div([
        dcc.Graph(
            id='Months_On_Book',
            figure=fig2, style={'display': 'inline-block'}
        ),
        dcc.Graph(
            id='Education_Level',
            figure=fig3, style={'display': 'inline-block'}
        )]),
    html.Div([
        dcc.Graph(
            id='Marital_Status',
            figure=fig4, style={'display': 'inline-block'}
        ),
        dcc.Graph(
            id='Gender',
            figure=fig5, style={'display': 'inline-block'}
    )])
])

if __name__ == '__main__':
    app.run_server(debug=True)
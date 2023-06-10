
import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from scipy import stats
app = dash.Dash(__name__)
from correlation import x,y,z
from linearregression import confusion_matrix, accuracy


width1 = 700

df = pd.read_excel("/Users/lukasandersson/Downloads/credit_card_customers.xlsx")
df['Attrition_Flag'].replace(["Existing Customer", "Attrited Customer"], [1, 0], inplace=True)

#colors = {
#    'background': 'snow',
#    'text': ''
#}
333
fig4 = px.histogram(df, x="Months_on_book", color="Attrition_Flag", barmode='group', width=width1, height=400)
fig1 = px.histogram(df, x="Education_Level", color="Attrition_Flag", category_orders=dict(Education_Level=["Unknown", "Uneducated","High School", "Graduate", "College", "Post-Graduate", "Doctorate"]), barmode='group', width=width1, height=400)
fig2 = px.histogram(df, x="Income_Category", color="Attrition_Flag", category_orders=dict(Income_Category=["Unknown","Less than $40K", "$40K - $60K", "$60K - $80K", "$80K - $120K", "$120K +"]),barmode='group', width=width1, height=400)
fig3 = px.histogram(df, x="Marital_Status", color="Attrition_Flag",barmode='group', width=width1, height=400)
fig = px.histogram(df, x="Attrition_Flag", color="Attrition_Flag",barmode='group', width=width1, height=400)
fig5 = px.histogram(df, x="Gender", color="Attrition_Flag",barmode='group', width=width1, height=400)
fig6 = px.imshow(z, aspect="auto", x=x, y=y, color_continuous_scale='RdBu_r')
fig7 = px.imshow(confusion_matrix, text_auto = True, color_continuous_scale='RdBu_r')




fig7.update_xaxes(side="top")
fig.update_layout(bargap =0.2)
fig4.update_layout(bargap =0.02)

app.layout = html.Div( children=[
    html.H1(children='Advanced Workshop - Project', style={'textAlign': 'center'}),
    html.Div(children='Linear regression', style={'textAlign': 'center'}),
    html.Div([
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
    )]),
    html.Div([
         dcc.Graph(
         id="Correlation Matrix",
	figure=fig6)]),

    html.Div([
         dcc.Graph(
         id="linearregression",
	figure=fig7)]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
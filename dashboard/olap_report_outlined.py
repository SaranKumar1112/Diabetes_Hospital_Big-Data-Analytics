import os

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/cleaned_diabetic_data_with_Median 1.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Impact of Hospital Stay Duration", style={'textAlign': 'center'}),

    html.H2("Distribution of Time in Hospital", style={'textAlign': 'center'}),
    dcc.Graph(id='time_in_hospital_plot'),

    html.Label("Select Variable:"),
    dcc.Dropdown(
        id='variable-dropdown',
        options=[
            {'label': 'Number of Lab Procedures', 'value': 'num_lab_procedures'},
            {'label': 'Number of Diagnoses', 'value': 'number_diagnoses'},
            {'label': 'Number of Medications', 'value': 'num_medications'},
            {'label': 'Discharge Disposition ID', 'value': 'discharge_disposition_id'},
            {'label': 'Number of Outpatient Visits', 'value': 'number_outpatient'},
            {'label': 'Age', 'value': 'age'},
            {'label': 'Number of Emergency Visits', 'value': 'number_emergency'},
            {'label': 'Number of Procedures', 'value': 'num_procedures'},
        ],
        value='num_lab_procedures'
    ),

    html.H2(id='selected-variable-title', style={'textAlign': 'center'}),
    dcc.Graph(id='selected_variable_plot'),

    html.H2("Time in Hospital vs Readmission Status", style={'textAlign': 'center'}),
    dcc.Graph(id='readmission_plot'),
])

# Static chart — renders once on load, independent of dropdown
@app.callback(
    Output('time_in_hospital_plot', 'figure')
)
def render_time_in_hospital_plot():
    fig = px.histogram(df, x='time_in_hospital', nbins=20, title='Distribution of Time in Hospital')
    fig.update_layout(xaxis_title='Time in Hospital', yaxis_title='Frequency', title_x=0.5)
    fig.update_traces(marker_line_width=1.5, marker_line_color='black')
    return fig

@app.callback(
    Output('selected_variable_plot', 'figure'),
    Output('selected-variable-title', 'children'),
    Input('variable-dropdown', 'value')
)
def update_selected_variable_plot(selected_variable):
    color_map = {
        'num_lab_procedures': ['#FF7F0E'],
        'number_diagnoses': ['#1F77B4'],
        'num_medications': ['#2CA02C'],
        'discharge_disposition_id': ['#D62728'],
        'number_outpatient': ['#9467BD'],
        'age': ['#8C564B'],
        'number_emergency': ['#E377C2'],
        'num_procedures': ['#7F7F7F'],
    }
    color = color_map.get(selected_variable, ['#17BECF'])

    fig = px.histogram(
        df, x=selected_variable, nbins=30,
        title=f'Distribution of {selected_variable}',
        color_discrete_sequence=color
    )
    fig.update_traces(marker_line_width=1.5, marker_line_color='black')
    fig.update_layout(
        xaxis_title=selected_variable.replace('_', ' ').title(),
        yaxis_title='Frequency', title_x=0.5
    )
    return fig, f"Selected Variable: {selected_variable.replace('_', ' ').title()}"

# Static chart — renders once on load, independent of dropdown
@app.callback(
    Output('readmission_plot', 'figure')
)
def render_readmission_plot():
    fig = px.histogram(
        df, x='time_in_hospital', color='readmitted',
        barmode='group', title='Time in Hospital vs Readmission Status'
    )
    fig.update_layout(xaxis_title='Time in Hospital (Days)', yaxis_title='Frequency', bargap=0.3, title_x=0.5)
    return fig

if __name__ == '__main__':
    debug = os.getenv('DASH_DEBUG', 'false').lower() == 'true'
    app.run_server(debug=debug, port=8054)

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
 
# Load the dataset
df = pd.read_csv('cleaned_diabetic_data_with_Median 1.csv')
 
# Initialize the Dash app
app = dash.Dash(__name__)
 
# Define the layout of the app
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
            {'label': 'Number of Discharge Disposition ID', 'value': 'discharge_disposition_id'},
            {'label': 'Number of Out Patient', 'value': 'number_outpatient'},
            {'label': 'Age', 'value': 'age'},
            {'label': 'Number of Emergency', 'value': 'number_emergency'},
            {'label': 'Number of Procedures', 'value': 'num_procedures'},
        ],
        value='num_lab_procedures'  # Default value
    ),
 
    html.H2(id='selected-variable-title', style={'textAlign': 'center'}),
    dcc.Graph(id='selected_variable_plot'),
 
    html.H2("Time in Hospital vs Readmission Status", style={'textAlign': 'center'}),
    dcc.Graph(id='readmission_plot'),
])
 
# Define the callback for the first plot (Time in Hospital)
@app.callback(
    Output('time_in_hospital_plot', 'figure'),
    Input('variable-dropdown', 'value')
)
def update_time_in_hospital_plot(selected_variable):
    fig = px.histogram(df, x='time_in_hospital', nbins=20, title='Distribution of Time in Hospital')  # Adjusted number of bins
    fig.update_layout(xaxis_title='Time in Hospital', yaxis_title='Frequency', title_x=0.5)  # Center-align title
    fig.update_traces(marker_line_width=1.5, marker_line_color='black')
    return fig
 
# Define the callback for the selected variable plot
@app.callback(
    Output('selected_variable_plot', 'figure'),
    Output('selected-variable-title', 'children'),
    Input('variable-dropdown', 'value')
)
def update_selected_variable_plot(selected_variable):
    # Define a color scheme based on the variable
    color_map = {
        'num_lab_procedures': ['#FF7F0E'],  # Orange
        'number_diagnoses': ['#1F77B4'],  # Blue
        'num_medications': ['#2CA02C'],  # Green
        'discharge_disposition_id': ['#D62728'],  # Red
        'number_outpatient': ['#9467BD'],  # Purple
        'age': ['#8C564B'],  # Brown
        'number_emergency': ['#E377C2'],  # Pink
        'num_procedures': ['#7F7F7F'],  # Gray
    }
   
    # Use the color from the color map or default to a standard color
    color = color_map.get(selected_variable, ['#17BECF'])  # Teal as default
 
    # Create the histogram with an outline for the bars
    fig = px.histogram(
        df,
        x=selected_variable,
        nbins=30,
        title=f'Distribution of {selected_variable}',
        color_discrete_sequence=color
    )
   

    fig.update_traces(marker_line_width=1.5, marker_line_color='black')
   
    fig.update_layout(xaxis_title=selected_variable.replace('_', ' ').title(), yaxis_title='Frequency')
   
    return fig, f"Selected Variable: {selected_variable.replace('_', ' ').title()}"
 

@app.callback(
    Output('readmission_plot', 'figure'),
    Input('variable-dropdown', 'value')
)
def update_readmission_plot(selected_variable):
    fig = px.histogram(df, x='time_in_hospital', color='readmitted', barmode='group', title='Time in Hospital vs Readmission Status')
    fig.update_layout(xaxis_title='Time in Hospital (Days)', yaxis_title='Frequency', bargap=0.3, title_x=0.5)  # Center-align title
    return fig
 

if __name__ == '__main__':
    app.run_server(debug=True, port=8054)
 
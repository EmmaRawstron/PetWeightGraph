"""
Author: Emma Rawstron
Date: 5/19/2029
Description: Script for visualizing pet data.
This script reads pet data from a CSV file, generates a plotly figure with two subplots, 
and exports the figure as an HTML file.
"""

import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Load the data
df = pd.read_csv('pet_data.csv')

# Calculate total weights, counts and average weights
totalWeights = df.groupby('species')['weight'].sum()
totalCount = df.groupby('species')['weight'].count()
averageWeight = df.groupby('species')['weight'].mean()

# Define the dictionary for grammatically corrected species names
species_names = {
    'cat': 'Cats',
    'dog': 'Dogs',
    'shinglebackLizard': 'Shingleback Lizards'
}

species_names2 = ['Cats', 'Dogs', 'Shingleback Lizards']

# Calculate individual weights and map to appropriate colors
species_to_color = {'cat': 'pink', 'dog': 'cyan', 'shinglebackLizard': 'lightgreen'}
df['color'] = df['species'].map(species_to_color)

# Create a list of colors corresponding to the index order of totalWeights
color_ordered = [species_to_color[species] for species in totalWeights.index]

# Create subplot figure
fig = make_subplots(rows=2, cols=1)


# Add total weights bar chart
fig.add_trace(
    go.Bar(x=species_names2, 
           y=totalWeights, 
           marker_color=color_ordered, 
           name='Total', 
           legendgroup="total", 
           showlegend=False,
           hoverinfo='skip',  # Skip the default hoverinfo
           hovertemplate='<b>Total Weight</b>: %{y} lb<br>' +
                         '<b>Total Count</b>: '+ totalCount.map(str) + ' %{x}s' + '<br>' +
                         '<b>Average Weight</b>: ' + averageWeight.round(2).map(str) + ' lb' +
                         '<extra></extra>'),  # Custom hover template with no extra info
    row=1, col=1
)

# Update the y domain of the first subplot to make it taller
#fig.update_yaxes(domain=[0.55, 1.0], row=1, col=1)

# Add individual weights bar chart
for species in df['species'].unique():
    df_species = df.loc[df['species']==species]
    fig.add_trace(
        go.Bar(x=df_species['petID'], 
               y=df_species['weight'], 
               marker_color=species_to_color[species], 
               name=species, 
               legendgroup=species, 
               hoverinfo='skip',  # Hide the default hoverinfo
               hovertemplate=
                '<br><b>Weight</b>: %{y} lb<br><extra></extra>'),
        row=2, col=1
    )
    
# Update the y domain of the second subplot to make it taller
#fig.update_yaxes(domain=[0.0, 0.45], row=2, col=1)

# Update layout
fig.update_layout(
    #autosize=True,
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            active=0,
            x=0.36,
            y=1.055,
            buttons=list([
                dict(label="All",
                     method="update",
                     args=[{"visible": [True, True, True, True]}]),
                dict(label="Cats",
                     method="update",
                     args=[{"visible": [True, False, True, False]}]),
                dict(label="Dogs",
                     method="update",
                     args=[{"visible": [True, True, False, False]}]),               
                dict(label="Shingleback Lizards",
                     method="update",
                     args=[{"visible": [True, False, False, True]}]),
            ]),
        )
    ],
    width=1000,   # Adjust this value to set the width
    height=800,  # Adjust this value to set the height
    title="Pet Weights Comparison",
    title_x=0.5,  # This places the title in the center
    legend=dict(
        x=1,  # Adjust these values to position the legend
        xanchor='auto',  # This anchors the legend to the right
        y=1,  # Adjust these values to position the legend
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),
        bgcolor="white",
        bordercolor="Black",
        borderwidth=1
    )
)

# Update the species names in the legend and x-axis labels
fig.for_each_trace(lambda t: t.update(name=species_names.get(t.name, t.name)))

# Add x-axis and y-axis labels for the first subplot
#fig.update_xaxes(title_text="Species", row=1, col=1)
fig.update_yaxes(title_text="Total Weight", row=1, col=1)

# Add x-axis and y-axis labels for the second subplot
fig.update_xaxes(title_text="Pet ID", tickfont=dict(size=10), row=2, col=1)
fig.update_yaxes(title_text="Weight (pounds)", row=2, col=1)

fig.write_html('pet_graph.html')
# Pet Data Visualization Project

This project visualizes data from a pet dataset using Python and Plotly. The dataset includes information about the pet's ID, species, and weight. The visualization includes two subplots showing total weights by species and individual weights by pet ID.

## Data

The dataset used for this project, 'pet_data.csv', includes the following columns:

- 'petID': Unique identifier for each pet.
- 'species': The species of the pet ('cat', 'dog', or 'shingleback lizard').
- 'weight': The weight of the pet.

## Visualization

The visualization includes two bar charts in a subplot format:

1. The top subplot shows the total weight for each species.
2. The bottom subplot shows the weight of each individual pet, grouped by species.

You can use the buttons below the title to switch between different species in the bottom subplot.

## Setup and Usage

To use this project, follow these steps:

1. Clone this repository: `git clone https://github.com/EmmaRawstron/PetWeightGraph.git`.
2. Install the required Python packages: `pip install pandas plotly`.
3. Run the Python script: `python pet_weight_data_viz.py`.
4. Open the generated 'pet_graph.html' file in your browser to view the visualization.

This project also includes a 'myplot.html' file, which is a standalone HTML file containing the visualization. You can view this file in any web browser.

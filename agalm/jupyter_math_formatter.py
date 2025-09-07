import json
import os

current_dir = os.getcwd()

HOMEWORK_PATH = current_dir + '/homework/'
ASSIGNMENT = HOMEWORK_PATH + 'Homework_8.ipynb' # << Change this string to the title of the notebook

# Load the notebook
with open(ASSIGNMENT, 'r') as file:
    notebook = json.load(file)

# Iterate through the cells and replace the text in markdown cells
for cell in notebook['cells']:
    if cell['cell_type'] == 'markdown':
        source = cell['source']
        updated_source = []
        for line in source:
            line = line.replace(r'\[', '$$').replace(r'\]', '$$')
            line = line.replace(r'\(', '$').replace(r'\)', '$')
            updated_source.append(line)
        cell['source'] = updated_source

# Save the updated notebook
with open(ASSIGNMENT, 'w') as file:
    json.dump(notebook, file, indent=2)

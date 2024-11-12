# Bootcamp_project_1

Mental health and substance use disorders death rate by age group, United States, 2021
Estimated annual number of deaths by age group from mental health and substance use disorders per 100,000 people in the same age group. These include alcohol use, drug use, and eating disorders. Figures do not include deaths resulting from suicide, which are related to these disorders.


Source and citation
Data sources: 
•	World Health Organization (2024)
 Cite this work
Our articles and data visualizations rely on work from many different people and organizations. When citing this topic page, please also cite the underlying data sources. This topic page can be cited as:

Saloni Dattani, Lucas Rodés-Guirao, Hannah Ritchie and Max Roser (2023) - “Mental Health” Published online at OurWorldinData.org. Retrieved from: 'https://ourworldindata.org/mental-health' [Online Resource]

BibTeX citation

@article{owid-mental-health,
    author = {Saloni Dattani and Lucas Rodés-Guirao and Hannah Ritchie and Max Roser},
    title = {Mental Health},
    journal = {Our World in Data},
    year = {2023},
    note = {https://ourworldindata.org/mental-health}
}– with major processing by Our World In Data

Our World In Data - Data APIs
https://docs.owid.io/projects/etl/api/

Python with Pandas:

import pandas as pd
import requests

# Fetch the data
df = pd.read_csv("https://ourworldindata.org/grapher/death-rates-from-mental-and-substance-disorders-by-age-who.csv?v=1&csvType=full&useColumnShortNames=true")

# Fetch the metadata
metadata = requests.get("https://ourworldindata.org/grapher/death-rates-from-mental-and-substance-disorders-by-age-who.metadata.json?v=1&csvType=full&useColumnShortNames=true").json()

Excel / Google Sheets
=IMPORTDATA("https://ourworldindata.org/grapher/death-rates-from-mental-and-substance-disorders-by-age-who.csv?v=1&csvType=full&useColumnShortNames=true")


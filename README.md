<<<<<<< Jake
=======
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
# Bootcamp_project_1
>>>>> jake/megan/shiki
10/29 Searched for data sources created plan to find data regarding substance abuse and mental health facilities
10/31 Finalized plan for subtance abuse, sent final plan to project proposals
11/04 Began sorting and cleaning data. posted first complete graph "Substance abuse related deaths by country"
11/05 Added markdowns created plan for more accurate findings based on population and amount of people using in the specific area vs amount of facilities available
11/07 Cleaned up other data sources, combined "api" into google maps to track amount of facilities and finalized interactive map.
11/08 Abandoned googlemaps api pulled data from samhsa applied research on python Nominatim and made appropriate maps

This project pulls data and cleans it from samhsa, kaggle, NCHS, and CDC. It sorts the data and creates graphs for a better visualization and understanding. 
The sorted data shows an increase of substance abuse and substance abuse related deaths across the world. The data also displays the visualization in New York counties, 
Erie and Westchester while having similar population and amount of treatment facilities Erie displays a higher amount of admissions related to substance abuse. 
This project is meant to shed light on substance abuse and the impact it has on the united states. While having facilities around is beneficial other factors should be considered
in stemming substance abuse. 

Sources are listed in collected CSV_files located in the folder.
=======

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

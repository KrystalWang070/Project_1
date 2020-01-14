# Linguistic Demographics in the United States
### K. Wang, M. Kuhn, and N. Dieck

## Introduction
The United States is a diverse country with more than 300 language groups tracked by the United States Census Bureau through the American community survey. The 2013 ACS includes national and state data as well as data for 100 of the largest urban areas. The geographic distribution of linguistic groups has major implications for effective resource distribution. _Lingustic Demographics in the United States_ is a study of what the US Census can tell us about what languages are spoken in the United States, how many people speak those languages, and where speakers are located. 

## Repository Content
The repository has five files in it as follow:

The package consists of two executibles in the form of Jupyter Notebooks, in total requires five files to run. The first four are included in the repository and the fifth must be created by the user. 
* Project_1_Collection.ipynb - _This is the notebook used for collecting, orgnizing, and exporting the Census data._
* Project_1_Analysis.ipynb - _This is the notebook used for analyzing the collected data and exporting the visualizations for further use._
* functions.py - _Several functions referenced by the data analysis notebook are stored in a separate Python file. The program will not run without these functions._
* state_code.csv - _A list of state FIPS codes that is subsequently referenced by the data analysis notebook. The program will not run without this file._
* apikey.py - _Stores the user's API Key for the Census Bureau. The data collection program requires this file to run._

The repository also includes a PowerPoint presentation (.pdf) covering the key findings of the analysis. 

## Setup and Use

1. Create a new file called apikey.py in the directory. Add your US Census API Key to the file apikey.py as a variable called api_key. For example, api_key = 1234567890abc
1. Run Project_1_Collection.ipynb.
    * The primary purpose of this file is to create two CSVs to be used by the analysis program. 
    * The first CSV breaks down the number and percentage of speakers of French, Chinese and Spanish across the 100 urban areas (Covering 155 counties). 
    * The second CSV breaks down all languages spoken in Cook County by number of speakers. 
1. Run Project_1_Analysis.ipynb.
    * There are three blocks of analysis to be found in this program.
    * First, bar chart summaries are created for French, Chinese and Spanish speakers in the 155 counties and overall. For the 155 counties, only the top counties are displayed.
    * Second, the county percentages are replicated as heatmaps using gmap functionality. 
    * Finally, the representation of different languages in Cook County is calculated in tabular and graphical format. 


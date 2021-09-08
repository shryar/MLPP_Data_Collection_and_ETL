#source: https://jtleider.github.io/censusdata/

#import pandas as pd
import censusdata
import psycopg2


colblocks = censusdata.geographies(censusdata.censusgeo([('state', '08'), ('county', '*'), 
                                                         ('block group', '*')]), 'acs5', 2019) 
#block group data for the state of Colorado


coldata = censusdata.download('acs5', 2019,
                             censusdata.censusgeo([('state', '08'), ('county', '*'), ('block group', '*')]),
                             ['B23025_003E', 'B23025_005E', 'B15003_017E', 'B15003_018E',
                              'B15002_011E', 'B15002_015E', 'B15002_028E', 'B15002_032E'])
#download data in to a pandas dataframe with the variables below:



""" Variable names:
B23025_003E',  Estimate!!Total:!!In labor force:!!Civilian labor force:
'B23025_005E', Estimate!!Total:!!In labor force:!!Civilian labor force:!!Unemployed
'B15003_017' 'Estimate!!Total:!!Regular high school diploma	EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVERE'
'B15003_018E' Estimate!!Total:!!GED or alternative credential	EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER
B15002_011E	Estimate!!Total:!!Male:!!High school graduate (includes equivalency)	SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER
B15002_015E	Estimate!!Total:!!Male:!!Bachelor's degree	SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER
B15002_028E	Estimate!!Total:!!Female:!!High school graduate (includes equivalency)	SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER
B15002_032E	Estimate!!Total:!!Female:!!Bachelor's degree	SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER
"""

coldata.reset_index(drop=True, inplace=True) #replace blocks with dummy numbers for now - this is quick data cleaning
coldata = coldata.rename(columns={'B23025_003E': 'total_labor_force', #rename df columns for variables of interest
                                  'B23025_005E': 'total_unemployed', 
                                  'B15003_017E': 'total_hs',
                                  'B15003_018E': 'total_ged',
                                  'B15002_011E': 'male_hs_grad', 
                                  'B15002_015E': 'male_bachelors', 
                                  'B15002_028E': 'female_hs_grad', 
                                  'B15002_032E': 'female_bachelors'})


coldata.to_csv("./ColoradoData.csv") #output to CSV file for import through psycopg2 or OHIO

conn = psycopg2.connect("host=acs-db.mlpolicylab.dssg.io dbname=acs_data_loading user=mlpp_student password=CARE-horse-most port=5432")
cur = conn.cursor()

cur.execute("""CREATE TABLE ACS.SSAHMAD_ACS_DATA(
            block_info TEXT, 
            total_labor_force INTEGER, 
            total_unemployed INTEGER, 
            total_hs INTEGER, 
            total_ged INTEGER, 
            male_hs_grad INTEGER, 
            male_bachelors INTEGER, 
            female_hs_grad INTEGER, 
            female_bachelors_grad INTEGER)""")

conn.commit()

with open('ColoradoData.csv', 'r') as f:
    next(f) # Skip the header row.
    cur.copy_from(f, 'acs.ssahmad_acs_data', sep=',')

conn.commit()
















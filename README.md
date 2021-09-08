# MLPP_Data_Collection_and_ETL
Week 1 of MLPP Fall 2021


I utilized the inbuilt Census Data package for python 'censusdata' that allows data to be quickly imported in to a pandas dataframe for quick and easy manipulation (source: https://jtleider.github.io/censusdata/)

This was faster than setting up an API call. 
I chose Colorado as my prefered US state (because of less population) and also becuase its geographically closest to a rectangle.

My **variables of interest** were the total civilian labor force, total unemployed labor force, total highschool diplomas attained, total GED or alternate credentials attained by the population, and both male and female estimates of high school and university graduates: 
 
 - 'B23025_003E'  Estimate!!Total:!!In labor force:!!Civilian labor force:
 - 'B23025_005E' Estimate!!Total:!!In labor force:!!Civilian labor force:!!Unemployed
 - 'B15003_017' Estimate!!Total:!!Regular high school diploma	EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVERE'
 - 'B15003_018E' Estimate!!Total:!!GED or alternative credential	EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER
 - 'B15002_011E'	Estimate!!Total:!!Male:!!High school graduate (includes equivalency)	SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER
 - 'B15002_015E'	Estimate!!Total:!!Male:!!Bachelor's degree	SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER
 - 'B15002_028E'	Estimate!!Total:!!Female:!!High school graduate (includes equivalency)	SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER
 - 'B15002_032E'	Estimate!!Total:!!Female:!!Bachelor's degree	SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER

These variables are the standards used for economic analysis, and provides both labor particpation, education level, and gender dis-aggregation. Hence, a lot of detailed analysis can be undertaken with just these 8 variables. I selected the age group of 25 years and older (rather than 18 and older) to allow for college graduates to enter the job market.

After 'cleaning' the data (basically dropping the index because it was a long string with multiple separators and a nightmare to modify), I converted the dataframe in to a CSV file to push to the database.

I had some trouble using psycopg2 to push the CSV data (~3500 rows) to the db table (I used the 'Copy from' method described here: https://www.dataquest.io/blog/loading-data-into-postgres/) and thus had to abandon it in order to submit the link.

Overall, I'm satisfied with my effort despite the hitch at the end (the SQL table is ready, only need to push the data through) given that I was travelling from Thursday-Monday and only had time after the lecture today to start the assignment.

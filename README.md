# Final_Project_PAI789


Summary

The purpose of this script is to compare the date at which states implemented 
stay at home orders and the predicted deaths per state as well as the predicted
length of social distancing measures. 

Input Data

There are two data sets used for this project. One is a csv file that contains 
dates social distancing measures were implemented as well as predicted deaths 
per state normalized by population and the predicted date at which social 
distancing measures can be relaxed by state. This data was compiled from The 
Institute for Health Metrics and Evaluation (IHME), an independent global 
health research center at the University of Washington.(I was unable to get 
access to a raw data file that contained the information so I ended up creating
one).
https://covid19.healthdata.org/united-states-of-america/district-of-columbia

The second data set is from the NYTimes Covid data on cases and deaths per 
state. It can be accessed here: https://github.com/nytimes/covid-19-data.

DELIVERABLES

A python script called social_distancing.py that merges the csv file with NYTimes
Covid data by state and three linear regression plots. One showing the correlation
between the number of deaths in states at the time stay at home orders 
were implemented and the number of predicted deaths. Another showing he correlation
between the number of cases in states at the time stay at home orders 
were implemented and the number of predicted deaths. And a third showing the 
number of cases at the time stay at home orders were implemented and the predicted
duration of social distancing measures. 

INSTRUCTIONS

1. Import pandas and seaborn libraries

2. Set ny_covid equal to pd.read_csv('us-states.csv')

3. Set states_info equal to pd.read_csv('states_info.csv')

4. Drop states that have not yet implemented a stay at home order from states_info
by using the dropna function to drop rows that are blank in the 'stay_at_home_order'
column. Call this file states_info_updated

5. Attach the prefix ny_ to the column names in the ny_covid data using add_prefix
and call this file ny_covid_updated

6. Remove the prefix ny_ from the fips column in the ny_covid_updated by renaming
the column ny_fips = fips

7. Merge the two files using a left join, with states_info_updated as the left 
dataframe and ny_covid_updated as the right dataframe. Use an outer, 1 to many 
merge. The resulting file should have multiple entries per state from the ny_covid 
data.

8. Drop the '_merge' column

9. Create a new column called 'deaths_per_100,000_at_close that is equal to 
ny_deaths divided by population multiplied by 100,000 and rounded to 2 decimal 
spaces.

10. Create a new column called 'cases_per_100,000_at_close that is equal to 
ny_cases divided by population multiplied by 100,000 and rounded to 2 decimal 
spaces.

11. Convert 'stay_at_home_order' and 'ny_date' to string format

12. Use boolean indexing to check when 'stay_at_home_order' is equal to 'ny_date'

13. Create a new dataframe that equals the rows where 'stay_at_home_order' is 
equal to 'ny_date'

14. Use regplot to plot a linear regression with 'deaths_per_100,000_at_close'
on the x-axis and 'total_predicted_deaths_per_100,000' on the y-axis.
This gives a linear regression of the total number of deaths on the date that 
the stay at home order was implemented and the total predicted deaths.

15. Use regplot to plot a linear regression with 'cases_per_100,000_at_close'
on the x-axis and 'total_predicted_deaths_per_100,000' on the y-axis. This gives 
a linear regression of the total number of cases on the date that the stay at 
home order was implemented and the total predicted deaths.

16. Convert 'end' and 'stay_at_home_order' to datetime format (pd.to_datetime)
'end' is the predicted date that the social distancing measures can be relaxed
according to IHME

17. Use dtypes to check the datatype of each column. 'end' and 'stay_at_home_order'
should now be in datetime64[ns] format

18. Create a column called 'duration' that is equal to 'stay_at_home_order' 
subtracted from 'end'. This will give you the time difference between the two or
the predicted duration of social distancing measures.

19. Convert 'duration' to string

20. Create a new column named 'duration_days' and set it equal to 
str.slice(stop=2) so that only the number of days is remaining in the 
duration column

21. Convert 'cases_per_100,000_at_close' to string format

22. Create a new column called 'cases_per_100,000_at_close_clean' that is equal 
to 'cases_per_100,000_at_close' split before the decimal point using 
.apply(lambda x: x.split('.')[0])  so that only values before the decimal are 
included. 

23. Convert 'cases_per_100,000_at_close_clean' and 'duration_days' to float
format

24. Use regplot to plot a linear regression with 'cases_per_100,000_at_close_clean'
on the x-axis and 'duration_days' on the y-axis. This gives a linear regression 
of the total number of cases on the date that the stay at home order was 
implemented and the duration of the social distancing measures.







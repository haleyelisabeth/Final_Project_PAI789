# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

import seaborn as sns

ny_covid = pd.read_csv('us-states.csv')

states_info = pd.read_csv('states_info.csv')

states_info_updated = states_info.dropna(axis=0, how='any', thresh=None, subset=['stay_at_home_order'], inplace=False)


ny_covid_updated = ny_covid.add_prefix('ny_')

ny_covid_updated.rename(columns = {'ny_fips':'fips'}, inplace = True)



df = pd.merge(states_info_updated, ny_covid_updated, on = 'fips', how = 'outer', validate = "1:m", indicator = True)

df.drop('_merge', axis='columns', inplace=True)

df['deaths_per_100,000_at_close'] = round(df['ny_deaths'] / df['population']*100000,2)

df['cases_per_100,000_at_close'] = round(df['ny_cases'] / df['population']*100000,2)


df['stay_at_home_order'] = df['stay_at_home_order'].astype(str)
df['ny_date'] = df['ny_date'].astype(str)

print (df['stay_at_home_order'] == df['ny_date'])

dff = df[df['stay_at_home_order'] == df['ny_date']]
print (dff)


sns.regplot(x=dff['deaths_per_100,000_at_close'], y=dff['total_predicted_deaths_per_100,000'])

sns.regplot(x=dff['cases_per_100,000_at_close'], y=dff['total_predicted_deaths_per_100,000'])


#Adding another column for the predicted duration of social distancing measures
dff['end'] = pd.to_datetime(dff['end'])
dff['stay_at_home_order'] = pd.to_datetime(dff['stay_at_home_order'])

dff.dtypes 

dff['end'] - dff['stay_at_home_order']

dff['duration'] = dff['end'] - dff['stay_at_home_order']

dff['duration'] = dff['duration'].astype(str)

dff['duration_days'] = dff['duration'].str.slice(stop=2)

dff['cases_per_100,000_at_close'] = dff['cases_per_100,000_at_close'].astype(str)

dff['cases_per_100,000_at_close_clean']= dff['cases_per_100,000_at_close'].apply(lambda x: x.split('.')[0])
 

dff['cases_per_100,000_at_close_clean'] = dff['cases_per_100,000_at_close_clean'].astype(float)

dff['duration_days'] = dff['duration_days'].astype(float)

sns.regplot(x=dff['cases_per_100,000_at_close_clean'], y=dff['duration_days'])

dff.to_csv('final_file.csv')







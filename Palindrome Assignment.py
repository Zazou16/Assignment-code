import pandas as pd
import matplotlib.pyplot as plt

path_to_file = '/Users/zanelemadikane/Desktop/Palindrome Interview Data.csv'

df = pd.read_csv(path_to_file)
							
#taking a look at the data
print(df.head)

#checking columns
print(df.columns)

#checking data types for each column
print(df.dtypes)

#check missing values
print(df.isnull().sum())

#checking how many entries for each district
print(df['District'].value_counts())


#Q2:  a) What is the total number of people living with HIV (NoPLHIV)
#in the listed districts according to the Survey estimate?

total_noplhiv_survey = df[df['Estimate'] =='Survey']['NoPLHIV'].sum()

print(total_noplhiv_survey)

#b)  WhatistheaverageNoPLHIVofthetwoestimatesusedfor“Xhariep”?

Xhariep_noplhiv_avg = df[df['District'].str.contains("Xhariep")]['NoPLHIV'].mean()
print(Xhariep_noplhiv_avg)

#c Add a column and populate it with the number of people not living with HIV
#for each row.

df['NOTHIV'] = df['NoPLHIV_UCL'] - df['NoPLHIV']

#print(df['NOTHIV'])

#d WhatisthetotalNoPLHIVinallthecities(districtswith“city”or“metro”inthename)?

total_cities_noplhiv = df[df['District'].str.contains("city|metro", case=False, na=False)]['NoPLHIV']
print(total_cities_noplhiv)

totalpl_cities_nohivd = df[df['District'].str.contains("city|metro", case=False, na=False)]['NoPLHIV'].sum()

print(totalpl_cities_nohivd)

df.columns = df.columns.str.replace(r'[^A-Za-z0-9_]+', '', regex=True)

print(df.columns)

#e)  Filter district ends in "i" and Fay Heriott

district_end_i = df[(df['District'].str.endswith("i", na=False)) & (df['Estimate'] == 'Fay-Heriott')]
              
print(district_end_i)

#f)  ploteachPrevalenceconfidenceinterval(Prevalence_UCLand Prevalence_LCL)
#for Districts that end in “i”; according to Fay-Herriott estimates on 1 graph.

plt.figure(figsize = (10,6))

for index, row in district_end_i.iterrows():
    plt.plot([row['Prevalence_LCL'], row['Prevalence_UCL']],
             [row['District'], row['District']], 'bo-', label="Confidence Interval")

plt.title('Prevalence Confidence Intervals (Fay-Herriott Estimates) for Districts ending in "i"')
plt.xlabel('Prevalence (%)')
plt.ylabel('Districts')
plt.grid(True)
plt.show()

df['Prevalence_'].hist(bins=20)
plt.title('Distribution of HIV Prevalence')
plt.xlabel('Prevalence (%)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(12,6))
df.groupby('District')['Prevalence_'].mean().plot(kind='bar')
plt.title('HIV Prevalence by District')
plt.xlabel('District')
plt.ylabel('Prevalence (%)')
plt.xticks(rotation=90)
plt.show()

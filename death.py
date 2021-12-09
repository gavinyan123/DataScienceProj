# Name: Gavin Yan
# Email: gavin.yan20@myhunter.cuny.edu
# Resources: pydata.org

import pandas as pd
import pandasql as psql
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('New_York_City_Leading_Causes_of_Death.csv')

dfQuery = 'SELECT Year, "Leading Cause" as "Cause", Sex, "Race Ethnicity", Deaths from df'
dfAgg = psql.sqldf(dfQuery)
dfAgg['Deaths'] = dfAgg['Deaths'].str.replace('.', '0', regex=False).astype(int)
dfAgg.loc[(dfAgg['Sex'] == "Female", 'Sex')] = "F"
dfAgg.loc[(dfAgg['Sex'] == "Male"), 'Sex'] = "M"
female = len(dfAgg[dfAgg.Sex == "F"])
male = len(dfAgg[dfAgg.Sex == "M"])
genderData = [female, male]

#Race Count
topCauseQuery = 'SELECT Cause, "Race Ethnicity", SUM(Deaths) as "Heart Diseases Death Count" from dfAgg WHERE Cause == "Diseases of Heart (I00-I09, I11, I13, I20-I51)" GROUP BY "Race Ethnicity"'
topRace = psql.sqldf(topCauseQuery)
del topRace['Cause']
secondCauseQuery = 'SELECT Cause, "Race Ethnicity", SUM(Deaths) as "Malignant Neoplasms Death Count" from dfAgg WHERE Cause == "Malignant Neoplasms (Cancer: C00-C97)" GROUP BY "Race Ethnicity"'
secondRace = psql.sqldf(secondCauseQuery)
del secondRace['Cause']
thirdCauseQuery = 'SELECT Cause, "Race Ethnicity", SUM(Deaths) as "Other Death Count" from dfAgg WHERE Cause == "All Other Causes"  GROUP BY "Race Ethnicity"'
thirdRace = psql.sqldf(thirdCauseQuery)
del thirdRace['Cause']
fourthCauseQuery = 'SELECT Cause, "Race Ethnicity", SUM(Deaths) as "Influenza and Pneumonia Death Count" from dfAgg WHERE Cause == "Influenza (Flu) and Pneumonia (J09-J18)"  GROUP BY "Race Ethnicity"'
fourthRace = psql.sqldf(fourthCauseQuery)
del fourthRace['Cause']
fifthCauseQuery = 'SELECT Cause, "Race Ethnicity", SUM(Deaths) as "Diabetes Death Count" from dfAgg WHERE Cause == "Diabetes Mellitus (E10-E14)"  GROUP BY "Race Ethnicity"'
fifthRace = psql.sqldf(fifthCauseQuery)
del fifthRace['Cause']

firstMerge = pd.merge(topRace, secondRace, on=["Race Ethnicity"])
secondMerge = pd.merge(thirdRace, fourthRace, on=["Race Ethnicity"])
thirdMerge = pd.merge(firstMerge, secondMerge, on=["Race Ethnicity"])
race = pd.merge(thirdMerge, fifthRace, on=["Race Ethnicity"])
# race = race.set_index('Race Ethnicity')
# race = race.transpose()
# race = race.reset_index()
# race = race.rename(columns={"index":"Cause"})

#Sum of deaths for all Causes
uniqueQuery = 'SELECT Cause, SUM(Deaths) as Deaths from dfAgg GROUP BY Cause'
uniqueAgg = psql.sqldf(uniqueQuery)
deathCause = uniqueAgg.sort_values(['Deaths'], ascending = False).head()

#2007 sum deaths
year7Q = 'SELECT * from dfAgg WHERE Year == 2007'
year7Agg = psql.sqldf(year7Q)
sum2007 = year7Agg['Deaths'].sum()
female7 = len(year7Agg[year7Agg.Sex == "F"])
male7 = len(year7Agg[year7Agg.Sex == "M"])

# 2008 sum deaths
year8Q = 'SELECT * from dfAgg WHERE Year == 2008'
year8Agg = psql.sqldf(year8Q)
sum2008 = year8Agg['Deaths'].sum()
female8 = len(year8Agg[year8Agg.Sex == "F"])
male8 = len(year8Agg[year8Agg.Sex == "M"])

#2009 sum deaths
year9Q = 'SELECT * from dfAgg WHERE Year == 2009'
year9Agg = psql.sqldf(year9Q)
sum2009 = year9Agg['Deaths'].sum()
female9 = len(year9Agg[year9Agg.Sex == "F"])
male9 = len(year9Agg[year9Agg.Sex == "M"])

#2010 sum deaths
year10Q = 'SELECT * from dfAgg WHERE Year == 2010'
year10Agg = psql.sqldf(year10Q)
sum2010 = year10Agg['Deaths'].sum()
female10 = len(year10Agg[year10Agg.Sex == "F"])
male10 = len(year10Agg[year10Agg.Sex == "M"])

#2011 sum deaths
year11Q = 'SELECT * from dfAgg WHERE Year == 2011'
year11Agg = psql.sqldf(year11Q)
sum2011 = year11Agg['Deaths'].sum()
female11 = len(year11Agg[year11Agg.Sex == "F"])
male11 = len(year11Agg[year11Agg.Sex == "M"])

#2012 sum deaths
year12Q = 'SELECT * from dfAgg WHERE Year == 2012'
year12Agg = psql.sqldf(year12Q)
sum2012 = year12Agg['Deaths'].sum()
female12 = len(year12Agg[year12Agg.Sex == "F"])
male12 = len(year12Agg[year12Agg.Sex == "M"])

#2013 sum deaths
year13Q = 'SELECT * from dfAgg WHERE Year == 2013'
year13Agg = psql.sqldf(year13Q)
sum2013 = year13Agg['Deaths'].sum()
female13 = len(year13Agg[year13Agg.Sex == "F"])
male13 = len(year13Agg[year13Agg.Sex == "M"])

#2014 sum deaths
year14Q = 'SELECT * from dfAgg WHERE Year == 2014'
year14Agg = psql.sqldf(year14Q)
sum2014 = year14Agg['Deaths'].sum()
female14 = len(year14Agg[year14Agg.Sex == "F"])
male14 = len(year14Agg[year14Agg.Sex == "M"])

#2015 sum deaths
year15Q = 'SELECT * from dfAgg WHERE Year == 2015'
year15Agg = psql.sqldf(year15Q)
sum2015 = year15Agg['Deaths'].sum()
female15 = len(year15Agg[year15Agg.Sex == "F"])
male15 = len(year15Agg[year15Agg.Sex == "M"])

#2016 sum deaths
year16Q = 'SELECT * from dfAgg WHERE Year == 2016'
year16Agg = psql.sqldf(year16Q)
sum2016 = year16Agg['Deaths'].sum()
female16 = len(year16Agg[year16Agg.Sex == "F"])
male16 = len(year16Agg[year16Agg.Sex == "M"])

#2017 sum deaths
year17Q = 'SELECT * from dfAgg WHERE Year == 2017'
year17Agg = psql.sqldf(year17Q)
sum2017 = year17Agg['Deaths'].sum()
female17 = len(year17Agg[year17Agg.Sex == "F"])
male17 = len(year17Agg[year17Agg.Sex == "M"])

#Make into Dataframe
yearlyData = {'Year': [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017],
            'Total deaths':[sum2007, sum2008, sum2009, sum2010, sum2011, sum2012, sum2013, sum2014, sum2015, sum2016, sum2017],
            'Female Deaths': [female7, female8, female9, female10, female11, female12, female13, female14, female15, female16, female17],
            'Male Deaths': [male7, male8, male9, male10, male11, male12, male13, male14, male15, male16, male17]}

sumYear = pd.DataFrame(yearlyData)

x = np.array([0,1,2,3,4,5,6,7,8,9,10])
y = np.array([0,1,2,3,4,5,6,7])
a_list = list(range(1,24))
b_list = list(range(1,142))


#Plot total deaths in each year
plt.plot(sumYear['Total deaths'])
plt.title('Total Number of Deaths by Year(2009-2017)')
plt.ylabel('Number of Deaths',fontsize= 14)
plt.xlabel('Year', fontsize = 14)
plt.xticks(x, sumYear['Year'])
plt.show()

#Plot difference between sex count total
labels = 'Female', 'Male'
fig1, ax = plt.subplots()
ax.pie(genderData, labels = labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax.axis('equal')
plt.title('Male vs Female Deaths')
plt.show()

#Plot difference between sex count yearly
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()

width = 0.2
sumYear['Female Deaths'].plot(kind='bar', color='red', ax=ax1, width=width,position=1)
sumYear['Male Deaths'].plot(kind='bar', color='blue', ax=ax2, width=width,position=0)

plt.title('Male vs Female Deaths')
ax1.set_ylabel('Number of Deaths',fontsize= 14)
plt.xlabel('Year', fontsize = 14)
plt.xticks(x, sumYear['Year'])
plt.show()

#Plot Race
plt.plot(race["Heart Diseases Death Count"], label = "Heart Disease")
plt.plot(race["Malignant Neoplasms Death Count"], label = "Malignant Neoplasms")
plt.plot(race["Other Death Count"], label = "Other")
plt.plot(race["Influenza and Pneumonia Death Count"], label = "Influenza and Pneumonia")
plt.plot(race["Diabetes Death Count"], label = "Diabetes")
plt.xticks(y, race['Race Ethnicity'])
plt.ylabel('Number of Deaths',fontsize= 14)
plt.legend()
plt.title('Race Death Comparison')
plt.show()

print(race)

# race.to_csv('test.csv', index = False)
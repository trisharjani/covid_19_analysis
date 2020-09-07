#!/usr/bin/env python
# coding: utf-8

# # Analysing the Spread of Covid-19 in India
# 

# #### Importing Relevant Packages 

# In[2]:


import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
print ('Modules are imported.')


# #### Importing Relevant Datasets

# In[3]:


#Daily cases nationally and by state; time-series - from Covid19India.com downloaded 1st Sept 2020
daily_national = pd.read_csv("datasets/India/national_case_time_series.csv")
daily_state = pd.read_csv("datasets/India/state_wise_overtime.csv")


# In[4]:


#Global data on a country level for India up to 28/08/2020 - may be reduntant later given above but use to cross-check
covid_dataset_csv = pd.read_csv("datasets/time_series_covid19_confirmed_global.csv")


# In[5]:


#Situation today state wise -  from Covid19India.com downloaded 1st Sept 2020
state_wise_cumulative = pd.read_csv("datasets/India/state_wise_today.csv")


# In[5]:


#Dataset displaying the number of hospital beds in India by State - from Kaggle, bookmarked 'Data-Source'
hospital_beds = pd.read_csv('datasets/India/hospital_beds_india.csv')


# In[6]:


#Dataset displaying Indian population - proxied on the number of Aadhar cards as the census is dated to 2011 by state 
# --> from Github
population = pd.read_csv('datasets/India/Indian_population_Aadhar.csv')


# In[265]:


#Dataset displaying testing by state - from Covid19India.com downloaded 5th Sept
testing = pd.read_csv('datasets/India/statewise_tested_numbers_data.csv')


# #### Exploring & Cleaning Datasets

# ##### 1)  Timeseries datasets:
# 

# In[155]:


daily_national.head() #Change dateformat to DD/MM/YYYY


# In[156]:


daily_national.shape


# In[157]:


daily_national.tail()


# In[158]:


daily_state.head() 


# In[159]:


daily_state.shape


# In[376]:


grouped_sets = daily_state.groupby(daily_state.Status)


# In[161]:


Cases_State = grouped_sets.get_group("Confirmed")


# In[162]:


Deaths_State = grouped_sets.get_group("Deceased")


# In[163]:


Recov_State = grouped_sets.get_group("Recovered")


# In[164]:


Cases_State.shape


# In[165]:


Deaths_State.shape


# In[166]:


Recov_State.head()


# In[167]:


Cases_State_bydate = pd.DataFrame(Cases_State.T)
Cases_State.head()


# In[168]:


Cases_State.drop(['Status'],axis =1, inplace = True)


# In[169]:


Cases_State.columns


# In[170]:


Cases_State.rename(columns={'TT':'Total', 'AN':'Andaman and Nicobar Islands', 'AP': 'Andhra Pradesh', 'AR': 'Arunachal Pradesh', 'AS':'Assam', 'BR':'Bihar', 'CH':'Chandigarh', 'CT':'Chhattisgarh', 'DN':'Dadra and Nagar Haveli', 'DD':'Daman and Diu',
       'DL':'Delhi', 'GA':'Goa', 'GJ':'Gujarat', 'HR':'Haryana', 'HP':'Himachal Pradesh', 'JK':'Jammu and Kashmir', 'JH':'Jharkhand', 'KA':'Karnataka', 'KL':'Kerala', 'LA':'Ladakh', 'LD':'Lakshadweep', 'MP':'Madhya Pradesh',
       'MH':'Maharashtra', 'MN':'Manipur', 'ML':'Meghalaya', 'MZ':'Mizoram', 'NL':'Nagaland', 'OR':'Odisha', 'PY':'Puducherry', 'PB':'Punjab', 'RJ':'Rajasthan', 'SK':'Sikkim', 'TN':'Tamil Nadu', 'TG':'Telangana',
       'TR':'Tripura', 'UP':'Uttar Pradesh', 'UT':'Uttarakhand', 'WB':'West Bengal', 'UN':'State Unassigned'},inplace=True)


# In[200]:


Cases_State['Date'] = pd.to_datetime(Cases_State.Date)


# In[212]:


Cases_State.set_index(['Date'],inplace=True)


# In[585]:


Cases_State.head(5)


# In[174]:


Recov_State.drop(['Status'],axis=1,inplace=True)


# In[176]:


Recov_State.rename(columns={'TT':'Total', 'AN':'Andaman and Nicobar Islands', 'AP': 'Andhra Pradesh', 'AR': 'Arunachal Pradesh', 'AS':'Assam', 'BR':'Bihar', 'CH':'Chandigarh', 'CT':'Chhattisgarh', 'DN':'Dadra and Nagar Haveli', 'DD':'Daman and Diu',
       'DL':'Delhi', 'GA':'Goa', 'GJ':'Gujarat', 'HR':'Haryana', 'HP':'Himachal Pradesh', 'JK':'Jammu and Kashmir', 'JH':'Jharkhand', 'KA':'Karnataka', 'KL':'Kerala', 'LA':'Ladakh', 'LD':'Lakshadweep', 'MP':'Madhya Pradesh',
       'MH':'Maharashtra', 'MN':'Manipur', 'ML':'Meghalaya', 'MZ':'Mizoram', 'NL':'Nagaland', 'OR':'Odisha', 'PY':'Puducherry', 'PB':'Punjab', 'RJ':'Rajasthan', 'SK':'Sikkim', 'TN':'Tamil Nadu', 'TG':'Telangana',
       'TR':'Tripura', 'UP':'Uttar Pradesh', 'UT':'Uttarakhand', 'WB':'West Bengal', 'UN':'State Unassigned'},inplace=True)


# In[178]:


Recov_State['Date'] = pd.to_datetime(Recov_State.Date)


# In[584]:


Recov_State.head()


# In[213]:


Recov_State.set_index(['Date'],inplace=True)


# In[180]:


Deaths_State.drop(['Status'],axis=1,inplace=True)


# In[181]:


Deaths_State.rename(columns={'TT':'Total', 'AN':'Andaman and Nicobar Islands', 'AP': 'Andhra Pradesh', 'AR': 'Arunachal Pradesh', 'AS':'Assam', 'BR':'Bihar', 'CH':'Chandigarh', 'CT':'Chhattisgarh', 'DN':'Dadra and Nagar Haveli', 'DD':'Daman and Diu',
       'DL':'Delhi', 'GA':'Goa', 'GJ':'Gujarat', 'HR':'Haryana', 'HP':'Himachal Pradesh', 'JK':'Jammu and Kashmir', 'JH':'Jharkhand', 'KA':'Karnataka', 'KL':'Kerala', 'LA':'Ladakh', 'LD':'Lakshadweep', 'MP':'Madhya Pradesh',
       'MH':'Maharashtra', 'MN':'Manipur', 'ML':'Meghalaya', 'MZ':'Mizoram', 'NL':'Nagaland', 'OR':'Odisha', 'PY':'Puducherry', 'PB':'Punjab', 'RJ':'Rajasthan', 'SK':'Sikkim', 'TN':'Tamil Nadu', 'TG':'Telangana',
       'TR':'Tripura', 'UP':'Uttar Pradesh', 'UT':'Uttarakhand', 'WB':'West Bengal', 'UN':'State Unassigned'},inplace=True)


# In[183]:


Deaths_State['Date'] = pd.to_datetime(Deaths_State.Date)


# In[184]:


Deaths_State.head() #Converted to YYYY-MM-DD


# In[214]:


Deaths_State.set_index(['Date'],inplace=True)


# In[185]:


#Transposing the data so that it's time-series
daily_state.set_index('Date')


# In[186]:


daily_bystate = pd.DataFrame(daily_state.T)
daily_bystate.head()


# In[187]:


#There are 171 days recorded in the daily_state dataset


# In[191]:


covid_dataset_csv.head() #Isolate India cases over time; drop rest


# In[192]:


covid_dataset_csv.drop(["Lat","Long"], axis =1, inplace = True)


# In[193]:


covid_aggregated = covid_dataset_csv.groupby("Country/Region").sum()


# In[195]:


covid_aggregated.head(2)


# In[616]:


covid_aggregated.columns = pd.to_datetime(covid_aggregated.columns)


# In[617]:


covid_aggregated.head(2)


# ##### 2) Cross-Sectional State Wise Data (Cumulative)

# In[7]:


state_wise_cumulative.head()
#Get rid of time only keep date in DD/MM/YYYY, delete total? 
#Active = Confirmed MINUS Recovered, Deaths & Migrated_Other


# In[8]:


state_wise_cumulative.shape


# In[9]:


state_wise_cumulative.set_index(['State'],inplace=True)


# In[10]:


state_cumulative = state_wise_cumulative.drop(['Delta_Confirmed','Delta_Recovered','Delta_Deaths'],axis=1)


# In[11]:


state_cumulative.head(2)


# ##### 3) Hospital Beds Data

# In[17]:


hospital_beds.head()


# In[269]:


hospital_beds.drop(['Sno'],axis=1,inplace=True)
hospital_beds.set_index(['State/UT'], inplace=True)


# In[282]:


hospital_beds.head(5)


# In[283]:


list(hospital_beds.columns)


# In[284]:


Beds_state = hospital_beds.drop(['NumPrimaryHealthCenters_HMIS',
 'NumCommunityHealthCenters_HMIS','NumSubDistrictHospitals_HMIS','NumDistrictHospitals_HMIS','TotalPublicHealthFacilities_HMIS','NumRuralHospitals_NHP18',
'NumUrbanHospitals_NHP18'],axis=1)


# In[285]:


Beds_state['Total No. of Beds'] = Beds_state['NumPublicBeds_HMIS'] + Beds_state['NumRuralBeds_NHP18'] + Beds_state['NumUrbanBeds_NHP18']


# In[286]:


Beds_state.head() #Assuming all 3 columns are independent counts so the Total is not double-counting!
#Also assuming these are ONLY PUBLIC facilities 


# In[287]:


Beds_state.rename(columns={'NumPublicBeds_HMIS':'No. of Public Beds', 'NumRuralBeds_NHP18':'No. of Beds in Rural Areas','NumUrbanBeds_NHP18':'No. of Beds in Urban Areas'},inplace=True)
Beds_state.head(4)


# ##### 4) Population Data based on Aadhar

# In[19]:


population.head()


# In[245]:


population.set_index(['State'],inplace=True)


# In[251]:


population.rename(columns={'Area (per sq km)': 'Area (sq km)','Aadhaar assigned as of 2019':'Population (based on Aadhar)'},inplace=True)


# In[252]:


population.head(2)


# In[261]:


population['Population Density (Persons per sq km)'] = population['Population (based on Aadhar)']/ population['Area (sq km)']
population = population.round({'Population Density (Persons per sq km)':0})


# In[ ]:


#Calculate population weighting?


# ##### 5) Testing in India

# In[485]:


testing.tail(5)


# In[486]:


testing.shape


# In[487]:


#Create a state-by-state cumulative dataframe & a time series dataframe by state


# In[488]:


#Checking which states are in the dataset
testing['State'].unique()


# In[550]:


list(testing.columns)


# In[558]:


useless_cols = ['Cumulative People In Quarantine','Total People Currently in Quarantine', 'Tag (People in Quarantine)',
                'Total People Released From Quarantine', 'People in ICU','People on Ventilators','Num Isolation Beds',
                'Num ICU Beds', 'Num Ventilators','Total PPE','Total N95 Masks','Corona Enquiry Calls',
                'Num Calls State Helpline','Source1','Source2', 'Source3','Unnamed: 31']


# In[587]:


testing_2 = testing.drop(useless_cols,axis=1)


# In[588]:


testing_2.head(5)


# In[589]:


testing_2.rename(columns ={'Updated On':'Date'}, inplace=True)


# In[607]:


testing_2.tail(200)


# In[591]:


#Creating a cumulative table:
testing_cross_sect = testing_2[testing_2.Date == '01/09/2020']


# In[592]:


testing_cross_sect.shape


# In[593]:


testing_cross_sect.set_index('State', inplace=True)


# In[603]:


testing_cross_sect.head(2)


# In[595]:


#Seperate by state
#Order by date -- currently in DD/MM/YYY
#Calculate difference from previous day to get moving average 


# In[618]:


testing_2.head()


# In[619]:


testing_2.sort_values(by='Date') #NOOOOO its doing 1st april, 1st may... instead of 1st april, 2nd april...


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#State by state, daily testing data:


# In[479]:


grouped_sets1 = testing_2.groupby('State')


# In[481]:


#35 Separate datasets:
AN = grouped_sets1.get_group("Andaman and Nicobar Islands")
AP = grouped_sets1.get_group("Andhra Pradesh")
AR = grouped_sets1.get_group("Arunachal Pradesh")
AS = grouped_sets1.get_group("Assam")
BR = grouped_sets1.get_group("Bihar")
CH = grouped_sets1.get_group("Chandigarh")
CT = grouped_sets1.get_group("Chhattisgarh")
DN = grouped_sets1.get_group("Dadra and Nagar Haveli and Daman and Diu")
DL = grouped_sets1.get_group("Delhi")
GA = grouped_sets1.get_group("Goa")
GJ = grouped_sets1.get_group("Gujarat")
HR = grouped_sets1.get_group("Haryana")
HP = grouped_sets1.get_group("Himachal Pradesh")
JK = grouped_sets1.get_group("Jammu and Kashmir")
JH = grouped_sets1.get_group("Jharkhand")
KA = grouped_sets1.get_group("Karnataka")
KL = grouped_sets1.get_group("Kerala")
LA = grouped_sets1.get_group("Ladakh")
MP = grouped_sets1.get_group("Madhya Pradesh")
MH = grouped_sets1.get_group("Maharashtra")
MN = grouped_sets1.get_group("Manipur")
ML = grouped_sets1.get_group("Meghalaya")
MZ = grouped_sets1.get_group("Mizoram")
NL = grouped_sets1.get_group("Nagaland")
OR = grouped_sets1.get_group("Odisha")
PY = grouped_sets1.get_group("Puducherry")
PB = grouped_sets1.get_group("Punjab")
RJ = grouped_sets1.get_group("Rajasthan")
SK = grouped_sets1.get_group("Sikkim")
YN = grouped_sets1.get_group("Tamil Nadu")
YG = grouped_sets1.get_group("Telangana")
TR = grouped_sets1.get_group("Tripura")
UP = grouped_sets1.get_group("Uttar Pradesh")
UT = grouped_sets1.get_group("Uttarakhand")
WB = grouped_sets1.get_group("West Bengal")


# In[482]:


AN.head(2)


# #### Visualising Recovered, Deaths & Confirmed Cases

# In[ ]:


#Objectives:
#let's try find top death rate
#let's try find top recovery rate too and see if it matches hospital capacity - trying to identify 'success stories'
#let's try to map general trends:
## 1 graph of cases daily for top 10, middle 10 and bottom 10 states
## 1 graph of national cases = daily_national showing the new cases, new conifrmed and deaths over time- differentiate


# In[218]:


Cases_State.tail(10)


# In[ ]:


#Visualising the top, middle and bottom 15 states, to find out which, we need to look at the cumulative dataset


# In[227]:


state_cumulative.head()


# In[237]:


population.head()


# In[243]:


population.head(2)


# In[12]:


state_cumulative.head(1)


# In[231]:


Top_confirmed = state_cumulative.sort_values(by='Confirmed', ascending=False)
Top_active = state_cumulative.sort_values(by='Active', ascending=False)
Top_deaths = state_cumulative.sort_values(by='Deaths', ascending=False) 
Top_recovered = state_cumulative.sort_values(by='Recovered', ascending=False) 


import pandas as pd
import numpy as np
import os

wine_data = 'data/wine/wine.data'
df_data_new = pd.read_csv(wine_data,header=None)
#Add titles
column_title = ['class','Alcohol','Malicacid','Ash','Alcalinity_of_ash','Magnesium','Total_phenols','Flavanoids','Nonglavanoid_phenols','Proanthocyanins','Color_intensity','Hue','0D280_0D315_of_diluted_wines','Proline']
df_data_new.columns = column_title
# Find average
avg_alco = df_data_new['Alcohol'].mean()
avg_malicacid = df_data_new['Malicacid'].mean()
avg_Ash = df_data_new['Ash'].mean()
avg_Acalinity = df_data_new['Alcalinity_of_ash'].mean()
avg_Magnesium = df_data_new['Magnesium'].mean()
avg_phenols = df_data_new['Total_phenols'].mean()
avg_Flavanoids = df_data_new['Flavanoids'].mean()
avg_Nonglavanoid_phenols = df_data_new['Nonglavanoid_phenols'].mean()
avg_Proanthocyanins = df_data_new['Proanthocyanins'].mean()
avg_Color_intensity = df_data_new['Color_intensity'].mean()
avg_Hue = df_data_new['Hue'].mean()
avg_Proline = df_data_new['Proline'].mean()
# Find less and larger

path = 'results'
if not os.path.exists('results'):
    os.mkdir('results')

less_avg_alco = df_data_new[df_data_new['Alcohol'] < avg_alco]
less_avg_alco_file = os.path.join(path, 'less_avg_alco.csv')
less_avg_alco.to_csv(less_avg_alco_file, index=False)
more_or_equal_avg_alco = df_data_new[df_data_new['Alcohol'] >= avg_alco]
more_or_equal_avg_alco_file = os.path.join(path, 'more_or_equal_avg_alco.csv')
more_or_equal_avg_alco.to_csv(more_or_equal_avg_alco_file, index=False)

less_avg_malicacid = df_data_new[df_data_new['Malicacid']<avg_malicacid]
less_avg_malicacid_file = os.path.join(path, 'less_avg_malicacid.csv')
less_avg_malicacid.to_csv(less_avg_malicacid_file, index=False)
more_or_equal_avg_malicacid = df_data_new[df_data_new['Malicacid'] >= avg_malicacid]
more_or_equal_avg_malicacid_file = os.path.join(path, 'more_or_equal_avg_malicacid.csv')
more_or_equal_avg_malicacid.to_csv(more_or_equal_avg_malicacid_file, index=False)

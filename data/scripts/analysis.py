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

less_avg_ash = df_data_new[df_data_new['Ash']<avg_Ash]
less_avg_ash_file = os.path.join(path, 'less_avg_ash.csv')
less_avg_ash.to_csv(less_avg_ash_file, index=False)
more_or_equal_avg_ash = df_data_new[df_data_new['Ash'] >= avg_Ash]
more_or_equal_avg_ash_file = os.path.join(path, 'more_or_equal_avg_ash.csv')
more_or_equal_avg_ash.to_csv(more_or_equal_avg_ash_file, index=False)

less_avg_Alcalinity = df_data_new[df_data_new['Alcalinity_of_ash']<avg_Acalinity]
less_avg_Alcalinity_file = os.path.join(path, 'less_avg_Acalinity.csv')
less_avg_Alcalinity.to_csv(less_avg_Alcalinity_file, index=False)
more_or_equal_avg_Alcalinity = df_data_new[df_data_new['Alcalinity_of_ash'] >= avg_Acalinity]
more_or_equal_avg_Alcalinity_file = os.path.join(path, 'more_or_equal_avg_Acalinity.csv')
more_or_equal_avg_Alcalinity.to_csv(more_or_equal_avg_Alcalinity_file, index=False)

less_avg_Magnesium = df_data_new[df_data_new['Magnesium']<avg_Magnesium]
less_avg_Magnesium_file = os.path.join(path, 'less_avg_Magnesium.csv')
less_avg_Magnesium.to_csv(less_avg_Magnesium_file, index=False)
more_or_equal_avg_Magnesium = df_data_new[df_data_new['Magnesium'] >= avg_Magnesium]
more_or_equal_avg_Magnesium_file = os.path.join(path, 'more_or_equal_avg_Magnesium.csv')
more_or_equal_avg_Magnesium.to_csv(more_or_equal_avg_Magnesium_file, index=False)

less_avg_phenols = df_data_new[df_data_new['Total_phenols']<avg_phenols]
less_avg_phenols_file = os.path.join(path, 'less_avg_phenols.csv')
less_avg_phenols.to_csv(less_avg_phenols_file, index=False)
more_or_equal_avg_phenols = df_data_new[df_data_new['Total_phenols'] >= avg_phenols]
more_or_equal_avg_phenols_file = os.path.join(path, 'more_or_equal_avg_phenols.csv')
more_or_equal_avg_phenols.to_csv(more_or_equal_avg_phenols_file, index=False)


less_avg_Flavanoids = df_data_new[df_data_new['Flavanoids']<avg_Flavanoids]
less_avg_Flavanoids_file = os.path.join(path, 'less_avg_Flavanoids.csv')
less_avg_Flavanoids.to_csv(less_avg_Flavanoids_file, index=False)
more_or_equal_avg_Flavanoids = df_data_new[df_data_new['Flavanoids'] >= avg_Flavanoids]
more_or_equal_avg_Flavanoids_file = os.path.join(path, 'more_or_equal_avg_Flavanoids.csv')
more_or_equal_avg_Flavanoids.to_csv(more_or_equal_avg_Flavanoids_file, index=False)

less_avg_Nonglavanoid_phenols = df_data_new[df_data_new['Nonglavanoid_phenols']<avg_Nonglavanoid_phenols]
less_avg_Nonglavanoid_phenols_file = os.path.join(path, 'less_avg_Nonglavanoid_phenols.csv')
less_avg_Nonglavanoid_phenols.to_csv(less_avg_Nonglavanoid_phenols_file, index=False)
more_or_equal_avg_Nonglavanoid_phenols = df_data_new[df_data_new['Nonglavanoid_phenols'] >= avg_Flavanoids]
more_or_equal_avg_Nonglavanoid_phenols_file = os.path.join(path, 'more_or_equal_avg_Nonglavanoid_phenols.csv')
more_or_equal_avg_Nonglavanoid_phenols.to_csv(more_or_equal_avg_Nonglavanoid_phenols_file, index=False)

less_avg_Proanthocyanins = df_data_new[df_data_new['Proanthocyanins']<avg_Proanthocyanins]
less_avg_Proanthocyanins_file = os.path.join(path, 'less_avg_Proanthocyanins.csv')
less_avg_Proanthocyanins.to_csv(less_avg_Proanthocyanins_file, index=False)
more_or_equal_avg_Proanthocyanins = df_data_new[df_data_new['Proanthocyanins'] >= avg_Proanthocyanins]
more_or_equal_avg_Proanthocyanins_file = os.path.join(path, 'more_or_equal_avg_Proanthocyanins.csv')
more_or_equal_avg_Proanthocyanins.to_csv(more_or_equal_avg_Proanthocyanins_file, index=False)

less_avg_Color_intensity = df_data_new[df_data_new['Color_intensity']<avg_Color_intensity]
less_avg_Color_intensity_file = os.path.join(path, 'less_avg_Color_intensity.csv')
less_avg_Color_intensity.to_csv(less_avg_Color_intensity_file, index=False)
more_or_equal_avg_Color_intensity = df_data_new[df_data_new['Color_intensity'] >= avg_Color_intensity]
more_or_equal_avg_Color_intensity_file = os.path.join(path, 'more_or_equal_avg_Color_intensity.csv')
more_or_equal_avg_Color_intensity.to_csv(more_or_equal_avg_Color_intensity_file, index=False)

less_avg_Hue = df_data_new[df_data_new['Hue']<avg_Hue]
less_avg_Hue_file = os.path.join(path, 'less_avg_Hue.csv')
less_avg_Hue.to_csv(less_avg_Hue_file, index=False)
more_or_equal_avg_Hue = df_data_new[df_data_new['Hue'] >= avg_Hue]
more_or_equal_avg_Hue_file = os.path.join(path, 'more_or_equal_avg_Hue.csv')
more_or_equal_avg_Hue.to_csv(more_or_equal_avg_Hue_file, index=False)

less_avg_Proline = df_data_new[df_data_new['Proline']<avg_Proline]
less_avg_Proline_file = os.path.join(path, 'less_avg_Proline.csv')
less_avg_Proline.to_csv(less_avg_Proline_file, index=False)
more_or_equal_avg_Proline = df_data_new[df_data_new['Proline'] >= avg_Proline]
more_or_equal_avg_Proline_file = os.path.join(path, 'more_or_equal_avg_Proline.csv')
more_or_equal_avg_Proline.to_csv(more_or_equal_avg_Proline_file, index=False)
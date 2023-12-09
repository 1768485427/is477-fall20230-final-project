from ydata_profiling import ProfileReport
import pandas as pd
wine_data = 'data/wine/wine.data'
df_data = pd.read_csv(wine_data)
profile = ProfileReport(df_data,title="Profiling Report")

import os

if not os.path.exists('profiling'):
    os.mkdir('profiling')
#if not os.path.exists('profiling/report.html'):
  #  os.mkdir('profiling/report.html')

profile_path = 'profiling/report.html'

if os.path.exists(profile_path):
    os.remove(profile_path)
profile.to_file(profile_path)
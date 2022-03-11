#import libraries
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import os
import glob

#set directory
os.chdir("/Volumes/Seagate Backup Plus Drive/TWINT/ByDisaster_WithKeywords/random sample/50each")

filenames = glob.glob('*.csv')

for file in filenames:
    print(file)
    date_cutoff = datetime.strptime(file[0:8],'%Y%m%d') - timedelta(days = 1)
    print(date_cutoff)

    df_old = pd.read_csv(file, lineterminator='\n')
    try:
        df_old['date_as_date'] = df_old['date'].astype('datetime64[ns]')
        df_old = df_old[(df_old['date_as_date'] <= date_cutoff)]
        df_old['Pre'] = np.where(df_old['date_as_date'] < date_cutoff, 1, 0)
        df_old.pop('date_as_date')
        df_old.pop('Post')
        df_old = df_old.dropna(how='any', subset=['date', 'Pre'])
        df_old = df_old.iloc[:, 1:]

        filename = os.path.basename(file)
        pre_rows = len(df_old[(df_old['Pre'] == 1)])
        post_rows = len(df_old[(df_old['Pre'] == 0)])
        pre_key = (df_old.loc[df_old['Pre'] == 1, 'key'].sum())
        post_key = (df_old.loc[df_old['Pre'] == 0, 'key'].sum())
        pre_placebo = (df_old.loc[df_old['Pre'] == 1, 'placebo'].sum())
        post_placebo = (df_old.loc[df_old['Pre'] == 0, 'placebo'].sum())

        data = {'Filename': [filename],
                'pre_rows': [pre_rows],
                'post_rows': [post_rows],
                'pre_key': [pre_key],
                'post_key': [post_key],
                'pre_placebo': [pre_placebo],
                'post_placebo': [post_placebo]
                }

        df = pd.DataFrame (data, columns = ['Filename',
                                        'pre_rows',
                                        'post_rows',
                                        'pre_key',
                                        'post_key',
                                        'pre_placebo',
                                        'post_placebo'])


        df.to_csv('Numbers/'+file)
        os.remove(file)
    except KeyError:
        pass

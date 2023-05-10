import pandas as pd
import os
from constants import DATABASE

files = os.listdir(DATABASE)

def readDatabase(file = files) -> pd.DataFrame:
    
    for file in files:
        
        df = pd.read_csv(os.path.join(DATABASE, file), sep="\t", on_bad_lines="skip")
        df.columns=['salesid', 'listid', 'sellerid', 'buyerid', 'eventid', 'dateid', 'qtysold', 'pricepaid', 'commission', 'saletime']
        df['saletime'] = pd.to_datetime(df['saletime'])
        df = df.rename(columns = {'qtysold' : 'y',
                         'saletime' : 'ds'})
        df.set_index('ds', inplace=True)
        df = df.drop(['salesid', 'listid', 'sellerid', 'buyerid', 'eventid', 'dateid', 'pricepaid', 'commission'], axis=1)
        
        df = df.sort_index(ascending=True)
        
        return df
from constants import DATABASE

import pandas as pd
import os

# get the list of files from the database directory
files = os.listdir(DATABASE)

def readDatabase(file=files) -> pd.DataFrame:
    """Reads sales data from the database directory.

    Args:
        file (list): A list of file names to read data from. Defaults to files in the database directory.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the sales data.
    """
    # loop over each file in the directory
    for file in files:
        
        # read the data from the file using pandas
        df = pd.read_csv(os.path.join(DATABASE, file), sep="\t", on_bad_lines="skip")
        
        # rename the columns and set index to sale time
        df.columns=['salesid', 'listid', 'sellerid', 'buyerid', 'eventid', 'dateid',
                    'qtysold', 'pricepaid', 'commission', 'saletime']
        df['saletime'] = pd.to_datetime(df['saletime'])
        df = df.rename(columns={'qtysold': 'y', 'saletime': 'ds'})
        df.set_index('ds', inplace=True)
        
        # drop unnecessary columns and sort by index
        df = df.drop(['salesid', 'listid', 'sellerid', 'buyerid', 'eventid', 'dateid',
                      'pricepaid', 'commission'], axis=1)
        df = df.sort_index(ascending=True)
        
        # return the final DataFrame
        return df

# script to clean raw DF that will be presented at the beginning of the streamlit app

import pandas as pd


def clean_raw(df):
    # First, get rid of the columns we don't want to show (_id, '', )
    df.drop(['_id', ''], axis=1, inplace=True)

    for id, row in df.iterrows():
        df.iloc[id].loc['District'] = row['District']['Name'] if len(
            row['District']) else ''
        df.iloc[id].loc['Neighborhood'] = row['Neighborhood']['Name'] if len(
            row['Neighborhood']) else ''
        df.iloc[id].loc['Location'] = row['Location']['coordinates'] if len(
            row['Location']) else ''

    return df

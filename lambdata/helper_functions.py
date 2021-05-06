'''A collection of Data Science helper functions'''

import pandas as pd
import numpy as np

from sklearn.utils import shuffle

DF = pd.DataFrame([4, 6, None, 23, None])


def null_count(df):
    '''This function returns the value of null values for a dataframe'''
    value = df.isnull().sum().sum()
    return value

def split_dates(date_series):
    # TODO Make it so it works with Series instead of DataFrames
    '''This function converts date series to a year, month, day column'''
    df = pd.DataFrame(columns=[date_series])
    df[['month', 'day', 'year']] = df[date_series].str.split('/')
    

def randomize(df, seed):
    """This function randomize all the dataframe cells then returns
    the randomized dataframe"""
    random_df = shuffle(df, random_state=seed)
    return random_df


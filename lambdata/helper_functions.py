"""Lambdata- A collection of Data Science helper functions"""

import pandas as pd
import numpy as np

def null_count(df):
    """This function returns the value of null values for a dataframe"""
    value = df.isnull().sum().sum()
    return value


def split_dates(date_series):
    """This function converts date column to a year, month, day column"""
    df['year'] = pd.Series(df[date_series].dt.year)
    df['month'] = pd.Series(df[date_series].dt.month)
    df['day'] = pd.Series(df[date_series].dt.day)
    return df
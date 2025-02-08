import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def detect_outliers_iqr(data, threshold=1.5):
    """
    Detect outliers in a dataset using the IQR method.
    
    Args:
        data: List or array of numerical data.
        threshold: Multiplier of the IQR to define the bounds.
        
    Returns:
        List of outliers.
    """
    data = np.array(data)
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - (threshold * iqr)
    upper_bound = q3 + (threshold * iqr)
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    return outliers.tolist()

def remove_outliers_df(df, columns=None, threshold=1.5):
    """
    Remove outliers from a DataFrame using the IQR method.
    
    Args:
        df: DataFrame.
        columns: List of columns to analyze. If None, analyzes all numerical columns.
        threshold: Multiplier of the IQR to define the bounds.
        
    Returns:
        DataFrame without outliers.
    """
    if columns is None:
        columns = df.select_dtypes(include=['number']).columns

    for column in columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR

        df = df[~((df[column] < lower_bound) | (df[column] > upper_bound))]

    return df
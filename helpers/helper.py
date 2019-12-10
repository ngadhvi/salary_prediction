import pandas as pd

def merge_data(feature, target):
    """Merge the features and label datasets. Both need to have a common key `jobId`

    Keyword arguments:
    feature -- the dataframe of job description
    target -- the dataframe of salaries
    
    Returns:
    a merged pandas dataframe
    """
    merged_df = pd.merge(feature, target, on='jobId')
    return merged_df


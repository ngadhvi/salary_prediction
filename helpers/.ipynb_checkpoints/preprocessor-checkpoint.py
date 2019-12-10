import pandas as pd
from sklearn.preprocessing import LabelEncoder

class PreProcessor:
    def __init__(self,columns = None):
        self.columns = columns # array of column names to encode

    def fit(self,X,y=None):
        return self # not relevant here

    def transform(self,X):
        '''
        Transforms columns of X specified in self.columns using
        LabelEncoder(). If no columns specified, transforms all
        columns in X.
        '''
        output = X.copy()
        if self.columns is not None:
            for col in self.columns:
                output[col] = LabelEncoder().fit_transform(output[col])
        else:
            for colname,col in output.iteritems():
                output[colname] = LabelEncoder().fit_transform(col)
        return output

    def fit_transform(self,X,y=None):
        print('Encoding complete')
        return self.fit(X,y).transform(X)


def labelenc(dframe, colm_name):
    '''Given a list of columns 
    the function will convert them into label encoded columns and return the data frame'''
   
    for col in colm_name:
        dframe[col] = LabelEncoder().fit_transform(dframe[col])
    return print('Encoding complete')
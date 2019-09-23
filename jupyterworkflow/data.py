import os
from urllib.request import urlretrieve
import pandas as pd

FREEMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_freemont_data(filename='Freemont.csv',url=FREEMONT_URL,force_download=False):
    """ Download and cached the freemont data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url,filename)
    data = pd.read_csv('Freemont.csv',index_col='Date',parse_dates=True)
    data.columns=['East','West']
    data['Total']=data['East']+data['West']
    return data

#SPDX-License-Identifier: MIT
import pandas as pd
from .util import get_data_path

class LocalCSV(object):
    
    def __init__(self):
        return

    name_gender = pd.read_csv(get_data_path('name_gender.csv'), index_col=0)
#using pandas get the data and read the csv named name_gender.

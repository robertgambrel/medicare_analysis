"""
Robert Gambrel - July 2016
Import tab-delineated Medicare data
"""

import pandas as pd
import numpy as np

docs = pd.read_table('Data/Medicare_Provider_Util_Payment_PUF_CY2014'
                     '/Medicare_Provider_Util_Payment_PUF_CY2014.txt',
                     skiprows = 3, header = 1, sep = r"\s\s+",
                     engine = python)
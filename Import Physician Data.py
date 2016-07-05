"""
Robert Gambrel - July 2016
Import tab-delineated Medicare data
"""

import pandas as pd
import numpy as np

docs = pd.read_table('Data/Medicare_Provider_Util_Payment_PUF_CY2014'
                     '/Medicare_Provider_Util_Payment_PUF_CY2014.txt',
                     skiprows = 3,
                     nrows = 100)

docs.columns = ['npi',
                'nppes_provider_last_org_name',
                'nppes_provider_first_name',
                'nppes_provider_mi',
                'nppes_credentials',
                'nppes_provider_gender',
                'nppes_entity_code',
                'nppes_provider_street1',
                'nppes_provider_street2',
                'nppes_provider_city',
                'nppes_provider_zip',
                'nppes_provider_state',
                'nppes_provider_country',
                'provider_type',
                'medicare_participation_indicator',
                'place_of_service',
                'hcpcs_code',
                'hcpcs_description',
                'hcpcs_drug_indicator',
                'line_srvc_cnt',
                'bene_unique_cnt',
                'bene_day_srvc_cnt',
                'average_Medicare_allowed_amt',
                'average_submitted_chrg_amt',
                'average_Medicare_payment_amt',
                'average_Medicare_standard_amt']

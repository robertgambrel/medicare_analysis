"""
Robert Gambrel - July 2016
Import tab-delineated Medicare data
"""

import pandas as pd
import numpy as np
import os
import re

if os.name == 'nt':
    docs = pd.read_table('.\\medicare_analysis\\Data\\Medicare_Provider_Util_Payment_PUF_CY2014.txt',
                         skiprows=3)
    scripts = pd.read_table('.\\medicare_analysis\\Data\\PARTD_PRESCRIBER_PUF_NPI_DRUG_13.tab',
                         skiprows=1)
else:
    docs = pd.read_table('Data/Medicare_Provider_Util_Payment_PUF_CY2014.txt',
                         skiprows = 3)




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

scripts.columns = ['npi',
                   'nppes_provider_last_org_name',
                   'nppes_provider_first_name',
                   'nppes_provider_city',
                   'nppes_provider_state',
                   'specialty_description',
                   'description_flag',
                   'drug_name',
                   'generic_name',
                   'bene_count',
                   'total_claim_count',
                   'total_day_supply',
                   'total_drug_cost',
                   'bene_count_ge65',
                   'bene_count_ge65_redact_flag',
                   'total_claim_count_ge65',
                   'ge65_redact_flag',
                   'total_day_supply_ge65',
                   'total_drug_cost_ge65']

any(re.match("OXYCODONE|CODEINE|FENTANYL|HYDROCODONE|HYDROMORPHONE|MEPERIDINE|METHADONE|MORPHINE", x)
    for x in scripts['generic_name'].head(10000))


opiate_matches = scripts.generic_name.str.contains("OXYCODONE|CODEINE|FENTANYL|HYDROCODONE|HYDROMORPHONE|MEPERIDINE|METHADONE|MORPHINE", regex = True,
                                                   na = False)

opiate_scripts = scripts[opiate_matches]

test = scripts.query(scripts.generic_name.str.contains("OXYCODONE|CODEINE|FENTANYL|HYDROCODONE|HYDROMORPHONE|MEPERIDINE|METHADONE|MORPHINE", regex = True,
                                                   na = False))




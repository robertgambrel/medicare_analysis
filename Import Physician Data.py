"""
Robert Gambrel - July 2016
Import tab-delineated Medicare data from website, extract to a sqlite db
"""

import pandas as pd
import numpy as np
import os
import sys
import re
import sqlite3
import io
import requests
from zipfile import ZipFile

os.chdir(
    "/Users/healthpolicyanalyst/Documents/Box Sync/python/"
    "Medicare Analyses/medicare_analysis/Data")

# download zip file, extract the portion we want, make it a pandas database
docs_request = requests.get('http://download.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Downloads/Medicare_Provider_Util_Payment_PUF_CY2013.zip')
docs_file = ZipFile(io.BytesIO(docs_request.content))
docs_file.namelist()
# for docs file, find the txt document
regex_search = re.compile(".*txt")
# get the name - search through the list, should produce a 1 element list
docs_name =  [m.group(0) for l in docs_file.namelist() for m in [
    regex_search.search(l)] if m][0]
docs_txt = docs_file.extract(docs_name)

docs = pd.read_table(docs_txt, skiprows = 3)


# repeat for prescriber file
scripts_request = requests.get('http://download.cms.gov/Research-Statistics-Data-'
                               'and-Systems/Statistics-Trends-and-Reports/Medicare-'
                               'Provider-Charge-Data/Downloads/'
                               'PartD_Prescriber_PUF_NPI_DRUG_13.zip')
scripts_file = ZipFile(io.BytesIO(scripts_request.content))
scripts_file.namelist()
# for scripts file, find the txt document
regex_search = re.compile(".*tab")
# get the name - search through the list, should produce a 1 element list
scripts_name = [m.group(0) for l in scripts_file.namelist() for m in [
    regex_search.search(l)] if m][0]
scripts_txt = scripts_file.extract(scripts_name)

scripts = pd.read_table(scripts_txt, skiprows=1)


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


# this is big and cumbersome, so put into sqlite database
c = conn.cursor()
docs.to_sql('docs', conn)
scripts.to_sql('scripts', conn)



any(re.match("OXYCODONE|CODEINE|FENTANYL|HYDROCODONE|HYDROMORPHONE|MEPERIDINE|METHADONE|MORPHINE", x)
    for x in scripts['generic_name'].head(10000))


opiate_matches = scripts.generic_name.str.contains("OXYCODONE|CODEINE|FENTANYL|HYDROCODONE|HYDROMORPHONE|MEPERIDINE|METHADONE|MORPHINE", regex = True,
                                                   na = False)

opiate_scripts = scripts[opiate_matches]

test = scripts.query(scripts.generic_name.str.contains("OXYCODONE|CODEINE|FENTANYL|HYDROCODONE|HYDROMORPHONE|MEPERIDINE|METHADONE|MORPHINE", regex = True,
                                                   na = False))




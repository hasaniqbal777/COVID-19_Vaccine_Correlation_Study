# # Fetching Data from Source
# https://www.ecdc.europa.eu/en/covid-19/data

# Importing Python packages
import pandas as pd

# Fetching Cases/Deaths Data
url = "https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/csv/data.csv"
pd.read_csv(url).to_csv("data/raw_cases.csv", index=False)

# Fetching Cases (Age wise) Data
url = "https://opendata.ecdc.europa.eu/covid19/agecasesnational/csv/data.csv"
pd.read_csv(url).to_csv("data/raw_cases_age.csv", index=False)

# Fetching Vaccines Data
url = "https://opendata.ecdc.europa.eu/covid19/vaccine_tracker/csv/data.csv"
pd.read_csv(url).to_csv("data/raw_vaccines.csv", index=False)

# Fetching Variants (percentage) Data
url = "https://opendata.ecdc.europa.eu/covid19/virusvariant/csv/data.csv"
pd.read_csv(url).to_csv("data/raw_variants.csv", index=False)

# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
cleaned_customer_transactions = dataiku.Dataset("cleaned_customer_transactions")
cleaned_customer_transactions_df = cleaned_customer_transactions.get_dataframe()

# Ensure 'age' is numeric (convert invalid values to NaN)
cleaned_customer_transactions_df['age'] = pd.to_numeric(cleaned_customer_transactions_df['age'], errors='coerce')

# Feature Engineering: Age Group
def age_group(age):
    if pd.isna(age):
        return "Unknown"  # If age is missing, categorize as "Unknown"
    elif age < 30:
        return "Young"
    elif age < 60:
        return "Middle-aged"
    else:
        return "Senior"

# Apply the function to the dataframe
cleaned_customer_transactions_df['age_group'] = cleaned_customer_transactions_df['age'].apply(age_group)

# Write recipe outputs
customers_with_age_groups = dataiku.Dataset("customers_with_age_groups")
customers_with_age_groups.write_with_schema(cleaned_customer_transactions_df)
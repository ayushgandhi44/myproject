# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
customer_transactions = dataiku.Dataset("customer_transactions")
customer_transactions_df = customer_transactions.get_dataframe()

# Data Cleaning
# Remove rows where 'transaction_amount' is below 50
cleaned_customer_transactions_df = customer_transactions_df[customer_transactions_df['transaction_amount'] >= 50]

# Handle missing values (if any)
# For example, fill missing 'name' entries with 'Unknown'
cleaned_customer_transactions_df['name'].fillna('Unknown', inplace=True)

# Optionally, you can print some insights or information about the data
# print(cleaned_customer_transactions_df.head())

# Write recipe outputs
cleaned_customer_transactions = dataiku.Dataset("cleaned_customer_transactions")
cleaned_customer_transactions.write_with_schema(cleaned_customer_transactions_df)
"""
Hospital Data Wrangling Assignment

This module contains functions for wrangling hospital patient, billing, and resource data.
Students should complete each function according to the specifications in the docstrings.

Author: [Your Name]
Date: [Date]
"""

import pandas as pd


def map_insurance_codes(df):
    """
    Map insurance type codes to full insurance names and create a new column.
    
    The mapping should be:
    - 'PPO' -> 'Preferred Provider Organization'
    - 'HMO' -> 'Health Maintenance Organization'
    - 'Medicare' -> 'Medicare'
    - 'Medicaid' -> 'Medicaid'
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing an 'insurance_type' column with insurance codes
    
    Returns:
    --------
    pandas.DataFrame
        Original DataFrame with a new column 'insurance_full_name' containing
        the full insurance names
    """
    # TODO: Implement this function
    pass


def encode_gender(df):
    """
    Create binary encoded columns for gender using one-hot encoding.
    
    This should create two new columns:
    - 'gender_M': 1 if Male, 0 otherwise
    - 'gender_F': 1 if Female, 0 otherwise
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing a 'gender' column with values 'M' or 'F'
    
    Returns:
    --------
    pandas.DataFrame
        Original DataFrame with new binary columns for gender
    """
    # TODO: Implement this function
    pass


def join_patient_billing(patients_df, billing_df):
    """
    Join patient and billing data on patient_id.
    
    This should perform an INNER join between the patients and billing DataFrames.
    The resulting DataFrame should contain all columns from both DataFrames.
    
    Parameters:
    -----------
    patients_df : pandas.DataFrame
        DataFrame containing patient information with 'patient_id' column
    billing_df : pandas.DataFrame
        DataFrame containing billing information with 'patient_id' column
    
    Returns:
    --------
    pandas.DataFrame
        Merged DataFrame containing all columns from both input DataFrames
    """
    # TODO: Implement this function
    pass


def pivot_bed_type_costs(resources_df):
    """
    Create a pivot table showing total daily rates by bed type.
    
    The pivot table should:
    - Have 'bed_type' as the index
    - Show the sum of 'daily_rate' for each bed type
    - Be sorted by total daily rate in descending order
    
    Parameters:
    -----------
    resources_df : pandas.DataFrame
        DataFrame containing resource information with 'bed_type' and 'daily_rate' columns
    
    Returns:
    --------
    pandas.Series
        Series with bed types as index and total daily rates as values,
        sorted in descending order
    """
    # TODO: Implement this function
    pass


def group_by_department(billing_df):
    """
    Group billing data by department code and calculate summary statistics.
    
    The result should show for each department:
    - Total number of procedures (count)
    - Total charges (sum of charge_amount)
    - Average charge (mean of charge_amount)
    
    Columns should be named: 'procedure_count', 'total_charges', 'avg_charge'
    Results should be sorted by total_charges in descending order.
    
    Parameters:
    -----------
    billing_df : pandas.DataFrame
        DataFrame containing billing information with 'dept_code' and 'charge_amount' columns
    
    Returns:
    --------
    pandas.DataFrame
        DataFrame with dept_code as index and aggregated statistics as columns
    """
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    # This section is for your own testing

# data_loader.py
# Author: Yangli Deng
# Responsibility: Load and validate Excel files for financial analysis

import os
import pandas as pd

REQUIRED_COLUMNS = [
    "Year",
    "Revenue",
    "Expenses",
    "Net Profit",
    "Assets",
    "Liabilities"
]

def load_company_data(folder_path: str) -> dict:
    """
    Reads all Excel files in the given folder, validates their structure,
    and returns a dictionary of company dataframes.

    Returns:
        dict: { company_name : pandas.DataFrame }
    """
    if not os.path.isdir(folder_path):
        raise ValueError("Provided path is not a valid directory")

    company_data = {}

    for file in os.listdir(folder_path):
        if file.endswith(".xlsx"):
            file_path = os.path.join(folder_path, file)
            company_name = os.path.splitext(file)[0]

            df = pd.read_excel(file_path)

            _validate_columns(df, file)
            _validate_data(df, file)

            company_data[company_name] = df

    if len(company_data) < 2:
        raise ValueError("At least two company Excel files are required")

    return company_data


def _validate_columns(df: pd.DataFrame, filename: str):
    for column in REQUIRED_COLUMNS:
        if column not in df.columns:
            raise ValueError(
                f'File "{filename}" is missing required column: {column}'
            )


def _validate_data(df: pd.DataFrame, filename: str):
    if df.isnull().values.any():
        raise ValueError(
            f'File "{filename}" contains missing values'
        )

    if not pd.api.types.is_numeric_dtype(df["Year"]):
        raise ValueError(
            f'File "{filename}" has non-numeric Year values'
        )

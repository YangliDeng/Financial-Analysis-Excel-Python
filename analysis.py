# analysis.py
# Author: Sarah
# Responsibility: Perform financial analysis and determine conclusions

import pandas as pd


def analyze_companies(company_data: dict) -> dict:
    """
    Performs financial analysis on company data and returns results
    required for reporting.
    """

    avg_profit_margin = {}
    profit_volatility = {}

    for company, df in company_data.items():
        profit_margin = df["Net Profit"] / df["Revenue"]
        avg_profit_margin[company] = profit_margin.mean()

        profit_volatility[company] = df["Net Profit"].std()

    most_profitable = _find_most_profitable(avg_profit_margin)
    most_concerning = _find_most_concerning(company_data, profit_volatility)

    return {
        "companies": list(company_data.keys()),
        "avg_profit_margin": avg_profit_margin,
        "profit_volatility": profit_volatility,
        "most_profitable": most_profitable,
        "most_concerning": most_concerning
    }


def _find_most_profitable(avg_profit_margin: dict) -> str:
    """
    Determines the most profitable company based on
    highest average profit margin.
    """
    return max(avg_profit_margin, key=avg_profit_margin.get)


def _find_most_concerning(company_data: dict, profit_volatility: dict) -> str:
    """
    Determines the most concerning company based on:
    - Negative net profit in any year, OR
    - Highest profit volatility
    """

    for company, df in company_data.items():
        if (df["Net Profit"] < 0).any():
            return company

    return max(profit_volatility, key=profit_volatility.get)

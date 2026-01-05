# reporting.py
# Author: Kyryl
# Responsibility: Generate graphs and summary report

import os
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd


def generate_graphs(company_data: dict, analysis_results: dict, output_dir: str):
    """
    Generates and saves all required graphs as PNG files.
    """

    graphs_dir = os.path.join(output_dir, "graphs")
    os.makedirs(graphs_dir, exist_ok=True)

    _plot_revenue(company_data, graphs_dir)
    _plot_net_profit(company_data, graphs_dir)
    _plot_profit_margin(analysis_results, graphs_dir)
    _plot_profit_volatility(analysis_results, graphs_dir)


def save_summary_txt(analysis_results: dict, output_dir: str):
    """
    Saves the financial analysis summary as a TXT file with analysis date.
    """

    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "summary_report.txt")

    today = datetime.now().strftime("%Y-%m-%d")

    with open(file_path, "w") as file:
        file.write("Financial Analysis Summary\n")
        file.write("==========================\n\n")
        file.write(f"Analysis Date: {today}\n\n")

        file.write("Companies Analyzed:\n")
        for company in analysis_results["companies"]:
            file.write(f"- {company}\n")

        file.write("\nMost Profitable Company:\n")
        file.write(f"{analysis_results['most_profitable']}\n\n")

        file.write("Most Concerning Company:\n")
        file.write(f"{analysis_results['most_concerning']}\n\n")

        file.write("Metrics Used:\n")
        file.write("- Revenue vs Year\n")
        file.write("- Net Profit vs Year\n")
        file.write("- Average Profit Margin\n")
        file.write("- Profit Volatility\n")


# ----------------- Graph Functions -----------------

def _plot_revenue(company_data: dict, output_dir: str):
    plt.figure()
    for company, df in company_data.items():
        plt.plot(df["Year"], df["Revenue"], label=company)

    plt.xlabel("Year")
    plt.ylabel("Revenue")
    plt.title("Revenue vs Year")
    plt.legend()
    plt.savefig(os.path.join(output_dir, "revenue_vs_year.png"))
    plt.close()


def _plot_net_profit(company_data: dict, output_dir: str):
    plt.figure()
    for company, df in company_data.items():
        plt.plot(df["Year"], df["Net Profit"], label=company)

    plt.xlabel("Year")
    plt.ylabel("Net Profit")
    plt.title("Net Profit vs Year")
    plt.legend()
    plt.savefig(os.path.join(output_dir, "net_profit_vs_year.png"))
    plt.close()


def _plot_profit_margin(analysis_results: dict, output_dir: str):
    companies = list(analysis_results["avg_profit_margin"].keys())
    margins = list(analysis_results["avg_profit_margin"].values())

    plt.figure()
    plt.bar(companies, margins)
    plt.xlabel("Company")
    plt.ylabel("Average Profit Margin")
    plt.title("Average Profit Margin Comparison")
    plt.savefig(os.path.join(output_dir, "profit_margin.png"))
    plt.close()


def _plot_profit_volatility(analysis_results: dict, output_dir: str):
    companies = list(analysis_results["profit_volatility"].keys())
    volatility = list(analysis_results["profit_volatility"].values())

    plt.figure()
    plt.bar(companies, volatility)
    plt.xlabel("Company")
    plt.ylabel("Profit Volatility")
    plt.title("Profit Volatility Comparison")
    plt.savefig(os.path.join(output_dir, "profit_volatility.png"))
    plt.close()

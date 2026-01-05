# main.py
from data_loader import load_company_data
from analysis import analyze_companies
from reporting import generate_graphs, save_summary_txt

DATA_FOLDER = "data"
OUTPUT_FOLDER = "output"

def main():
    company_data = load_company_data(DATA_FOLDER)
    analysis_results = analyze_companies(company_data)
    generate_graphs(company_data, analysis_results, OUTPUT_FOLDER)
    save_summary_txt(analysis_results, OUTPUT_FOLDER)
    print("Analysis completed successfully.")

if __name__ == "__main__":
    main()

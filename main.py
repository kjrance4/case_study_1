from pdf_data import get_pdf_data
from csv_data import extract_csv_data

# Define the path to the PDF file (Certificate Holders Statement)
pdf_path = 'data/Certificate Holders Statement/CertStmtCMLT06AMC10710.pdf'

# Define the path to the CSV file containing loan details
csv_path = 'data/Enhanced Loan-Level Data/LoanDetailCMLT06AMC10710.csv'

total_from_pdf = float(get_pdf_data(pdf_path).replace(",", ""))
total_from_csv = extract_csv_data(csv_path)

# Compare the extracted CSV data with the PDF data and print the result
if total_from_pdf == total_from_csv:
    print(f"Total Principal Funds Available are equal.")
    print(f"Amount: {total_from_csv}")
else:
    difference = total_from_pdf - total_from_csv
    print(f"Total Principal Funds Available are unequal with a discrepancy of {difference}.")


import pdf_data
import csv_data

A = float(pdf_data.total_funds_pdf.replace(",", ""))
B = csv_data.extract_csv_data('data_frame')

# Compare the extracted CSV data with the PDF data and print the result
if A == B:
    print("Correct!")
else:
    print("Try Again!")


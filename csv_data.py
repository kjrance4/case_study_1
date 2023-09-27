import pandas as pd

# Define the path to the CSV file containing loan details
csv_path = 'data/Enhanced Loan-Level Data/LoanDetailCMLT06AMC10710.csv'

df = pd.read_csv(csv_path)

# Define a function to extract data from csv
def extract_csv_data(data_frame):
    # Define the columns to extract
    columns_to_extract = ['Scheduled Principal', 'Curtailments',
                          'Curtailment Adjustments', 'Prepayment',
                          'Repurchase Principal', 'Other Principal Adjustments',
                          'Liquidation Principal', 'Principal Losses']

    selected_columns = df[columns_to_extract]
    summary = selected_columns.sum()
    summary_str = summary.to_string(dtype=False)

    # Calculate the total sum of all columns
    total = summary.sum()

    # Subtract the losses
    extract_losses = df['Principal Losses']
    total_losses = extract_losses.sum()
    result = round(total - (2 * total_losses), 2)

    return result


# Call the extract_csv_data function
total_funds_csv = extract_csv_data(df)


import PyPDF2

# Define a function to extract data from the PDF
def get_pdf_data(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    page = pdf_reader.pages[5]
    text = page.extract_text()

    # Initialize an empty dictionary to store headers
    items = dict()
    header = ""

    # Loop through each line in the PDF page
    for t in text.split("\n"):
        if t == "Principal Funds Available":
            header = t
            # Create a sub-dictionary to store items under the header
            items[header] = dict()

        # Check for various item types and extract their data
        elif t.startswith("Scheduled Principal"):
            data = t.split("  ")
            items[header][data[0]] = data[1]

        elif t.startswith("Curtailments"):
            data = t.split("  ")
            items[header][data[0]] = data[1]

        elif t.startswith("Prepayments"):
            data = t.split("  ")
            items[header][data[0]] = data[1]

        elif t.startswith("Liquidation"):
            data = t.split("  ")
            items[header][data[0]] = data[1]

        elif t.startswith("Repurchased"):
            data = t.split("  ")
            items[header][data[0]] = data[1]

        elif t.startswith("Substitution"):
            data = t.split("  ")
            items[header][data[0]] = data[1]

        elif t.startswith("Total Principal"):
            data = t.split("  ")
            items[header][data[0]] = data[1]

    # Extract the value under the "Total Principal Funds Available" header
    values = list(items.values())[0]
    return values['Total Principal Funds Available:']


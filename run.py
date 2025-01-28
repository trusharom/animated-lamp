from PyPDF2 import PdfMerger

# Specify the paths of the PDF files
pdf_files = [
    "physics.pdf",  # Replace with the path of the first PDF
    "chemistry.pdf",
    "math.pdf",
    "english.pdf",
    "biology.pdf"   # Replace with the path of the second PDF
]

# Ask the user for the sequence
print("Files to merge:", pdf_files)
order = input("Enter the order of files to merge (e.g., 1,2): ").split(",")

# Validate and parse the order
order = [int(idx) - 1 for idx in order if idx.isdigit()]
if len(order) != len(pdf_files):
    print("Error: Invalid sequence")
else:
    # Merge PDFs
    merger = PdfMerger()
    for idx in order:
        merger.append(pdf_files[idx])

    # Output the merged file
    output_file = "merged_output.pdf"
    merger.write(output_file)
    merger.close()

    print(f"PDF files merged successfully into {output_file}")

from PyPDF2 import PdfMerger

# Create PdfMerger Object
merger = PdfMerger()

# List of PDF Files
pdf_files = [
    "file1.pdf",
    "file2.pdf",
    "file3.pdf"
]

# Merge PDFs
for pdf in pdf_files:
    merger.append(pdf)

# Save Merged PDF
merger.write("merged_output.pdf")

# Close Merger
merger.close()

print("PDF files merged successfully!")

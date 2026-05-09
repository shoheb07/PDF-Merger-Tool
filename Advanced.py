from PyPDF2 import PdfMerger
import os

merger = PdfMerger()

# Merge all PDFs in folder
for file in os.listdir():

    if file.endswith(".pdf") and file != "merged_output.pdf":
        merger.append(file)

merger.write("merged_output.pdf")
merger.close()

print("All PDFs merged successfully!")

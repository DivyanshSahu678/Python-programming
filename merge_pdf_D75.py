#Day 75

#Merge multiple PDF

from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["file1.pdf", "file2.pdf"]:
    merger.append(pdf)
    
merger.write("merged.pdf")
merger.close()
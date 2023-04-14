from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["Chap8_Laplace.pdf", "Chap8_Laplace_sol.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

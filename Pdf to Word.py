from pdf2docx import Converter

pdf_file="C:\\Users\\abuka\\Downloads\\Documents\\Hacker.pdf"
docx_file="C:\\Users\\abuka\\Downloads\\Documents\\HackerDoc.docx"
cv=Converter(pdf_file=pdf_file)
cv.convert(docx_filename=docx_file)
cv.close()


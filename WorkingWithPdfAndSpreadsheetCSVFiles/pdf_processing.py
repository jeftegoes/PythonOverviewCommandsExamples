import PyPDF2

pdf_file = open("example.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
print(f"1: {pdf_reader.numPages}")

page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
print(f"2: {page_one_text}")

pdf_file.close()

pdf_file = open("example.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
first_page = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
print(f"3: {first_page}")
pdf_writer.add_page(first_page)
pdf_output = open("to_save_pdf.pdf", "wb")
pdf_writer.write(pdf_output)
pdf_file.close()
pdf_output.close()

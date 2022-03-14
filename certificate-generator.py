from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import os
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

print("\ncertificate-generator-v1.0")
print("@sanbabyfrancis")
print("--------------------------\n")
print("This simple utility will produce multiple certificates from a given certificate template.")
print("The participant names are read from a spreadsheet. Make sure that the python script, the ")
print("certificate template (pdf), the participant spreadsheet (xls, xlsx, xlsm, xlsb, odf, odt)")
print("and the font (ttf) that has to be used to print the name are in the same directory.    \n")
print("--------------------------\n")

certemplate = input("> Enter the name of the certificate template (eg. template.pdf): ")
excelfile = input("> Enter the name of the spreadsheet that contains participant details (eg. participants.xlsx): ")
varname = input("> Enter the name of the column that contains the participant name (eg. Name): ")
print("> Enter the pixel dimensions for the text to be printed on the certificate:")
horz = int(input("  > Horizontal dimension: "))
vert = int(input("  > Vertical dimension: "))
varfont = input("> Enter the font for the text (eg. Inter.ttf): ")
fontsize = int(input("> Enter the font size: "))
print()

#create the certificate directory
os.makedirs("certificates", exist_ok=True)

# register the necessary font
pdfmetrics.registerFont(TTFont('myFont', varfont))

# provide the excel file that contains the participant names (in column 'Name')
data = pd.read_excel(excelfile)

name_list = data[varname].tolist()
names = [x.upper().strip() for x in name_list]
for i in names:
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    # the registered font is used, provide font size
    can.setFont("myFont", fontsize)

    # provide the text location in pixels
    can.drawString(horz, vert, i)

    can.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    # provide the certificate template
    existing_pdf = PdfFileReader(open(certemplate, "rb"))

    output = PdfFileWriter()
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    destination = "certificates" + os.sep + i + ".pdf"
    outputStream = open(destination, "wb")
    output.write(outputStream)
    outputStream.close()
    print("created " + i + ".pdf")

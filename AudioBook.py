from gtts import gTTS

import docxpy
file = "D:\\n.docx"
tet = docxpy.process(file)
print(tet)
tt = gTTS(text=tet,lang='en',slow=False)
tt.save("D:\\pdfr.mp3")
print("---------------------------------------")

import PyPDF2
pdo = open('D:\\the.pdf','rb')
pdr = PyPDF2.PdfFileReader(pdo)
print(pdr.numPages)
pg = pdr.getPage(0)
str = pg.extractText()
tt = gTTS(text=str,lang='en',slow=False)
tt.save("D:\\pdfr.mp3")
print("done")
print(str)


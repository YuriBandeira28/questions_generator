from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph

import gpt

perg = gpt.chat("Python", "Orientação a objetos")
res = gpt.respostas(perg)
parag = Paragraph

try:
    pdf = canvas.Canvas('Gababrito.pdf', pagesize=A4)
    y = 850
    for i, pergunta in enumerate(perg):
        y -=50
        texto = parag(pergunta)
        texto.wrapOn(pdf, 500, 100)
        texto.drawOn(pdf, 20, y)
        #pdf.drawString(20,y, f'{pergunta}')
        y -=50
        texto2 = parag(res[i])
        texto2.wrapOn(pdf, 500, 100)
        texto2.drawOn(pdf, 30, y)
        #pdf.drawString(30,y, res[i])

    pdf.setTitle("Gabarito")
    pdf.setFont("Helvetica-Oblique", 14)
    pdf.save()
    print("finalizou")
except Exception as e:
    print(e)
    print('erro')

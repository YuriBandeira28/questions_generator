from reportlab.pdfgen import canvas
import gpt

perg = gpt.chat("Python", "Orientação a objetos")
res = gpt.respostas(perg)

try:
    pdf = canvas.Canvas('Gababrito.pdf')
    y = 720
    for i, pergunta in enumerate(perg):
        y -=30
        pdf.drawString(20,y, f'{pergunta}')
        y -=20
        pdf.drawString(30,y, res[i])

    pdf.setTitle("Gabarito")
    pdf.setFont("Helvetica-Oblique", 14)
    pdf.save()
except Exception as e:
    print(e)
    print('erro')

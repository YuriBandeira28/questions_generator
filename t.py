from reportlab.pdfgen import canvas

def GeneratePDF(lista):
    try:
        pdf = canvas.Canvas('Gababrito.pdf')
        x = 720
        for nome,idade in lista.items():
            x -= 20
            pdf.drawString(247,x, '{} : {}'.format(nome,idade))
        pdf.setTitle("Gabarito")
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.save()
    except:
        print('erro')

lista = {'Rafaela': '19', 'Jose': '15', 'Maria': '22','Eduardo':'24'}

GeneratePDF(lista)
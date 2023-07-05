from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph





def export_pdf(perg, res):
    
    parag = Paragraph

    try:
        pdf = canvas.Canvas('Gababrito.pdf', pagesize=A4)
        y = 850
        for i, pergunta in enumerate(perg):
            y -=50
            texto = parag(pergunta)
            texto.wrapOn(pdf, 500, 100)
            texto.drawOn(pdf, 20, y)
            y -=50
            texto2 = parag(res[i])
            texto2.wrapOn(pdf, 500, 100)
            texto2.drawOn(pdf, 30, y)

        pdf.setTitle("Gabarito")
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.save()
        print("finalizou")
        return """PDF Gerado com Sucesso!!\n
                    Nota: Pode ser que o PDF não esteja correto, caso ocorra, 
                    ele pode ser gerado novamente"""
    except Exception as e:
        print(e)
        return 'Houve Algum erro ao gerar o PDF!\nTente Novamente!'

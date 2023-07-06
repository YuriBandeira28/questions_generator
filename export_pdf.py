from flask import Flask, render_template, redirect
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from requests import request

app = Flask(__name__)

def export_pdf(perg, res):
    parag = Paragraph

    try:
        pdf = canvas.Canvas('Gababrito.pdf', pagesize=A4)
        y = 850
        for i, pergunta in enumerate(perg):
            y -= 60
            texto = parag(pergunta)
            texto.wrapOn(pdf, 500, 100)
            texto.drawOn(pdf, 20, y)
            y -= 70
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


@app.route('/', methods=['GET', 'POST'])
def gerador_questoes():
    if request.method == 'POST':
        # Aqui você pode obter os dados do formulário, como 'materia' e 'assunto'
        materia = request.form.get('materia')
        assunto = request.form.get('assunto')

        # Aqui você pode gerar as perguntas e respostas com base nos dados fornecidos

        # Exemplo de dados fictícios para teste
        perguntas = ['Pergunta 1', 'Pergunta 2', 'Pergunta 3']
        respostas = ['Resposta 1', 'Resposta 2', 'Resposta 3']

        # Chama a função export_pdf() para gerar o PDF
        resultado = export_pdf(perguntas, respostas)

        # Retorna o resultado como uma mensagem na página
        return render_template('index.html', resultado=resultado)

    return render_template('index.html')


@app.route('/reset')
def reset():
    # Lógica de redefinição dos dados e do PDF gerado
    # ...

    return redirect('/')


if __name__ == '__main__':
    app.run()

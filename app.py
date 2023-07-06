from flask import Flask, render_template, request, redirect
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
import gpt

app = Flask(__name__)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def send(assunto, materia):
    
    if assunto != '' or materia != '':
        preguntas = gpt.chat(materia, assunto)
        respostas = gpt.respostas(preguntas)
        return preguntas, respostas
    else:
        return [], []

def export_pdf(perg, res):
    parag = Paragraph

    try:
        pdf = canvas.Canvas('Gababrito.pdf', pagesize=A4)
        y = 850
        for i, pergunta in enumerate(perg):
            y -= 50
            texto = parag(pergunta)
            texto.wrapOn(pdf, 500, 100)
            texto.drawOn(pdf, 20, y)
            y -= 60
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

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

perguntas = []
respostas = []

@app.route('/', methods=['GET', 'POST'])
def index():
    assunto = ''
    materia = ''
    global perguntas
    global respostas
    
    if request.method == 'POST':
        assunto = request.form.get('assunto')
        materia = request.form.get('materia')
        perguntas, respostas = send(assunto, materia)

    return render_template('index.html', perguntas=perguntas, respostas=respostas, assunto=assunto, materia=materia)

@app.route('/reset')
def reset():
    # Lógica de redefinição dos dados e do PDF gerado
    # ...

    return redirect('/')

@app.route('/export', methods=['POST'])
def export():
    global perguntas
    global respostas
    assunto = request.form.get('assunto')
    materia = request.form.get('materia')
    #preguntas, respostas = send(assunto, materia)
    resultado = export_pdf(perguntas, respostas)
    return render_template('index.html', resultado=resultado, perguntas=perguntas, respostas=respostas, assunto=assunto, materia=materia)

if __name__ == '__main__':
    app.run()

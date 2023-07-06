from flask import Flask, render_template, request, redirect
from pathlib import Path
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

def export_docx(perg, res):
    
    try:
        with open("Gabarito.docx", "w") as t: 
            for p in perg:
                t.write(p)
                t.write("\n")
                t.write(f'\t{res[perg.index(p)]}')
                t.write("\n")
                t.write("\n")
        print("DOCX Gerado com Sucesso!!")
        return """DOCX Gerado com Sucesso!!"""
    
    except Exception as e:
        print(e)
        return 'Houve Algum erro ao gerar o DOCX!\nTente Novamente!'

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
    resultado = export_docx(perguntas, respostas)
    return render_template('index.html', resultado=resultado, perguntas=perguntas, respostas=respostas, assunto=assunto, materia=materia)

if __name__ == '__main__':
    app.run()

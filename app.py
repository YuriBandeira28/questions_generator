from flask import Flask, render_template, request
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
        return 'Por favor, insira algo na caixa de texto'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        assunto = request.form.get('assunto')
        materia = request.form.get('materia')
        preguntas, respostas = send(assunto, materia)
        return render_template('index.html', perguntas = preguntas, respostas=respostas, assunto=assunto, materia=materia)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

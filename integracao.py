from flask import Flask, render_template, request
import json
import requests
import config

app = Flask(__name__)

def gerar_questoes(materia, assunto):
    headers = {"Authorization": f"Bearer {config.token}", "Content-Type": "application/json"}

    data = {
        "model": config.model,
        "messages": [{
            "role": "user",
            "content": f"""FAÇA EXATAMENTE DA FORMA QUE SE PEDE, gere 7 questões de {materia} sobre {assunto} numeradas de 1 a 7 com um prefixo de
                         "Questão <número da questão> - ",
                         separe cada uma, exceto a última, por 'FIM DA QUESTÃO'"""
        }]
    }

    data = json.dumps(data)
    try:
        req = requests.post(url=config.url, headers=headers, data=data)
        res = req.json()
        res = res['choices'][0]['message']['content']
        res = str(res)
        questions = res.split('FIM DA QUESTÃO\n')
        questions2 = []

        for q in questions:
            try:
                q = q.replace("\n", "")
                q = q.replace("Questão ", '')
                try:
                    q = q.replace("FIM DA QUESTÃO", '')
                except:
                    pass

                questions2.append(q)
            except:
                questions2.append(q)
    except:
        questions2 = None
    print("questoes - ", questions2)
    return questions2


def gerar_respostas(questoes):
    headers = {"Authorization": f"Bearer {config.token}", "Content-Type": "application/json"}

    data = {
        "model": config.model,
        "messages": [{
            "role": "user",
            "content": f"""FAÇA EXATAMENTE DA FORMA QUE SE PEDE, responda essas questões {questoes} numerando elas de 1 a 7,
                    com um prefixo de "Resposta <número da resposta> - ",
                    separe cada uma, exceto a última, por 'FIM DA RESPOSTA'"""
        }]
    }
    data = json.dumps(data)
    req = requests.post(url=config.url, headers=headers, data=data)
    res = req.json()
    res = res['choices'][0]['message']['content']
    res = str(res)
    respostas = res.split('FIM DA RESPOSTA\n')

    respostas2 = []

    for i, r in enumerate(respostas):
        try:
            r = r.replace("\n", "")
            r = r.replace(f"Resposta {i + 1} -", "R:")
            try:
                r = r.replace("FIM DA QUESTÃO", '')
            except:
                pass
            try:
                r = r.replace("FIM DA RESPOSTA", '')
            except:
                pass
            respostas2.append(r)
        except:
            respostas2.append(r)

    print("respostas - ", respostas2)
    return respostas2


@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        materia = request.form['materia']
        assunto = request.form['assunto']
        questoes = gerar_questoes(materia, assunto)
        respostas_questoes = gerar_respostas(questoes) if questoes else None
        return render_template('resultado.html', materia=materia, assunto=assunto, questoes=questoes, respostas=respostas_questoes)
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run()

import json
import requests
import config



def chat(materia, assunto):
    headers = {"Authorization" : f"Bearer {config.token}", "Content-Type": "application/json"}
    
    data = {
        "model": config.model,
        "messages":[{
            "role": "user",
            "content": f"""FAÇA EXATAMENTE DA FORMA QUE SE PEDE, gere 10 questões de {materia} sobre {assunto} numeradas de 1 a 10 com um prefixo de
                         "Questão <número da questão> - ", 
                         separe cada uma, exceto a ultima, por 'FIM DA QUESTÃO'"""
            }]
    }
    
    data = json.dumps(data)
    
    try:
        req = requests.post(url = config.url, headers= headers, data=data)
        res = req.json()
        res = res['choices'][0]['message']['content']
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
    except Exception as e:
        print(e)
        questions2 = None

    #print("questoes - ", questions2)
    return questions2


def respostas(questoes):
    
    headers = {"Authorization" : f"Bearer {config.token}", "Content-Type": "application/json"}
    
    data = {
        "model": config.model,
        "messages":[{
            "role": "user",
            "content": f"""FAÇA EXATAMENTE DA FORMA QUE SE PEDE,  responda essas questões {questoes} numerando elas  de 1 a 10, 
                    com um prefixo de "Resposta <número da resposta> - ", 
                    separe cada uma por 'FIM DA RESPOSTA', exceto a ultima, """
            }]
    }
    data = json.dumps(data)
    req = requests.post(url = config.url, headers= headers, data=data)
    res = req.json()
    res = res['choices'][0]['message']['content']
    respostas = res.split('FIM DA RESPOSTA\n')

    respostas2 = []

    for i, r in enumerate(respostas):
        try:
            try:
                r = r.replace("\n", "")
                r = r.replace(f"Resposta {i + 1} -", "R:")
                r = r.replace("FIM DA RESPOSTA", '')
                respostas2.append(r)
            except Exception:
                pass
        except:
            respostas2.append(r)

    #print("respostas - ", respostas2)
    return respostas2


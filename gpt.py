import json
import requests

with open("config.json", encoding="utf-8") as confJson:
    conf = json.load(confJson)
    

def chat(materia, assunto):
    headers = {"Authorization" : f"Bearer {conf['token']}", "Content-Type": "application/json"}
    
    data = {
        "model": conf["model"],
        "messages":[{
            "role": "user",
            "content": f'gere 8 questões de {materia} sobre {assunto} numeradas de 1 a 8'
            }]
    }
    
    data = json.dumps(data)
    try:
        req = requests.post(url = conf['url'], headers= headers, data=data)
        res = req.json()
        res = res['choices'][0]['message']['content']
        res = str(res)
        questions = res.split('\n')
    except:
        questions = None
    return questions

def respostas(questoes):
    
    headers = {"Authorization" : f"Bearer {conf['token']}", "Content-Type": "application/json"}
    
    data = {
        "model": conf["model"],
        "messages":[{
            "role": "user",
            "content": f'resposta essas questões numerando e colocando cada resposta em uma linha {questoes}'
            }]
    }
    
    
    data = json.dumps(data)

    req = requests.post(url = conf['url'], headers= headers, data=data)
    res = req.json()
    res = res['choices'][0]['message']['content']
    res = str(res)
    respostas = res.split('\n')
    return respostas
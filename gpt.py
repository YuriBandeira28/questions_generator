import json
import requests
import config



def chat(materia, assunto):
    headers = {"Authorization" : f"Bearer {config.token}", "Content-Type": "application/json"}
    
    data = {
        "model": config.model,
        "messages":[{
            "role": "user",
            "content": f"""somente gere 8 questões de {materia} sobre {assunto} numeradas de 1 a 8 com um prefixo de
                         "Questão <número da questão> - ", 
                         separe cada uma por '========================'"""
            }]
    }
    
    data = json.dumps(data)
    try:
        req = requests.post(url = config.url, headers= headers, data=data)
        res = req.json()
        res = res['choices'][0]['message']['content']
        res = str(res)
        questions = res.split('========================\n')
    except:
        questions = None
    return questions


def respostas(questoes):
    
    headers = {"Authorization" : f"Bearer {config.token}", "Content-Type": "application/json"}
    
    data = {
        "model": config.model,
        "messages":[{
            "role": "user",
            "content": f"""somente responda essas questões {questoes} numerando elas  de 1 a 8, 
                    com um prefixo de "Resposta <número da resposta> - ", 
                    separe cada uma por '========================'"""
            }]
    }
    data = json.dumps(data)
    req = requests.post(url = config.url, headers= headers, data=data)
    res = req.json()
    res = res['choices'][0]['message']['content']
    res = str(res)
    respostas = res.split('========================\n')
    return respostas


## testes

"""
quest = chat("Python", "Orientação a objetos")
print("questões - ", quest)
with open("questões.txt", "w") as q:
    for qu in quest:
        q.write(qu)
        q.write("\n\n")

resp = respostas(quest)
print("repostas - ", resp)
with open("respostas.txt", "w") as q:
    for r in resp:
        q.write(r)
        q.write("\n\n")
"""
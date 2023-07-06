import connect 
import datetime
import time
def salva_bd(materia, assunto, perguntas, respostas):
    ts = datetime.datetime.now()
    try:

        conn = connect.connect()
        conn._set_autocommit(True)
        cursor = conn.cursor()

        for p in perguntas:
            try:
                cursor.execute(f"""INSERT INTO questoes_e_respostas (materia, assunto, pergunta, resposta, ts) 
                            VALUES ('{materia}', '{assunto}', '{p}', '{respostas[perguntas.index(p)]}', '{ts}')""")
        
                #conn.commit()
            except Exception as e:
                print(f"erro {e}")
                print("Houve um erro ao inserir os dados no Banco de dados")
        conn.close()
        cursor.close()

        return "Inserção Realizada no Banco de Dados"
    except Exception as e:
        try:
            conn.close()
            cursor.close()
        except:
            pass

        return "Erro ao Inserir no Banco de Dados"

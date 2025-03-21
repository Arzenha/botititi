import openai
import os
# Armazene a chave da API em uma variável de ambiente para maior segurança
openai.api_key = os.getenv('OPENAI_API_KEY')

def enviar_mensagem(mensagem, lista_mensagens=None):
    if lista_mensagens is None:
        lista_mensagens = []
    
    lista_mensagens.append({'role': 'user', 'content': mensagem})
    
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagens,
    )

    # Retorna a mensagem no formato correto
    return resposta['choices'][0]['message']

lista_mensagens = []
while True:
    texto = input('Escreva uma mensagem: ')
    
    if texto.lower() == 'sair':
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        lista_mensagens.append({'role': 'assistant', 'content': resposta['content']})
        print('Robs:', resposta['content'])
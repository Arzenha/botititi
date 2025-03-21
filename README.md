# Bot de Chat com OpenAI

Este projeto é um exemplo simples de um bot de chat que utiliza a API da OpenAI para interagir com o modelo `gpt-3.5-turbo`. 
O bot permite que o usuário envie mensagens e receba respostas geradas pelo modelo de IA.

## Como funciona o código

1. **Configuração da API**:
   - A chave da API da OpenAI é carregada a partir de uma variável de ambiente chamada `OPENAI_API_KEY` para garantir segurança.
   - Certifique-se de configurar essa variável de ambiente antes de executar o código.

2. **Função `enviar_mensagem`**:
   - Esta função recebe uma mensagem do usuário e uma lista de mensagens anteriores.
   - A mensagem do usuário é adicionada à lista no formato esperado pela API da OpenAI.
   - A função faz uma chamada à API da OpenAI para obter uma resposta do modelo.
   - A resposta é retornada no formato correto para ser usada no programa.

3. **Loop principal**:
   - O programa entra em um loop onde o usuário pode digitar mensagens.
   - Se o usuário digitar "sair", o programa encerra.
   - Caso contrário, a mensagem é enviada para a função `enviar_mensagem`, e a resposta do modelo é exibida no console.

## Pré-requisitos

- Python 3.7 ou superior.
- Biblioteca `openai` instalada. Você pode instalá-la com o comando:
  ```bash
  pip install openai

"""
Lesson 1: Core Building Blocks of an Agent
  - models, prompts, chains, output parsers, memory, tools
  
order:
    1. Models, Prompts, Chains, Memory
    2. Tools
    
Prerequisites:
  pip install langchain langchain-openai python-dotenv
  
"""

import os   # os permite o acesso ao sistema operacional
from pathlib import Path
from dotenv import load_dotenv

script_dir = Path(__file__).resolve().parent
env_path = script_dir / ".env"


load_dotenv(dotenv_path=env_path)  # permite carregar variáveis de ambiente de um arquivo .env

print("ANTHROPIC_API_KEY found:", bool(os.getenv("ANTHROPIC_API_KEY")))

# 1. MODELS - The Reasoning Engine

from langchain.chat_models import init_chat_model

model = init_chat_model("claude-sonnet-4-6")

# response = model.invoke("What is the capital of France?")
# print("=== Model Response ===")
# print(response.content)
# print()

# 2. PROMPT TEMPLATES - Steering the Model

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

# PromptTemplate = Um texto com espaços em brancos para preencher com variáveis. Ele é usado para criar prompts dinâmicos para o modelo de linguagem.

# simple_template = PromptTemplate(
#     input_variables=["question"],
#     template="What is the capital of {question}?"
# )

# format() preenche os espaços em brancos com os valores das variáveis.

# formatted = simple_template.format(question="France")
# print("=== Formatted Prompt ===")
# print(formatted)
# print()


# ChatPromptTemplate = criado a partir de "papeis" (sistema, humano), que podem ser usados para criar prompts dinâmicos para o modelo de linguagem. Sistema define o comportamento do modelo, enquanto o humano define a entrada do usuário.

chat_prompt = ChatPromptTemplate.from_messages([("system", "Você está indeciso em quem votar, mas é uma pessoa inteligente que defende o direito das minorias e a igualdade e, com base nisso, vai realizar sua escolha."), ("human", "Qual é a melhor escolha: {concept}? Explique o porquê.")])

# .format_messages() preenche os espaços em brancos com os valores das variáveis e retorna uma lista de mensagens, cada uma com um papel (sistema ou humano) e o conteúdo do prompt. É um método útil para verificar se as instruções do prompt estão corretas antes de enviar para o modelo de linguagem.

# messages = chat_prompt.format_messages(concept="Flávio Bolsonaro ou Lula")
# print("=== Formatted Chat Prompt ===")
# for message in messages:
#     print(f"{message.type}: {message.content}")
# print()


from langchain_core.output_parsers import StrOutputParser

# prompt preenche o espaço em branco -> model gera a resposta -> output parser processa a resposta do modelo
# StrOutputParser = processa a saída do modelo de linguagem e retorna uma string. Ele é usado para extrair informações relevantes da resposta do modelo.

# chain = chat_prompt | model | StrOutputParser()

# response = chain.invoke({"concept": "Flávio Bolsonaro ou Lula"})
# print("=== Chain Response ===")
# print(response)
# print()


# 4. MEMORY - Giving the model a sense of context

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

memory = InMemoryChatMessageHistory()

# Uma parte da conversa, assim teremos algo para "lembrar"
memory.add_message(HumanMessage(content="Qual é a melhor escolha: Flávio Bolsonaro ou Lula? Explique o porquê."))
memory.add_message(AIMessage(content="A melhor escolha é o Lula a depender das suas prioridades e valores. Flávio Bolsonaro e Lula têm visões políticas diferentes, e é importante considerar suas propostas, histórico e impacto em questões sociais, econômicas e ambientais antes de tomar uma decisão."))

print("=== Memory Content ===")
for message in memory.messages:
    print(f"{message.type}: {message.content}")
print()


# o placeholder {history} no prompt será substituído pelo histórico da conversa, permitindo que o modelo de linguagem tenha contexto sobre a conversa anterior e personalize sua resposta com base nesse contexto.
chat_with_memory = ChatPromptTemplate.from_messages([("system", "use o histórico da conversa para personalizar sua resposta"), ("placeholder", "{history}"), ("human", "{concept}")])

chain_with_memory = chat_with_memory | model | StrOutputParser()

response = chain_with_memory.invoke({"history": memory.messages, "concept": "em quem devo votar mesmo?"})
print("=== Chain with Memory Response ===")
print(response)
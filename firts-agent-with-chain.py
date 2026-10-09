"""
Lesson 1: Core Building Blocks of an Agent
  - models, prompts, chains, output parsers, memory, tools
  
order:
    1. Models, Prompts, Chains, Memory
    2. Tools
    
Prerequisites:
  pip install langchain langchain-openai python-dotenv
  
"""

import os   # os is used to access environment variables SO
from pathlib import Path
from dotenv import load_dotenv

script_dir = Path(__file__).resolve().parent
env_path = script_dir / ".env"


load_dotenv(dotenv_path=env_path)  # take environment variables from .env.

print("OPENAI_API_KEY found:", bool(os.getenv("OPENAI_API_KEY")))

# 1. MODELS - The Reasoning Engine

from langchain.chat_models import init_chat_model

model = init_chat_model("claude-sonnet-4-6")

response = model.invoke((" user", "What is the capital of France?"))
print("=== Model Response ===")
print(response.content)
print()

# 2. PROMPT TEMPLATES - Steering the Model

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

# PromptTemplate = Um texto com espaços em brancos para preencher com variáveis. Ele é usado para criar prompts dinâmicos para o modelo de linguagem.

simple_template = PromptTemplate(
    input_variables=["question"],
    template="What is the capital of {question}?"
)

# format() preenche os espaços em brancos com os valores das variáveis.
formatted = simple_template.format(question="France")
print("=== Formatted Prompt ===")
print(formatted)
print()


# ChatPromptTemplate = criado a partir de "papeis" (sistema, humano), que podem ser usados para criar prompts dinâmicos para o modelo de linguagem. Sistema define o comportamento do modelo, enquanto o humano define a entrada do usuário.
chat_prompt = ChatPromptTemplate.from_messages([("system", "You are a helpful assistant."), ("human", "Explain {concept} in simple terms.")])

# .format_messages() preenche os espaços em brancos com os valores das variáveis e retorna uma lista de mensagens, cada uma com um papel (sistema ou humano) e o conteúdo do prompt.
messages = chat_prompt.format_messages(concept="quantum computing")
print("=== Formatted Chat Prompt ===")
for message in messages:
    print(f"{message.role}: {message.content}")
print()

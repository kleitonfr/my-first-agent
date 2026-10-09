# My First Agent

Um agente simples construído em Python com **LangChain** e **Claude (Anthropic)**.

O projeto demonstra como um agente pode interpretar uma pergunta, escolher uma ferramenta e executar operações matemáticas como soma, multiplicação, divisão e raiz quadrada.

## Requisitos

- Python 3.10+
- Uma chave da Claude API
- Créditos disponíveis no Claude Console para realizar requisições

## 1. Clone o repositório

```bash
git clone https://github.com/kleitonfr/my-first-agent.git
cd my-first-agent
```

## 2. Crie o ambiente virtual

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Instale as dependências

As dependências utilizadas pelo projeto estão indicadas no arquivo `firts-agent.py`.

```bash
pip install -qU langchain "langchain[anthropic]"
pip install python-dotenv
```

## 4. Crie uma chave da Claude API

Acesse o **Claude Console**:

https://console.anthropic.com/

No Console, crie uma API key para utilizar a Claude API.

> A assinatura do Claude e o uso da Claude API/Console são serviços separados. Para realizar chamadas à API, é necessário configurar o faturamento e adicionar créditos de uso à organização.

## 5. Adicione créditos à conta

No Claude Console, configure o faturamento e adicione créditos de uso à organização.

Sem saldo/créditos disponíveis, as requisições à API não poderão ser realizadas.

## 6. Configure a API key

Na raiz do projeto, crie um arquivo chamado `.env`:

```env
ANTHROPIC_API_KEY=sua_chave_aqui
```

O arquivo `.env` já está incluído no `.gitignore`, portanto sua chave não deve ser enviada para o GitHub.

**Nunca coloque sua API key diretamente no código ou faça commit do arquivo `.env`.**

## 7. Execute o agente

Com o ambiente virtual ativado:

```bash
python firts-agent.py
```

O exemplo configurado no código envia a pergunta:

```text
Quanto é 15 vezes 8?
```

O agente deve identificar que precisa utilizar a ferramenta de multiplicação e retornar o resultado.

## Como funciona

O projeto possui quatro ferramentas matemáticas:

- `add` — soma dois números
- `multiply` — multiplica dois números
- `divide` — divide dois números e trata divisão por zero
- `square_root` — calcula a raiz quadrada e trata números negativos

O LangChain utiliza o modelo Claude para decidir qual ferramenta deve ser utilizada para responder à pergunta.

## Tecnologias

- Python
- LangChain
- Anthropic Claude
- python-dotenv

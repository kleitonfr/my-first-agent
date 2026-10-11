# My First Agent

Projeto de estudo para aprender os blocos fundamentais de aplicações com modelos de linguagem usando **Python**, **LangChain** e **Claude, da Anthropic**.

O repositório contém dois exemplos:

- `firts-agent.py`: um agente que pode escolher entre ferramentas matemáticas.
- `firts-agent-with-chain.py`: exemplos de modelo, prompt template, chain, parser e histórico de conversa em memória.

## Requisitos

- Python 3.10 ou superior
- Uma conta no [Anthropic Console](https://console.anthropic.com/)
- Uma chave de API da Anthropic e faturamento/créditos habilitados para chamadas à API

> A assinatura do Claude (claude.ai) e o uso da API no Anthropic Console são serviços separados. O uso da API pode gerar cobranças conforme o modelo e os tokens processados. Consulte os [preços da API](https://docs.anthropic.com/en/docs/about-claude/pricing).

## 1. Clone o repositório

```bash
git clone https://github.com/kleitonfr/my-first-agent.git
cd my-first-agent
```

## 2. Crie e ative o ambiente virtual

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Se estiver usando o Prompt de Comando (cmd.exe), ative com:

```bat
.venv\Scripts\activate.bat
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Instale as dependências

Com o ambiente virtual ativado, execute:

```bash
python -m pip install --upgrade pip
pip install -U langchain "langchain[anthropic]" python-dotenv
```

Esses pacotes fornecem a integração com LangChain, o conector Anthropic e o carregamento das variáveis de ambiente do arquivo `.env`.

## 4. Crie uma chave da API Anthropic

1. Acesse o [Anthropic Console](https://console.anthropic.com/).
2. Crie uma API key nas configurações de chaves.
3. Configure o faturamento e adicione créditos, se necessário, para habilitar as chamadas à API.

A disponibilidade de créditos e as configurações de faturamento são gerenciadas no Console da Anthropic. Veja também a [documentação oficial](https://docs.anthropic.com/en/docs/welcome).

## 5. Configure a variável de ambiente

Na pasta raiz do projeto, crie um arquivo chamado `.env` com o seguinte conteúdo:

```env
ANTHROPIC_API_KEY=sua_chave_aqui
```

Substitua `sua_chave_aqui` pela sua chave real. Não compartilhe essa chave e **nunca a envie para o GitHub**. O arquivo `.env` já está listado no `.gitignore`.

## 6. Execute os exemplos

### Exemplo 1: agente com ferramentas

```bash
python firts-agent.py
```

O exemplo chama o agente com a pergunta `Quanto é 15 vezes 8?`. O agente pode escolher entre estas ferramentas:

- `add`: soma dois números.
- `multiply`: multiplica dois números.
- `divide`: divide dois números e trata divisão por zero.
- `square_root`: calcula a raiz quadrada e trata números negativos.

O script imprime as mensagens da execução, incluindo chamadas às ferramentas e a resposta final.

### Exemplo 2: chains e memória

```bash
python firts-agent-with-chain.py
```

Esse exemplo demonstra:

- Inicialização do modelo Claude (`claude-sonnet-4-6`).
- Criação de um `ChatPromptTemplate`.
- Uso de `StrOutputParser` para obter a resposta como texto.
- Armazenamento de mensagens com `InMemoryChatMessageHistory`.
- Uso do histórico como contexto para uma nova pergunta.

**Observação:** o prompt desse segundo exemplo contém uma pergunta política fixa usada para demonstrar templates e memória. Edite o prompt e os exemplos no arquivo para experimentar outros assuntos.

## Estrutura do projeto

```text
my-first-agent/
├── .gitignore
├── firts-agent.py
├── firts-agent-with-chain.py
└── README.md
```

## Segurança

- Mantenha a chave em `.env` ou em uma variável de ambiente segura.
- Não imprima, compartilhe nem faça commit da chave.
- Monitore o uso e os custos no Anthropic Console.
- Se a chave for exposta, revogue-a e crie outra.

## Tecnologias

- Python
- [LangChain](https://www.langchain.com/)
- [Anthropic Claude API](https://docs.anthropic.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

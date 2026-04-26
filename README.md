# 🧠 Summarizer App — Pipeline de Sumarização com LangChain + Cohere

## 📌 Visão Geral

O **Summarizer App** é uma aplicação CLI em Python que implementa um pipeline de sumarização de textos utilizando **LangChain** e modelos da **Cohere**.

Ele permite processar documentos extensos e gerar resumos de alta qualidade para contextos como:

- Relatórios de projeto
- Transcrições de reuniões
- Documentação técnica
- Artigos internos
- Logs operacionais

---

## 🚨 Problema

Equipes lidam com grandes volumes de texto, causando:

- Perda de produtividade
- Dificuldade de entendimento
- Inconsistência de informação
- Atrasos na tomada de decisão

---

## 🎯 Solução

O sistema implementa um pipeline de IA que:

- Processa textos longos
- Divide o conteúdo em partes (chunking)
- Gera resumos parciais
- Consolida em um resumo final
- Oferece múltiplos formatos de saída

---

## 🏗 Arquitetura

Entrada (Texto / Arquivo)
↓
Loader (TXT / PDF)
↓
Text Splitter (Chunking)
↓
Map (Resumo por chunk)
↓
Reduce (Consolidação)
↓
Resumo Final

---

## ⚙️ Tecnologias

- Python 3.12
- LangChain
- Cohere
- argparse
- python-dotenv
- pypdf

---

## 📦 Estrutura do Projeto

summarizer-app/
├── .env
├── requirements.txt
├── main.py
└── engine/
    ├── processor.py
    └── summarizer.py

---

## 🔑 Configuração

### 1. Clone o projeto

git clone <SEU_REPOSITORIO>
cd summarizer-app

### 2. Crie o ambiente virtual

Windows:
python -m venv venv
venv\Scripts\activate

Linux / Mac:
python3 -m venv venv
source venv/bin/activate

### 3. Instale as dependências

pip install -r requirements.txt

### 4. Configure o .env

COHERE_API_KEY=SUA_CHAVE_AQUI

---

## ▶️ Execução

### Texto direto

python main.py --text "Seu texto aqui"

### Arquivo TXT

python main.py --file exemplo.txt

### Arquivo PDF

python main.py --file documento.pdf

---

## 🧠 Modos de Sumarização

python main.py --file exemplo.txt --mode short
python main.py --file exemplo.txt --mode detailed
python main.py --file exemplo.txt --mode bullet
python main.py --file exemplo.txt --mode executive

### Tipos

- **short** → resumo curto
- **detailed** → resumo detalhado
- **bullet** → pontos principais
- **executive** → foco em decisão

---

## ✂️ Chunking

- Técnica: RecursiveCharacterTextSplitter
- Chunk size: 1000
- Overlap: 200

### Motivo

- Evita perda de contexto
- Permite textos grandes
- Mantém coerência

---

## 🔄 Pipeline

### Map

Resumo individual de cada chunk

### Reduce

Consolidação final

---

## 🤖 Modelo

- Cohere
- Modelo: command-light / fallback automático
- Temperatura: 0.2–0.3

---

## 📊 Exemplo

### Entrada

A empresa AlphaTech realizou uma reunião estratégica...

### Saída

O projeto apresentou atrasos devido a falhas de comunicação e requisitos. Foram definidas ações como melhoria da documentação e reorganização do backlog.

---

## 📌 Casos de Uso

- Resumo de relatórios
- Análise de reuniões
- Documentação técnica
- Extração de insights

---

## ⚠️ Limitações

- Dependência de API externa
- Limite de requisições
- Pode perder nuances técnicas

---

## 🚀 Melhorias Futuras

- Interface web
- Exportação para PDF
- Avaliação automática
- Multi-idioma
- Histórico

---

## 👨‍💻 Autor

Projeto desenvolvido para estudo de IA generativa com LangChain.

---

## 📄 Licença

Uso educacional.

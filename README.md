# 💸 Controle de Gastos Pessoais (CLI)

![CI](https://github.com/amachado2006/controle-gastos-cli/actions/workflows/ci.yml/badge.svg)

## 📌 Descrição do Problema Real

Muitas pessoas têm dificuldade em saber para onde vai o dinheiro no fim do mês. A falta de controle financeiro é uma dor real e frequente, especialmente entre estudantes e jovens adultos. Sem um registro simples dos gastos, é difícil economizar ou planejar o futuro.

## 💡 Proposta da Solução

Uma aplicação de linha de comando (CLI) simples e objetiva que permite registrar, listar, calcular e remover gastos pessoais. Os dados são salvos localmente em um arquivo JSON, sem necessidade de banco de dados ou conexão com internet.

## 👥 Público-alvo

Estudantes e jovens adultos que querem começar a controlar seus gastos de forma prática e sem complicações.

## ⚙️ Funcionalidades

- ✅ Adicionar um gasto (descrição, valor e categoria)
- ✅ Listar todos os gastos registrados
- ✅ Calcular o total gasto
- ✅ Remover um gasto pelo ID
- ✅ Dados salvos automaticamente em arquivo JSON

## 🛠️ Tecnologias Utilizadas

- Python 3.11+
- pytest (testes automatizados)
- flake8 (análise estática de código)
- GitHub Actions (CI)

## 📁 Estrutura do Projeto

```
controle-gastos-cli/
├── src/
│   └── gastos.py           # Código principal
├── tests/
│   └── test_gastos.py      # Testes automatizados
├── dados/                  # Criado automaticamente ao usar
│   └── gastos.json
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline de CI
├── requirements.txt        # Dependências
└── README.md
```

## 🚀 Instalação

**Pré-requisito:** Python 3.11 ou superior instalado.

```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/controle-gastos-cli.git
cd controle-gastos-cli

# Instale as dependências
pip install -r requirements.txt
```

## ▶️ Execução

```bash
python src/gastos.py
```

Você verá um menu interativo:

```
===== CONTROLE DE GASTOS PESSOAIS =====
1. Adicionar gasto
2. Listar gastos
3. Ver total gasto
4. Remover gasto
0. Sair
========================================
```

## 🧪 Rodando os Testes

```bash
pytest tests/ -v
```

## 🔍 Rodando o Lint

```bash
flake8 src/ tests/ --max-line-length=100
```

## 📦 Versão

**1.0.0**

Arthur Machado

## 🔗 Repositório

https://github.com/SEU_USUARIO/controle-gastos-cli

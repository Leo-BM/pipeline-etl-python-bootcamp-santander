# 🚀 Pipeline ETL - Marketing Bancário Personalizado

Projeto desenvolvido como parte do **Santander Bootcamp Ciência de Dados**, focado em aplicar conceitos de **ETL (Extract, Transform, Load)** e **Ciência de Dados** usando Python.

## 📋 Sobre o Projeto

Este projeto simula um pipeline de dados para geração de mensagens de marketing personalizadas para clientes bancários. O objetivo é demonstrar o fluxo completo de um processo ETL, desde a extração dos dados até o carregamento das informações processadas.

### 🎯 Problema de Negócio

Como cientista de dados, você precisa engajar clientes de forma personalizada, criando mensagens de marketing sob medida que incentivem investimentos, baseando-se no perfil e histórico de cada cliente.

## 🔧 Tecnologias Utilizadas

- **Python 3.8+**
- **JSON** (para persistência de dados)
- **Conceitos de ETL**
- **Lógica de Programação**

## 📊 Arquitetura do Pipeline

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   EXTRACT   │ --> │  TRANSFORM   │ --> │    LOAD     │
│             │     │              │     │             │
│ Dados dos   │     │ Geração de   │     │ Salvamento  │
│ Clientes    │     │ Mensagens    │     │ em JSON     │
└─────────────┘     └──────────────┘     └─────────────┘
```

### 1️⃣ Extract (Extração)
- Carrega dados dos clientes (simulados em lista Python)
- Na vida real: poderia ser uma API REST, banco de dados ou arquivo CSV

### 2️⃣ Transform (Transformação)
- Analisa o perfil de cada cliente
- Gera mensagens personalizadas baseadas em regras de negócio
- Simula o uso de IA Generativa (ChatGPT/Claude)

### 3️⃣ Load (Carregamento)
- Salva os dados processados em arquivo JSON
- Na vida real: poderia ser um PUT em API REST ou INSERT em banco de dados



## 🎓 Conceitos Aprendidos

- ✅ Fluxo ETL (Extract, Transform, Load)
- ✅ Manipulação de estruturas de dados em Python
- ✅ Lógica de personalização baseada em regras
- ✅ Persistência de dados em JSON
- ✅ Boas práticas de código e documentação

## 👤 Autor

**Leonardo Bento Maria**

- LinkedIn: [https://www.linkedin.com/in/leonardo-bento-maria)

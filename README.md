# 📘 Painel Web – Integração via Arquivos

Um sistema simples e flexível para consolidar informações em um dashboard web.  
Os dados podem ser extraídos automaticamente de arquivos estruturados (TXT, CSV, JSON etc.), processados por um backend e exibidos em uma interface limpa e acessível para qualquer contexto — seja produtividade de uma fábrica, relatórios financeiros, métricas de TI ou indicadores personalizados.

---

## 📌 Visão Geral / Contexto

Muitos profissionais precisam acompanhar métricas ou indicadores que são gerados em relatórios periódicos.  
Normalmente esses dados vêm em arquivos (TXT, CSV, JSON etc.) e acabam sendo atualizados manualmente em planilhas ou apresentações.

Esse projeto tem como objetivo automatizar esse processo: ler os arquivos, processar as informações e exibir tudo em um dashboard web simples e atualizado automaticamente.

**Motivação:**  
- Evitar atualizações manuais em relatórios.  
- Reduzir tempo gasto em tarefas repetitivas.  
- Garantir indicadores sempre atualizados e acessíveis.

---

## 📊 Status do Projeto

- 🚧 Em desenvolvimento  

---

## 🚀 Tecnologias Utilizadas

- Python 
- Flask 
- HTML
- JavaScript

---

## 🛠️ Funcionalidades

- Integração backend + frontend via Flask
- Endpoint `/api/dados` retornando JSON com:
  - `valor`: número lido do CSV
  - `modificado`: horário da última atualização do arquivo
- Painel em tela cheia exibindo o número e a última atualização
- Atualização automática a cada 15 minutos


---

## 📂 Estrutura do Projeto

```
painel-web/
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   └── script.js
├── .env.example
├── README.md
└── .gitignore
```

---

## 📦 Instalação / Como Executar

```bash
# Clone o repositório
git clone https://github.com/pablosscosta/painel-web.git

# Acesse a pasta do projeto
cd painel-web/backend

# Ative o ambiente virtual
source venv/bin/activate   # Linux/Mac
.\venv\Scripts\activate    # Windows PowerShell

# Instale as dependências
pip install -r requirements.txt

# Inicie o projeto
python app.py

# Acesse no navegador:
http://127.0.0.1:5000/  → frontend
http://127.0.0.1:5000/api/dados → API
```

---

## ⏭️ Próximas Etapas

- [ ] Adicionar transições visuais ao número

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 👤 Autor / Contato

**Pablo Sousa da Costa**  
[LinkedIn](https://www.linkedin.com/in/pablosilva013/)  
📧 pablosousa013@gmail.com
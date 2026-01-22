
# Painel Web
Um sistema simples e flexível para consolidar informações em um dashboard web. Os dados podem ser extraídos automaticamente de arquivos estruturados (TXT, CSV, JSON etc.), processados por um backend e exibidos em uma interface limpa e acessível.

## Visão Geral
### O que este sistema faz
Transforma dados de arquivos em painéis web que atualizam automaticamente. Ideal para situações onde você tem informações sendo salvas em arquivos e precisa visualizá-las em tempo real.

### Em termos simples:
1. Lê dados de um arquivo que você especificar
2. Mostra esses dados em uma página web
3. Atualiza automaticamente quando o arquivo muda
4. Funciona com diferentes tipos de arquivos e formatos

### Para que usar:
**Alguns exemplos práticos:**
- Monitorar valores de sensores ou equipamentos
- Acompanhar métricas de sistemas
- Visualizar resultados de cálculos ou processos
- Criar painéis para indicadores que são salvos em arquivos

## Contexto
### Caso de uso real: Monitoramento de Produção Industrial
Este sistema foi desenvolvido para resolver um problema concreto em uma linha de produção:    

**Problema:**
Líderes de produção precisavam acompanhar o número de peças fabricadas em tempo real. Os dados vinham de um relatório .pdf gerado pelo sistema ERP, que era copiado para um PowerPoint atualizado manualmente.

**Solução implementada:**
1. Um script extrai as informações do relatório gerado pelo ERP para CSV
2. Este sistema lê o arquivo CSV e exibe o valor atual
3. O painel fica visível em um monitor na fábrica
4. Atualização automática do valor

**Resultado:**
- Eliminou atualizações manuais do PowerPoint
- Todos na fábrica podem ver a produção atual
- Dados em tempo real para tomada de decisão

## Tecnologias

- Python
- Flask (Backend)
- HTML/CSS/JavaScript (Frontend)
- Server-Sent Events (SSE) para atualização em tempo real

## Funcionalidades

- Backend Flask com frontend integrado
- Endpoint `/api/dados` retornando JSON com:
  - `valor`: dado lido do arquivo
  - `modificado`: horário da última atualização
- Painel em tela cheia com número e timestamp
- Atualização automática (via Server-Sent Events)

## Instalação e execução
### Pré-requisitos

- [Python](https://www.python.org/downloads/) (em máquinas com Windows 7: [versão 3.7.9](https://www.python.org/downloads/release/python-379/))

### Obtenção do código-fonte

**Opção 1: Download direto (recomendado para máquinas sem Git)**
1. Acesse: https://github.com/pablosscosta/painel-web
2. Clique no botão verde "Code"
3. Selecione "Download ZIP"
4. Extraia o arquivo ZIP em uma pasta local

**Opção 2: Via Git (para desenvolvedores)**
```
git clone https://github.com/pablosscosta/painel-web.git
```

### Preparação do ambiente
1. Acessa a pasta do projeto:
```
cd painel-web\backend
```

2. Crie a ative o ambiente virtual Python:
```
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:
```
pip install -r requirements.txt
```

### Configuração

1. **Crie o arquivo `.env`:**
   - Na pasta `backend\`, clique com o botão direito → Novo → Documento de texto
   - Renomeie para `.env` (incluindo o ponto no início)

2. **Conteúdo do arquivo `.env`:**
```
CSV_PATH=C:\caminho\para\seu\arquivo.csv
```
*Substitua pelo caminho completo do arquivo que será lido*

3. **Formato esperado do arquivo:**
- O sistema lê apenas a primeira coluna
- Exemplo de conteúdo: `1234` (apenas o número)

### Execução

1. Com o ambiente virtual ativado, execute:
```
python app.py
```

2. O servidor iniciará em `http://localhost:5000`

3. Acesse no navegador:
- Painel principal: `http://localhost:5000/painel-prod`
- API de dados: `http://localhost:5000/api/dados`

4. Para usar em exibição dedicada:
- Abra o painel principal
- Pressione F11 para tela cheia
- Posicione no monitor desejado

### Autor

**Pablo Sousa da Costa**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/pablosilva013)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/pablosscosta)
[![Email](https://img.shields.io/badge/Email-pablosousa013%40gmail.com-red?logo=gmail)](mailto:pablosousa013@gmail.com)

Desenvolvedor do sistema. Para dúvidas ou sugestões, entre em contato.
# Ferramenta de Geração Automática de Testes Unitários em Python

Este projeto consiste numa ferramenta interativa que gera automaticamente testes unitários para funções Python. A geração baseia-se na análise do código-fonte via AST (Abstract Syntax Tree), com apoio de heurísticas e técnicas de aprendizagem automática leve (ML).

## Funcionalidades

- Interface gráfica simples e intuitiva (Tkinter)
- Suporte para ficheiros individuais ou projetos completos
- Análise automática de funções via AST
- Inferência de tipos e geração de valores com base em dados estatísticos
- Escrita automática de testes unitários com `unittest`
- Execução e apresentação do relatório de cobertura com `coverage.py`
- Componente de ML que aprende valores típicos usados em testes

## Requisitos

Python 3.12+

Bibliotecas:

tkinter (já incluída no Python)

coverage

scikit-learn

numpy


## Como Usar

### 1. Clonar o repositório

git clone https://github.com/teu-username/ferramenta-testes-python.git
cd ferramenta-testes-python

### 2. Criar um ambiente virtual

python3 -m venv venv
source venv/bin/activate   

### 3. Instalar as dependências

pip install -r requirements.txt

### 4. Executar a ferramenta

python main.py


## Exemplo de Utilização

1.Carrega um ficheiro ou uma pasta de projeto.

2. A ferramenta analisa automaticamente as funções.

3. São gerados testes baseados nas combinações possíveis de entradas.

4. Executa os testes e exibe o relatório de cobertura.

5. Podes editar os testes e regenerar conforme necessário.


# Autor

Desenvolvido por Diogo Cambeiro no âmbito do estágio da Licenciatura em Engenharia Informática – Universidade de Évora.

Supervisor: Prof. Rui Oliveira




# Definição das Entradas para o Hugging Face

## Análise do Repositório AnythingLLM

Para definir o que usar como entrada no **Hugging Face**, acessei o repositório do [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm), onde procurei pelas pastas que continham mais informações relevantes sobre o projeto, como:


- `package.json`
- `frontend/package.json`
- `server/package.json`
- `collector/package.json`
- `docker/Dockerfile`

Dentro dessas pastas, analisei os trechos de código que poderiam me ajudar a compreender melhor a estrutura do projeto. Durante esse processo, também pesquisei sobre cada parte para identificar quais arquivos e linhas seriam mais importantes para utilizar como entrada.

---

## Geração de Novo Conjunto de Dados

Em uma abordagem complementar, visando gerar um novo conjunto de dados (input) a ser processado pelos modelos adotados pelos demais integrantes da equipe, optei por analisar os logs disponíveis no repositório.  Com o objetivo de conferir maior robustez e generalização ao processo, desenvolvi um script em **Python** (`git_extractor.py`) que, utilizando a biblioteca `subprocess`, automatiza a extração e exportação em formato `.txt`** dos commits, branches e informações sobre autores a partir do repositório clonado localmente.

### Passos para utilização do script

1. **Clonar o repositório alvo localmente** utilizando o comando git clone.

2. **Editar a variável REPO** no script git_extractor.py, inserindo o caminho completo do repositório clonado.

Ao executar o script, os arquivos de saída (.txt) serão gerados na pasta git_output, criada automaticamente no diretório de execução.

# Engenharia_SoftwareII_2025-2_T04_AnythingLLM

## Projeto da Matéria de Engenharia de Software

### Equipe 3

1.  Ana Vitória de Almeida Bizo - `202200025401`
2.  Carlos Augusto Santos de Carvalho - `202200025448`
3.  Guilherme Lavrador Viana - `202200092450`
4.  Guilherme Menezes de Azevedo - `202200025804`
5.  João Guilherme Alves - `202200014711`
6.  Ravi Ribeiro Proença - `202300061779`
7.  Ricardo Nabuco Sampaio Santana do Couto - `202300038903`
8.  Uilson Alves dos Santos Neto - `201900115954`

---

**Link para o projeto (AnythingLLM):** [https://github.com/Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)

---

Análise de Arquitetura do AnythingLLM (Atividade 1)
Este repositório contém os artefatos, scripts e a análise da Atividade 1 da disciplina de Engenharia de Software II.


Universidade: Universidade Federal de Sergipe (UFS) 


Curso: Engenharia de Software II 


Orientador: Prof. Glauco de Figueiredo Carneiro 


Data: 2025 

🎯 Objetivo
O objetivo principal desta atividade foi identificar o padrão de arquitetura de software do projeto AnythingLLM. Para isso, foram utilizadas três abordagens distintas, empregando diferentes modelos de LLM (Large Language Models) do Hugging Face para analisar diferentes tipos de artefatos do projeto.


🔬 Metodologia: As Três Abordagens
Foram empregadas três técnicas de análise para triangular a arquitetura do projeto:

1. Abordagem 1: Classificação por Texto

Modelo: BAAI/bge-reranker-v2-m3 
Por que esse modelo:
* O bge-reranker-v2-m3 é um dos melhores modelos atuais para ranqueamento semântico, superando embeddings comuns quando a tarefa exige comparar pares de textos longos.
* Ele foi projetado para comparação texto-a-texto de alta precisão, ideal para descobrir qual descrição arquitetural é mais próxima do conteúdo do projeto.
* Ele usa cross-encoding, avaliando a similaridade considerando interações diretas entre tokens, o que aumenta muito a precisão em classificações deste tipo.
* É robusto para lidar com conteúdos textuais heterogêneos: commits, diffs, lista de arquivos e sumários — exatamente como no AnythingLLM.
* É adequado para situações em que a entrada não é um único documento bem estruturado, mas sim um conjunto de textos técnicos extraídos do repositório.

Input: Arquivos textuais extraídos do repositório (ex: commits.txt, files.txt, summary.txt).


Técnica: O modelo (um reranker) comparou o conteúdo textual agregado do projeto com descrições de padrões arquiteturais.


Resultado Principal: MVC (Score: -5.5664), seguido por Camadas (Layered) e Monolítico.

2. Abordagem 2: Embeddings Técnicos

Modelo: Qwen/Qwen3-Embedding-0.6B 
Por que esse modelo:
* É leve e roda bem em CPU.
* Tem boa performance semântica para comparação de textos.
* Funciona nativamente com `sentence-transformers`.
* Baixa latência e baixo custo computacional.
* Não exige GPU nem API externa — tudo roda localmente.


Input: Artefatos técnicos como package.json, Dockerfile e outros arquivos de configuração.


Técnica: Geração de embeddings (vetores) para os artefatos técnicos e para as descrições de arquiteturas, seguida pelo cálculo de similaridade de cosseno.

Resultado Principal: Microlítico (Score: 0.6583), seguido por Microserviços e Monolítico.

3. Abordagem 3: Embedding Textual Resumido (Zero-Shot)

Modelo: all-MiniLM-L6-v2 
Por que esse modelo:
* O all-MiniLM-L6-v2 é extremamente eficiente e rápido, ideal quando queremos gerar embeddings em tarefas zero-shot de forma leve.
* Produz vetores de alta qualidade para descrições curtas, como resumos de arquitetura — exatamente o formato usado na abordagem 3.
* Tem excelente desempenho em tarefas de similaridade semântica, mesmo com input pequeno, mantendo boa precisão.
* É amplamente utilizado como baseline por causa da combinação de qualidade + velocidade + baixo custo computacional.
* Funciona muito bem quando a entrada é apenas um resumo textual e não um conjunto de documentos longos.
* Input: Um resumo textual breve descrevendo as linguagens, frameworks e o funcionamento geral do projeto.


Técnica: Classificação Zero-Shot baseada em similaridade semântica (cosseno) entre o resumo do projeto e as descrições de arquitetura.


Resultado Principal: Orientada a Serviços (SOA) (Score: 0.9988), seguido por Plugin/Modular e Microserviços.

📊 Análise e Conclusão Final
A análise comparativa dos três resultados indica que nenhuma arquitetura única define o projeto. A conclusão é que a arquitetura mais condizente para o AnythingLLM é um monólito modular (microlítico).


Esta arquitetura principal é complementada por:

Um padrão Camadas (Layered) / MVC na aplicação web , que é composta por um frontend (React/Vite) e um server (Node/Express).

Um ecossistema de plugins , o que explica a alta pontuação de "SOA" e "Plugin/Modular" na Abordagem 3.



Por que "Monólito Modular"?

A Abordagem 2 (Embeddings Técnicos) foi a que melhor capturou a estrutura de implantação.

O projeto se autodeclara um monorepo.

Apesar de possuir dois processos principais (server e collector), eles residem no mesmo repositório e são comumente implantados juntos no mesmo artefato Docker. Isso difere de microserviços clássicos, que teriam implantação e governança independentes.


🚀 Como Reproduzir os Experimentos
Os tutoriais detalhados e os scripts para cada abordagem estão neste repositório.

1. Tutorial - BAAI/bge-reranker-v2-m3 (Classificação por Texto)

Objetivo: Comparar arquivos .txt (como commits.txt, files.txt) com descrições de arquiteturas.


Instalação:
pip3 install FlagEmbedding torch

Execução:

Garanta que todos os arquivos .txt de entrada estejam na mesma pasta que o script text-classification.py.


Execute o script:
python3 text-classification.py

Interpretação: O modelo retorna logits (valores negativos). Quanto maior o valor (menos negativo), maior a compatibilidade.


2. Tutorial - Qwen/Qwen3-Embedding-0.6B (Embeddings Técnicos)

Objetivo: Gerar embeddings de artefatos técnicos (ex: package.json) e calcular a similaridade de cosseno com padrões arquiteturais.


Dependências: O script utiliza a biblioteca sentence-transformers.
Instalação: pip install sentence-transformers scikit-learn numpy


Execução: O script carrega o modelo, gera os embeddings para as entradas (resumo de dependências e descrições de arquitetura) e calcula a similaridade.
Como executar: python extracao-embedding.py


3. Tutorial - all-MiniLM-L6-v2 (Zero-Shot Classification)

Objetivo: Calcular a similaridade semântica entre uma descrição textual do sistema e um dicionário de arquiteturas pré-definidas.

Instalação:
pip install sentence-transformers torch

Execução:

- Edite a variável description no bloco if __name__ == "__main__": do script para inserir o texto a ser analisado.
- Execute o script Python. Ele irá imprimir o ranking de arquiteturas mais prováveis.


🔗 Links Úteis

Vídeo de Apresentação (YouTube): https://youtu.be/FqMbKRy-whs 

👥 Equipe 3 e Contribuições

Ana Vitória de Almeida Bizo: feature-extractor e text-classification\
Carlos Augusto Santos de Carvalho: classificação zero-shot\
Guilherme Lavrador Viana: text-classification, análise e organização do repo\
Guilherme Menezes de Azevedo: feature-extractor e edição de vídeo\
João Guilherme Alves: geração de entrada do tipo artefatos\
Ravi Ribeiro Proença: geração de entrada do tipo sumário\
Ricardo Nabuco Sampaio Santana do Couto: geração de entrada do tipo .txt\
Uilson Alves: Não fez nada



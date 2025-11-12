# Tutorial — Identificando o padrão arquitetural do AnythingLLM usando `text-classification` (BAAI/bge-reranker-v2-m3)

Este tutorial explica, passo a passo, como eu chegar ao resultado que indica qual arquitetura é mais semelhante ao projeto **AnythingLLM**.  
O método escolhido foi **text-classification** com um *reranker* (modelo `BAAI/bge-reranker-v2-m3`) que compara os textos dos arquivos `.txt` com descrições de padrões arquiteturais e retorna um score de similaridade.  

> 💡 **Importante:** todos os arquivos `.txt` (ex.: `branches.txt`, `commits.txt`, `contributors.txt`, `diffs.txt`, `files.txt`, `summary.txt`) **devem estar na mesma pasta** onde você executa o script — o script lê todos esses arquivos localmente.

---

## 🧭 1. Resumo do processo

1. Escolher a *task* **text-classification** no Hugging Face.  
2. Usar o modelo **BAAI/bge-reranker-v2-m3** — um reranker de similaridade textual.  
3. Escrever descrições resumidas de várias arquiteturas de software (monolítico, microserviços, camadas etc.).  
4. Usar como entrada os arquivos `.txt` (commits, files, summary etc.).  
5. O script analisa o conteúdo dos `.txt` e calcula a similaridade entre o texto do projeto e cada descrição de arquitetura.  
6. O resultado indica qual arquitetura é mais compatível.

---

## ⚙️ 2. Por que o modelo `BAAI/bge-reranker-v2-m3`?

- Modelos **reranker** são feitos para comparar dois textos e medir o quanto eles se relacionam.  
- No caso, queremos saber **qual descrição de arquitetura se parece mais com o conteúdo do projeto**.  
- O modelo `bge-reranker-v2-m3` é uma escolha sólida por ser relativamente leve e eficiente em tarefas de similaridade textual.

---

## 📉 3. Por que os valores de similaridade são negativos?

Os scores retornados aparecem como:

monolitico -> Similaridade: -8.8984
microservicos -> Similaridade: -7.1562
plugin_modular -> Similaridade: -6.5430


Isso é **normal**.  
O reranker **não retorna probabilidades (0–1)**, e sim **valores de logit** — números reais (positivos ou negativos) que representam relevância.  
Eles **não devem ser interpretados literalmente**: apenas comparados entre si.

👉 **Quanto maior o valor (menos negativo), mais compatível o par de textos.**  
Por exemplo:  
`-6.5` indica mais compatibilidade do que `-9.2`.

---

## 🧰 4. Instalação dos pacotes necessários

No terminal, instale as dependências com:

```bash
pip3 install FlagEmbedding torch
```

## 📂 5. Estrutura esperada de arquivos
/meu_projeto/

├── branches.txt

├── commits.txt

├── contributors.txt

├── files.txt

├── summary.txt

└── text-classification.py

## 6 — Como executar o script

1. Abra o terminal e navegue até a pasta que contém o script `text-classification.py` e os arquivos `.txt`.

2. Garanta que as dependências estejam instaladas:
    ```bash
    pip3 install FlagEmbedding torch
    ```

3. Execute o script
    ```bash
    python3 text-classification.py
    ```
4. Observações:

    Na primeira execução o modelo será baixado (pode levar alguns minutos).

    Certifique-se de que todos os arquivos .txt estejam na mesma pasta do script.

### Exemplo de saída:

🏁 Resultado de similaridade das arquiteturas:

1. mvc                  -> Similaridade: -5.5664
2. camadas              -> Similaridade: -5.7656
3. monolitico           -> Similaridade: -6.2383
4. plugin_modular       -> Similaridade: -6.3984
5. microservicos        -> Similaridade: -6.6836
6. serverless           -> Similaridade: -7.3281
7. hexagonal            -> Similaridade: -7.8359
8. orientada_a_servicos -> Similaridade: -7.8984
9. event_driven         -> Similaridade: -8.3516
10. microlithico         -> Similaridade: -8.4141
11. pipe_and_filter      -> Similaridade: -8.7734
12. limpa                -> Similaridade: -9.4062

🔮 Arquitetura mais provável: MVC

## Interpretação do resultado

O modelo indica que o projeto se parece mais com a arquitetura cujo score é maior (menos negativo).

Nesse exemplo, o AnythingLLM foi considerado mais próximo de uma arquitetura "MVC".

**Os valores negativos não representam erro, apenas a forma interna de cálculo do modelo.**
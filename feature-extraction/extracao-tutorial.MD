# 📘 Análise de Similaridade Entre Padrões Arquiteturais

Este repositório contém um script Python que utiliza *embeddings* para identificar qual padrão arquitetural mais se aproxima semânticamente de uma descrição textual.
A técnica utilizada é baseada em **inferência local** com o modelo **Qwen/Qwen3-Embedding-0.6B**, que gera vetores numéricos para comparação via similaridade de cosseno.

---

## 🧠 Visão Geral

O objetivo do script é analisar um texto de entrada — já incluído no código — e compará-lo com um conjunto de descrições de padrões arquiteturais. A análise é totalmente baseada em embeddings, permitindo comparar textos por proximidade semântica.

O processo funciona assim:

1. Geramos o embedding da entrada.
2. Geramos o embedding de cada padrão arquitetural.
3. Calculamos as similaridades usando **cosseno**.
4. Ordenamos os resultados do mais semelhante ao menos semelhante.
5. Identificamos o padrão arquitetural mais provável.

---

## 🤖 Modelo Utilizado

Foi utilizado o modelo:

**Qwen/Qwen3-Embedding-0.6B**

Ele foi escolhido porque:

* É leve e roda bem em CPU.
* Tem boa performance semântica para comparação de textos.
* Funciona nativamente com `sentence-transformers`.
* Baixa latência e baixo custo computacional.
* Não exige GPU nem API externa — tudo roda localmente.

O modelo é carregado diretamente pela biblioteca `sentence-transformers` para gerar os embeddings.

---

## 📝 Sobre a Entrada e os Padrões

A entrada já está dentro do código, em:

```python
entrada = """
...
"""
```

Ela contém um resumo da arquitetura geral do projeto analisado.

Os padrões arquiteturais também estão definidos no código, dentro de um dicionário:

```python
padroes = {
    "monolitico": "...",
    "microservicos": "...",
    "microlithico": "...",
    ...
}
```

Cada descrição é comparada contra a entrada para medir qual padrão é semanticamente mais semelhante.

---

## 🛠️ Instalação das Dependências

Instale as dependências necessárias:

```bash
pip install sentence-transformers scikit-learn numpy
```

O modelo será baixado automaticamente quando o script for executado pela primeira vez.

---

## ▶️ Como Executar

Basta executar o arquivo principal:

```bash
python nome_do_arquivo.py
```

Ao rodar, o script irá:

* carregar o modelo Qwen Embedding
* gerar os embeddings
* calcular as similaridades
* mostrar as pontuações
* indicar o padrão arquitetural mais provável

Exemplo de saída:

```
microlithico        -> Similaridade: 0.7021
monolitico          -> Similaridade: 0.6810
camadas             -> Similaridade: 0.5102
...
Padrão mais provável: microlithico
```

---

## 📊 Interpretação dos Resultados

A similaridade de cosseno indica quão próximos semanticamente os textos são.
Quanto maior o valor (próximo de 1.0), mais a descrição do padrão arquitetural se aproxima da descrição do projeto.



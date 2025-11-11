from transformers import pipeline
from typing import Dict, Any, List

# ===============================================================
# 🔹 Dicionário de arquiteturas com descrições detalhadas
# ===============================================================
ARCHITECTURE_DESCRIPTIONS = {
    "MVC": (
        " Padrão arquitetural que separa a aplicação em três camadas principais: "
        "Model (dados e regras de negócio), View (interface de usuário) e Controller (lógica de controle). "
        "Essa separação facilita testes e manutenção. "
        "Ideal para aplicações web com interface rica. "
        "Pode aumentar a complexidade em sistemas grandes."
    ),

    "Microservices": (
        " Divide a aplicação em pequenos serviços independentes, "
        "cada um responsável por uma funcionalidade específica e comunicando-se via APIs (geralmente REST ou gRPC). "
        "Permite escalabilidade independente e deploy contínuo. "
        " Alta resiliência e flexibilidade tecnológica. "
        " Complexidade operacional elevada (monitoramento, comunicação, autenticação)."
    ),

    "Layered architecture": (
        " Estrutura clássica onde o sistema é dividido em "
        "camadas como apresentação, lógica de negócio e acesso a dados. "
        "As dependências seguem de cima para baixo. "
        " Simples de entender e aplicar. "
        " Dificulta testes isolados e pode gerar acoplamento entre camadas adjacentes."
    ),

    "Monolithic": (
        " Toda a aplicação é empacotada em um único artefato implantável, "
        "onde todos os módulos compartilham o mesmo ambiente de execução. "
        "Fácil de desenvolver e implantar inicialmente. "
        " Difícil de escalar e manter conforme o sistema cresce; pequenos erros podem afetar todo o sistema."
    ),

    "Event-driven architecture": (
        " Baseia-se em eventos que são emitidos e consumidos por serviços "
        "ou componentes. Usada para sistemas reativos e desacoplados. "
        "Alta escalabilidade e resposta em tempo real. "
        "Depuração e rastreamento de erros são complexos; exige infraestrutura de mensageria (Kafka, RabbitMQ)."
    ),

    "Plugin/modular architecture": (
        " O sistema é construído como um núcleo principal (core) "
        "com módulos independentes (plugins) que adicionam funcionalidades. "
        " Extensível e personalizável. "
        " Pode exigir um framework complexo de integração entre módulos."
    ),

    "Serverless": (
        "Baseada em funções executadas sob demanda em provedores de nuvem "
        "(como AWS Lambda, Google Cloud Functions ou Azure Functions). "
        " Reduz custo e manutenção de servidores; escala automaticamente. "
        " Latência inicial (cold start) e limitações de execução em funções longas."
    ),

    "CQRS": (
        "Separa as operações de leitura (Query) "
        "das operações de escrita (Command), permitindo otimizações distintas para cada fluxo. "
        " Alta performance em leitura e consistência eventual bem controlada. "
        " Implementação mais complexa e maior esforço de sincronização entre os modelos."
    ),

    "Hexagonal architecture": (
        "Organiza o sistema em torno de um núcleo de domínio, "
        "com portas e adaptadores para interagir com o mundo externo (banco, API, UI). "
        " Altamente testável e desacoplado de frameworks externos. "
        "️ Exige disciplina arquitetural e compreensão avançada de design de software."
    ),

    "Onion architecture": (
        " Variante da arquitetura hexagonal, "
        "em que o domínio central é envolto por camadas progressivas (aplicação, infraestrutura, interface). "
        " Mantém o domínio independente de frameworks. "
        " Pode ser excessivamente abstrata para projetos pequenos."
    ),

    "Client-server": (
        " Divide o sistema entre cliente (que solicita recursos) e servidor "
        "(que fornece serviços). É a base de aplicações web e de rede. "
        " Modelo simples e bem compreendido. "
        " Escalabilidade limitada se o servidor for um ponto único de falha."
    ),

    "Service-oriented architecture": (
        " Estrutura o sistema como um conjunto de serviços interoperáveis "
        "que seguem padrões de comunicação (SOAP, REST, etc.). "
        " Reutilização e integração facilitadas entre sistemas legados. "
        " Overhead de comunicação e necessidade de governança rigorosa."
    ),
}

# ===============================================================
# 🔹 Carregar modelo Zero-Shot Classification
# ===============================================================
def load_zero_shot_classifier(model_name: str = "MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7"):
    """
    Carrega o modelo zero-shot-classification (sem necessidade de treino).
    """
    return pipeline("zero-shot-classification", model=model_name)

# ===============================================================
# 🔹 Função de classificação por similaridade semântica
# ===============================================================
def classify_architecture(description: str,
                          architecture_descriptions: Dict[str, str],
                          model_name: str = "MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7",
                          multi_label: bool = True) -> Dict[str, Any]:
    """
    Usa zero-shot-classification para identificar qual arquitetura o texto mais descreve.
    """
    classifier = load_zero_shot_classifier(model_name)
    candidate_labels = list(architecture_descriptions.keys())

    result = classifier(description, candidate_labels, multi_label=multi_label)
    labels_scores = list(zip(result["labels"], result["scores"]))
    labels_scores = sorted(labels_scores, key=lambda x: x[1], reverse=True)

    return {
        "sequence": result.get("sequence", description),
        "labels_scores": labels_scores
    }

# ===============================================================
# 🔹 Impressão formatada
# ===============================================================
def pretty_print(result: Dict[str, Any], top_k: int = 6):
    print("\nTexto analisado:\n", result["sequence"][:600], "...\n")
    print(f"Top {top_k} arquiteturas mais prováveis (label : score):\n")
    for label, score in result["labels_scores"][:top_k]:
        print(f"  - {label:<30} : {score:.4f}")

# ===============================================================
# 🔹 Execução principal
# ===============================================================
if __name__ == "__main__":
    description = """
    Linguagem dominante é o JS.
    Frontend: ViteJs + React.
    Backend: NodeJs + Express (JS).
    Permite rodar localmente (Desktop) e em servidores (Docker).
    Funcionalidade principal: RAG (Geração Aumentada por Recuperação).
    Objetivo: construtor no-code de IAs.
    Suporta múltiplos modelos LLM (Gemini, OpenAI, Ollama, etc.).
    Permite escolher Vector DB (LanceDB, PGVector, Pinecone, etc.).
    Backend dividido em dois serviços NodeJS/Express:
      - Server: gerencia interações com DB.
      - Collector: coleta e processa documentos enviados.
    """

    result = classify_architecture(description, ARCHITECTURE_DESCRIPTIONS)
    pretty_print(result, top_k=12)

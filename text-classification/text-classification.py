from FlagEmbedding import FlagReranker
import os

reranker = FlagReranker('BAAI/bge-reranker-v2-m3', use_fp16=True)

textos = []
for nome_arquivo in ["branches.txt", "commits.txt", "contributors.txt", "diffs.txt", "files.txt", "summary.txt"]:
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            textos.append(f.read())

entrada = "\n".join(textos)

arquiteturas = {
    "monolitico": (
        "A arquitetura monolítica concentra toda a aplicação em um único bloco. "
        "Todos os módulos — interface, lógica de negócio e acesso a dados — estão integrados no mesmo código-base e são implantados juntos. "
        "É simples de desenvolver e testar, mas de difícil escalabilidade e manutenção, pois qualquer mudança exige o redeploy completo do sistema."
    ),

    "camadas": (
        "A arquitetura em camadas (ou em tiers) organiza o sistema em níveis lógicos, geralmente compostos por apresentação, negócio e dados. "
        "Cada camada se comunica apenas com a imediatamente inferior ou superior, promovendo separação de responsabilidades e modularidade. "
        "É comum em aplicações web tradicionais e facilita manutenção e testes, embora possa introduzir acoplamento entre camadas."
    ),

    "microservicos": (
        "A arquitetura de microserviços divide a aplicação em serviços pequenos, independentes e executáveis separadamente. "
        "Cada serviço possui sua própria lógica e banco de dados, comunicando-se via APIs, filas ou mensagens assíncronas. "
        "Essa abordagem aumenta a escalabilidade e a tolerância a falhas, mas adiciona complexidade operacional e necessidade de observabilidade e orquestração."
    ),

    "orientada_a_servicos": ( 
        "A arquitetura orientada a serviços (SOA) é baseada em serviços que expõem funcionalidades por meio de interfaces padronizadas. "
        "Diferente dos microserviços, os serviços SOA tendem a ser maiores e centralizados em um barramento de integração (ESB), "
        "favorecendo reuso, mas com menor independência e maior acoplamento entre módulos."
    ),

    "event_driven": (
        "A arquitetura orientada a eventos é centrada em produtores e consumidores de eventos. "
        "Os componentes reagem a mudanças de estado publicando ou escutando eventos através de um barramento assíncrono. "
        "Esse modelo reduz o acoplamento e melhora a escalabilidade, sendo útil em sistemas distribuídos e aplicações em tempo real."
    ),

    "serverless": (
        "Na arquitetura serverless, o código é executado sob demanda em funções hospedadas por provedores de nuvem, sem gerenciamento de servidores. "
        "Cada função é acionada por eventos específicos, permitindo escalabilidade automática e cobrança por uso. "
        "Ideal para workloads variáveis, mas depende fortemente do provedor e pode introduzir latência no cold start."
    ),

    "microlithico": (
        "A arquitetura microlítica (ou monólito modular) combina características de microserviços e monólitos. "
        "Os módulos são bem definidos e independentes dentro de um mesmo deploy, compartilhando o mesmo ambiente de execução. "
        "Facilita desenvolvimento e manutenção modular sem a complexidade operacional dos microserviços."
    ),

    "hexagonal": (
        "A arquitetura hexagonal (ou ports and adapters) separa a lógica central do sistema das interfaces externas, como banco de dados e APIs. "
        "A aplicação comunica-se com o mundo externo por meio de portas (interfaces) e adaptadores (implementações). "
        "Esse padrão facilita testes, substituição de dependências e manutenção de regras de negócio puras."
    ),

    "limpa": (
        "A arquitetura limpa (Clean Architecture) organiza o código em círculos concêntricos, onde a lógica de negócio é o núcleo e as dependências externas estão nas camadas mais externas. "
        "O fluxo de dependência é sempre de fora para dentro, mantendo o domínio independente de frameworks e infraestrutura."
    ),

    "mvc": (
        "O padrão MVC (Model-View-Controller) separa a aplicação em três componentes: Model (dados e regras), View (interface do usuário) e Controller (controle do fluxo). "
        "Esse padrão é amplamente utilizado em aplicações web e desktop, facilitando organização e reutilização de código."
    ),
    "pipe_and_filter": (
        "A arquitetura Pipe and Filter (tubos e filtros) organiza o processamento de dados como uma sequência de etapas independentes (filtros), "
        "onde cada filtro recebe uma entrada, processa-a e envia a saída para o próximo filtro através de um canal (pipe). "
        "Cada filtro é responsável por uma transformação específica, e os pipes servem apenas para transmitir dados entre eles. "
        "Essa arquitetura é útil em sistemas que realizam processamento de fluxo de dados contínuos, como compiladores, pipelines de dados e sistemas de processamento multimídia. "
        "Ela favorece a reutilização e a composição de componentes, já que filtros podem ser facilmente substituídos ou rearranjados."
    ),
    "plugin_modular": (
        "A arquitetura de plugins e modularidade permite que funcionalidades sejam adicionadas ou removidas dinamicamente através de módulos ou plugins independentes. "
        "O núcleo da aplicação fornece uma infraestrutura básica, enquanto os plugins estendem suas capacidades sem alterar o código principal. "
        "Esse padrão é comum em sistemas extensíveis, como IDEs, CMSs e plataformas de software que suportam customizações pelos usuários."
    ),
}

print("🔍 Analisando arquitetura com base nos arquivos de log...\n")

scores = {}
for nome, descricao in arquiteturas.items():
    score = reranker.compute_score([[entrada, descricao]])
    scores[nome] = float(score[0]) if isinstance(score, (list, tuple)) else float(score)

ordenado = sorted(scores.items(), key=lambda x: x[1], reverse=True)

print("🏁 Resultado de similaridade das arquiteturas:\n")
for i, (nome, valor) in enumerate(ordenado, start=1):
    print(f"{i}. {nome:20} -> Similaridade: {valor:.4f}")

melhor = ordenado[0][0]
print(f"\n🔮 Arquitetura mais provável: {melhor.upper()}")

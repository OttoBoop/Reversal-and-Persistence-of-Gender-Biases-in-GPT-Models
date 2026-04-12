# Plano Vivo - Notebook Replicavel do Paper de Vies de Genero

> Documento vivo criado em 2026-04-11. Atualize este arquivo sempre que uma decisao for tomada, uma lacuna for descoberta, ou uma nova rodada de agentes mudar o plano.

## 0. Objetivo

Criar uma versao clara, executavel e modificavel do notebook do projeto, para que:

1. peer reviewers consigam reproduzir os CSVs finais ou gerar versoes menores;
2. pesquisadores consigam modificar prompts, modelos, numero de repeticoes e escopo dos testes;
3. a analise final do paper seja reproduzivel a partir dos CSVs versionados;
4. a geracao completa via API fique documentada, mas sem obrigar todo usuario a gastar tempo/custo rodando tudo.

O alvo nao e apenas "limpar" o notebook antigo. O alvo e criar um fluxo reproduzivel com tres caminhos:

- **Caminho A - replicacao analitica:** usa os CSVs ja versionados em `data/raw/` e regenera tabelas/graficos.
- **Caminho B - regeneracao pequena:** usa a API para gerar CSVs pequenos de teste, baratos e auditaveis.
- **Caminho C - regeneracao completa:** documenta e permite uma execucao completa, mas com protecoes explicitas de custo.

## 1. Estado Atual Recuperado

### Artefatos principais

- `analysis/notebooks/march_2026_tcc_publicavel.ipynb`: notebook historico, avancado, com funcoes importantes, mas ainda preso a Colab/Drive, batch IDs e celulas exploratorias.
- `analysis/scripts/tcc_complete_analysis.py`: script limpo para reproduzir analises a partir dos CSVs consolidados.
- `data/raw/df_teste_1_unified.csv`: Teste 1 final/unificado.
- `data/raw/df_teste_2_unified.csv`: Teste 2 final/unificado.
- `data/raw/df_teste_3_unified.csv`: Teste 3 final/unificado.
- `data/derived/`: tabelas derivadas finais.
- `data/supporting/`: tabelas auxiliares, especialmente legacy/shot order.

### Diagnostico

O projeto esta em bom estado para reproducao **a partir dos CSVs finais**. Ainda nao esta em bom estado para reproducao **da geracao dos CSVs via API**.

O notebook novo deve preservar o poder do notebook antigo, mas trocar a experiencia de "caderno de pesquisa historico" por "protocolo auditavel".

### Mapa logico do notebook historico

Rodada de agentes de 2026-04-11 mapeou o notebook antigo assim:

- celulas 1-7: setup Colab/Drive, API key e configuracao (`MODELS`, `N_REPETITIONS = 30`);
- celulas 8-12: helpers iniciais de batch/download/parsing;
- celulas 13-29: geracao do Teste 1, com `create_story_tasks_reasoning(...)` e batch IDs hardcoded;
- celulas 30-78: classificacao de genero do Teste 1, com `create_gender_tasks(...)`, parsing e merges;
- celulas 79-102: geracao dos Testes 2 e 3, com `create_story_tasks_feedback(...)` e `create_story_tasks_position(...)`;
- celulas 103-142: classificacao de genero dos Testes 2 e 3, incluindo uma correcao manual na celula 128;
- celulas 143-163: multiplas versoes de plots;
- celulas 164-173: regressao OLS, incluindo uma versao corrigida e tabelas hardcoded;
- celulas 174-181: exploracoes/correlacoes antigas com dataframes fora do fluxo atual.

Funcoes candidatas a migracao:

- `create_story_tasks_reasoning`
- `create_story_tasks_feedback`
- `create_story_tasks_position`
- `create_gender_tasks`
- `run_batch_request`
- `check_batch_status`
- `download_batch_jsonl_text`
- `batch_to_dataframe` / `batch_to_dataframe_flexible`
- `classification_batch_to_clean_df`
- funcoes de plots/regressoes, preferencialmente alinhadas ao script limpo.

Trechos a evitar no fluxo principal:

- caminhos `/content/drive/...`;
- `files.download`;
- batch IDs como execucao principal;
- resultados hardcoded;
- multiplas versoes duplicadas de helpers;
- correcao manual sem arquivo/manifest de overrides.

## 2. Principios De Design Do Notebook

1. **Executavel de cima para baixo:** uma pessoa deve conseguir rodar cada caminho sem pular celulas ocultas.
2. **Separacao entre custo zero e custo API:** analise dos CSVs finais deve funcionar sem chave de API.
3. **Modo teste primeiro:** toda geracao via API deve ter um modo pequeno, barato e facil de revisar.
4. **Outputs isolados:** outputs de teste nunca devem sobrescrever CSVs finais versionados.
5. **Configuracao concentrada:** modelos, N, idiomas, testes, seed/identificadores e diretorios devem ficar em uma secao unica.
6. **Modificavel por pesquisadores:** prompts, modelos e desenho experimental devem ser faceis de localizar e alterar.
7. **Provenance explicita:** cada CSV deve ter origem, parametros e data de geracao documentados.
8. **Validacao embutida:** o notebook deve conferir colunas, tamanhos, nulos, duplicatas e consistencia de `story_id`.
9. **Chamadas reais so depois de validacao seca:** primeiro gerar codigo, JSONL e manifestos; so rodar API real quando as contagens pequenas estiverem claras e o codigo estiver revisado.
10. **Polling automatico de batches:** depois de submeter um batch, o notebook deve checar periodicamente ate o batch ficar pronto, falhar, expirar ou atingir timeout configurado.

## 3. Arquitetura Alvo

### 3.1 Notebook principal

Arquivo proposto:

- `analysis/notebooks/replicate_gender_bias_paper.ipynb`

Decisoes atuais:

- Idioma do notebook: ingles.
- Formato: um notebook unico, com secoes bem separadas.
- Regressao no notebook: `statsmodels`, pela legibilidade academica.
- Classificador de genero default: `gpt-4o-mini`, preservando o desenho original; deve ser configuravel.

Estrutura alvo:

1. **Introducao**
   - O que este notebook reproduz.
   - Diferenca entre replicacao analitica e regeneracao via API.
   - Custos e prerequisitos.

2. **Setup**
   - Imports.
   - Paths relativos ao repo.
   - Checagem de dependencias.
   - Configuracao de output.

3. **Configuracao**
   - `RUN_MODE = "analysis_only" | "dry_run" | "smoke" | "pilot" | "full_generation"`
   - `TESTS_TO_RUN = ["test1", "test2", "test3"]`
   - `MODELS_TO_RUN`
   - `CLASSIFIER_MODEL = "gpt-4o-mini"`
   - `N_REPETITIONS`
   - `LANGUAGES`
   - `OUTPUT_DIR`
   - `SUBMIT_BATCHES = False`
   - `POLL_BATCHES = True`
   - `BATCH_POLL_INTERVAL_SECONDS`
   - `BATCH_TIMEOUT_MINUTES`

4. **Carregar CSVs versionados**
   - Leitura de `data/raw/*.csv`.
   - Validacao de colunas obrigatorias.
   - Sumarios por teste/modelo/idioma/genero.

5. **Reproduzir analises finais**
   - Proporcoes.
   - Regresses legacy.
   - Graficos.
   - Comparacao com `data/derived/` e `data/supporting/`.

6. **Modo teste de geracao via API**
   - Gera poucas tarefas por teste.
   - Envia ou salva JSONL, dependendo de `SUBMIT_BATCHES`.
   - Quando enviar, monitora batch periodicamente ate conclusao.
   - Recupera resultados.
   - Classifica genero.
   - Une em CSV pequeno.

7. **Modo completo de geracao via API**
   - Mesmo pipeline do modo teste, mas com configuracao completa.
   - Protecoes contra execucao acidental.
   - Estimativa de numero de chamadas.

8. **Provenance e manifest**
   - Salvar `manifest.json` com parametros.
   - Salvar nomes de arquivos, hashes e contagens.
   - Registrar modelos e batch IDs quando aplicavel.

9. **Appendix**
   - Relacao com o notebook historico.
   - Como modificar prompts/modelos/N.
   - Limites conhecidos.

### 3.2 Modulos auxiliares possiveis

Se o notebook ficar longo demais, extrair codigo para:

- `analysis/scripts/replication_utils.py`
- `analysis/scripts/generation_utils.py`
- `analysis/scripts/validation_utils.py`

Decisao pendente: manter tudo autocontido no notebook para reviewers, ou extrair funcoes para scripts para facilitar manutencao.

## 4. Modos De Execucao

### 4.1 `analysis_only`

Objetivo: reproduzir tabelas e graficos a partir dos CSVs finais.

Nao requer API key. Deve ser o caminho recomendado para reviewers que querem validar a analise do paper.

Entradas:

- `data/raw/df_teste_1_unified.csv`
- `data/raw/df_teste_2_unified.csv`
- `data/raw/df_teste_3_unified.csv`

Saidas:

- `analysis/generated/`
- tabelas CSV regeneradas
- graficos PNG regenerados
- relatorio de comparacao com outputs versionados

### 4.2 `test_generation`

Objetivo: permitir que reviewers/pesquisadores testem a pipeline de geracao sem rodar o experimento inteiro.

Caracteristicas desejadas:

- poucos modelos;
- poucas repeticoes;
- poucos itens por teste;
- outputs em pasta separada;
- manifest obrigatorio;
- nunca sobrescrever `data/raw/`.

Saidas propostas:

- `analysis/generated/test_runs/<timestamp>/jsonl/`
- `analysis/generated/test_runs/<timestamp>/raw_outputs/`
- `analysis/generated/test_runs/<timestamp>/csv/`
- `analysis/generated/test_runs/<timestamp>/manifest.json`

Perfis recomendados:

#### `dry_run`

- Nao chama API.
- Gera JSONL local.
- Valida `custom_id`, `story_id`, schema, contagem esperada e duplicatas.
- Serve para revisar o desenho antes de gastar.

#### `smoke`

- Chama API com amostra minima.
- Sugestao inicial: `N_REPETITIONS = 1`.
- Sugestao inicial: `MODELS_TO_RUN = ["gpt-4o-mini"]`.
- Sugestao inicial: `CLASSIFIER_MODEL = "gpt-4o-mini"`.
- Modelos legacy (`davinci-002`, `babbage-002`) ficam fora do `smoke`: o caminho pequeno via batch deve seguir o fluxo moderno do notebook original, que gera batches e depois baixa as respostas automaticamente.
- Objetivo: provar que o fluxo API -> JSONL -> batch -> parsing -> classificacao -> merge -> CSV funciona.
- Nao tem objetivo estatistico.

Amostra sugerida para `smoke`:

- Teste 1: 2 categorias (`Leadership`, `Efficiency`), positivo/negativo, ingles/portugues = 8 historias por modelo.
- Teste 2: todos os quatro estimulos de valencia/idioma = 4 historias por modelo.
- Teste 3: 6 posicoes balanceadas (`CEO`, `secretary`, `pilot`, `flight attendant`, `professor`, `teacher`) = 6 historias por modelo.
- Total com 1 modelo e 1 repeticao: 18 historias + 18 classificacoes = 36 requests aproximadas.

#### `pilot`

- Chama API com amostra pequena, mas mais interpretavel.
- Sugestao inicial: `N_REPETITIONS = 3`.
- Sugestao inicial: `MODELS_TO_RUN = ["gpt-4o-mini", "gpt-4.1-nano-2025-04-14"]`.
- Com a mesma amostra acima: 108 historias + 108 classificacoes = 216 requests aproximadas.

Travas iniciais:

- `SUBMIT_BATCHES = False` por padrao.
- `MAX_TOTAL_TASKS_SMOKE = 100`.
- `MAX_TOTAL_TASKS_PILOT = 600`.
- Qualquer execucao acima disso deve exigir confirmacao explicita.

### 4.2.1 Polling de batches

Requisito novo decidido em 2026-04-11:

- depois de pedir um batch, o codigo deve checar periodicamente se ele ficou pronto;
- o polling deve ser configuravel por intervalo e timeout;
- o notebook deve imprimir estado resumido sem poluir demais a saida;
- estados finais esperados: `completed`, `failed`, `expired`, `cancelled`;
- quando o batch estiver `completed`, o codigo deve baixar e parsear a resposta automaticamente;
- quando falhar/expirar/cancelar, o codigo deve registrar erro em manifest e parar de forma clara.

API desejada:

```python
batch = submit_batch(jsonl_path, endpoint="/v1/responses")
batch = wait_for_batch(batch.id, poll_interval_seconds=180, timeout_minutes=180)
df = download_completed_batch(batch.id)
```

Para rodadas paralelas:

- submeter os batches de geracao dos Testes 1, 2 e 3;
- monitorar todos ate ficarem prontos;
- baixar e validar cada teste;
- criar e submeter os batches de classificacao de genero dos Testes 1, 2 e 3;
- monitorar os tres batches de classificacao;
- baixar, validar e fazer merge em paralelo/logicamente separado.

### 4.3 `full_generation`

Objetivo: regenerar os CSVs completos ou variacoes completas do estudo.

Deve ter protecoes:

- exige confirmacao explicita em uma variavel, por exemplo `CONFIRM_FULL_RUN = "YES_I_UNDERSTAND_COSTS"`;
- imprime estimativa de tarefas antes de enviar;
- salva manifest antes de chamar API;
- permite retomar de batch IDs salvos.

## 5. Validacoes Obrigatorias

### Para os CSVs finais

- arquivo existe;
- colunas esperadas presentes;
- `story_id` presente e unico dentro do escopo esperado;
- `gender` em valores esperados;
- `modelo` mapeia para familia;
- contagens por teste batem com valores documentados;
- sem vazamentos de outputs de teste em `data/raw/`.

Contagens documentadas:

- Teste 1: 17.973 linhas, 12 colunas.
- Teste 2: 2.040 linhas, 9 colunas.
- Teste 3: 12.600 linhas, 11 colunas.

Schemas esperados:

- Teste 1: `caracteristica`, `caracteristica_oposta`, `categoria`, `valencia`, `idioma`, `modelo`, `example_order`, `story_id`, `repetition`, `historia`, `gender`, `explanation`.
- Teste 2: `valencia`, `idioma`, `modelo`, `example_order`, `story_id`, `repetition`, `historia`, `gender`, `explanation`.
- Teste 3: `posicao`, `power_level`, `categoria`, `idioma`, `modelo`, `example_order`, `story_id`, `repetition`, `historia`, `gender`, `explanation`.

Observacoes a investigar:

- Teste 3 final tem 14 modelos e nao inclui `gpt-5.2-2025-12-11`.
- Testes 1/2 tem 15 modelos.
- Foi sinalizada uma `historia` ausente no Teste 1.
- `valencia` precisa ser normalizada entre ingles/portugues quando aplicavel.

### Para chamadas API

- API key encontrada apenas via variavel de ambiente ou arquivo `.env` local ignorado pelo Git;
- numero de tarefas calculado antes do envio;
- JSONL validado antes do upload;
- cada task tem `custom_id` rastreavel;
- batch IDs registrados no manifest;
- downloads conferidos contra numero esperado de tarefas;
- falhas ou linhas perdidas registradas explicitamente.
- chave de API nunca deve ser salva no notebook, em outputs, manifests ou arquivos versionados;
- em testes reais, preferir `OPENAI_API_KEY` no ambiente local.

### Para outputs

- tabelas regeneradas comparadas com `data/derived/` quando o modo for `analysis_only`;
- tolerancias numericas definidas;
- graficos regenerados salvos em pasta temporaria/generated;
- README ou manifest gerado junto dos outputs.

### Smoke tests do notebook

- Executar caminho `analysis_only` sem API key.
- Gerar todos os CSVs e PNGs esperados em `analysis/generated/`.
- Comparar CSVs regenerados com `data/derived/` e `data/supporting/`.
- Executar `dry_run` sem chamar API.
- Conferir que `smoke` nao consegue escrever em `data/raw/`.
- Conferir que o notebook roda linearmente com "Restart & Run All" no caminho sem API.
- Conferir que o `dry_run` gera JSONL pequeno para Testes 1, 2 e 3.
- Conferir que o codigo de polling esta preparado antes de usar uma chave real.
- Quando Otavio fornecer/configurar API key, rodar `smoke` real com N baixo nos tres testes e nas tres classificacoes de genero.

## 6. Estrategia De Agentes E Loops

### Loop padrao

1. **Explorar:** agentes leem notebook/script/dados e reportam achados.
2. **Consolidar:** atualizar este plano com decisoes, lacunas e perguntas.
3. **Perguntar:** quando houver decisao substantiva, parar e perguntar ao Otavio.
4. **Implementar fatia pequena:** editar apenas um conjunto claro de arquivos.
5. **Verificar:** rodar smoke tests, validacoes ou execucao parcial.
6. **Registrar:** atualizar este documento com resultado, decisoes e proximo passo.

### Agentes uteis

- **Agente notebook:** mapear celulas, duplicacoes e funcoes reaproveitaveis.
- **Agente test mode:** desenhar amostras pequenas, parametros e estimativa de chamadas.
- **Agente reviewer:** revisar experiencia de peer reviewer e checklist de reproducibilidade.
- **Agente dados:** validar formatos, contagens, colunas, `story_id`, duplicatas.
- **Agente prompts/API:** separar prompts, schemas, batch upload, download e parsing.

## 7. Fases Do Trabalho

### Fase 0 - Plano vivo

Status: concluida inicialmente; continua vivo.

Objetivo:

- criar este documento;
- registrar estado atual;
- levantar perguntas iniciais.

Criterio de pronto:

- Otavio aprova a direcao geral;
- perguntas abertas prioritarias respondidas ou explicitamente adiadas.

### Fase 1 - Auditoria do notebook antigo

Status: primeira rodada concluida por agentes em 2026-04-11; pode aprofundar quando formos migrar codigo.

Objetivo:

- mapear todas as celulas do notebook historico;
- identificar blocos reutilizaveis;
- separar codigo ativo, legado e duplicado.

Saida:

- tabela de celulas/blocos;
- lista de funcoes a migrar;
- lista de trechos a descartar ou arquivar.

Resultado parcial:

- celulas reutilizaveis e obsoletas registradas na secao 1;
- pendente reconciliar schema do Teste 3 entre notebook antigo e CSV final;
- pendente decidir como tratar override manual de genero da celula 128.

### Fase 2 - Esqueleto do notebook novo

Objetivo:

- criar notebook novo com secoes vazias ou parcialmente preenchidas;
- implementar `analysis_only`;
- implementar esqueleto de geracao pequena para os tres testes em `dry_run`;
- implementar configuracao de batch/polling, sem chamadas reais por padrao.

Saida:

- notebook executavel sem API;
- validacao dos CSVs finais;
- reproducao de tabelas e graficos usando codigo existente.
- JSONL pequeno gerado para Testes 1, 2 e 3 sem API;
- manifest de teste seco.

Status em 2026-04-11/12: primeira fatia implementada.

Arquivos criados/alterados:

- `analysis/notebooks/replicate_gender_bias_paper.ipynb`
- `requirements.txt`

Resultado validado:

- o notebook executou de ponta a ponta em modo `dry_run`, sem API key e sem chamadas reais;
- o caminho de analise leu os tres CSVs versionados de `data/raw/`;
- os CSVs regenerados em `analysis/generated/notebook_analysis/` bateram exatamente com `data/derived/` para os nove arquivos comparados;
- o notebook tambem gerou figuras de familia/valencia, idioma/valencia, shot order legacy, posicoes do Teste 3 e tabelas visuais de regressao em `analysis/generated/notebook_analysis/figures/`;
- o dry run gerou JSONL para geracao de historias e classificacao-placeholder nos Testes 1, 2 e 3;
- contagem do dry run: 8 tarefas de historia para Teste 1, 4 para Teste 2, 6 para Teste 3, e 18 tarefas de classificacao-placeholder; total 36 requests preparados;
- o manifest de teste seco foi salvo em `analysis/generated/test_runs/<timestamp>/manifest.json`;
- `data/raw/` e `data/derived/` nao foram modificados.

Limite consciente da primeira fatia:

- a classificacao-placeholder valida o formato das chamadas, mas o merge real geracao -> classificacao -> CSV pequeno ainda deve ser feito depois de baixar respostas reais de um smoke;
- a submissao, polling e download de Batch API estao implementados como helpers, mas ainda nao foram testados com chave real;
- a experiencia de peer reviewer ainda precisa de uma decisao final sobre o default: `analysis_only` por padrao, ou `dry_run` por padrao sem custo.

Recomendacao atual: fazer a revisao desta fase antes de qualquer chamada API real.

### Fase 3 - Modo teste de geracao

Objetivo:

- implementar geracao pequena de tarefas;
- salvar JSONL;
- enviar via API apenas quando o codigo estiver revisado e a chave estiver configurada;
- submeter e monitorar batches com polling periodico;
- baixar/classificar/unificar resultados pequenos.

Saida:

- CSVs pequenos de teste;
- manifest;
- documentacao de custo/numero de chamadas.
- relatorio de polling/status dos batches;
- validacao de merge geracao -> classificacao -> CSV.

### Fase 4 - Modo completo

Objetivo:

- transformar o modo teste em pipeline completo controlado;
- permitir retomar batches;
- documentar como gerar os tres CSVs finais.

Saida:

- fluxo completo auditavel;
- protecoes contra custo acidental;
- manifest completo.

### Fase 5 - Revisao de reviewer

Objetivo:

- rodar o notebook do zero em ambiente limpo;
- verificar se instrucoes sao suficientes;
- simular mudancas de modelo/N/prompt.

Saida:

- checklist final;
- README atualizado;
- eventuais ajustes em requirements/env.

## 8. Perguntas Abertas

### Perguntas prioritarias para Otavio

Respondidas em 2026-04-11:

1. Notebook em ingles.
2. Notebook unico, claramente separado.
3. Primeira parte: gerar codigo, validacoes e chamadas pequenas em seco; depois testar API real com N baixo quando o codigo estiver maduro e a chave estiver configurada.
4. Regressao com `statsmodels`.
5. Classificador de genero configuravel, default `gpt-4o-mini`, para preservar o desenho original.
6. Polling de batches a cada 180 segundos, com timeout inicial de 180 minutos para `smoke`/`pilot`.
7. `smoke` nao inclui legacy; segue o fluxo moderno de batch do notebook original.

Estas ainda travam detalhes da proxima implementacao:

8. A chave de API sera configurada via `OPENAI_API_KEY` no ambiente local quando chegar a hora do teste real?

### Escopo de reproducao

9. O notebook novo deve tentar reproduzir **os tres CSVs finais completos** via API, ou basta documentar o caminho completo e oferecer modo teste executavel?
10. Para peer reviewers, o caminho recomendado deve ser `analysis_only` por padrao?

### Modo teste

11. Quais modelos devem entrar no modo teste? Sugestao atual: `smoke` com `gpt-4o-mini`; `pilot` com `gpt-4o-mini` e `gpt-4.1-nano-2025-04-14`.
12. O modo teste deve fazer chamadas reais por padrao, ou apenas gerar JSONL e deixar o envio manual/opcional?

### API e custos

13. O projeto deve usar a OpenAI Batch API como caminho principal, ou tambem suportar chamadas sincronas pequenas para o modo teste?
14. Como queremos lidar com modelos que mudaram, foram descontinuados ou nao estao acessiveis para reviewers?
15. Devemos registrar uma tabela de custo estimado por modo?

### Arquitetura

16. O notebook deve ser autocontido, mesmo ficando maior, ou pode importar scripts auxiliares?
17. Devemos substituir partes do script atual por funcoes importaveis, ou duplicar temporariamente logica no notebook para clareza?
18. Devemos criar `environment.yml` ou `pyproject.toml`, alem de `requirements.txt`?

### Outputs

19. Outputs regenerados devem sempre ir para `analysis/generated/`?
20. Devemos criar uma pasta padrao para test runs com timestamp?

## 9. Log De Implementacao

### 2026-04-11/12 - Primeira versao do notebook replicavel

Implementado:

- notebook unico em ingles: `analysis/notebooks/replicate_gender_bias_paper.ipynb`;
- configuracao centralizada com `RUN_MODE`, `TESTS_TO_RUN`, `MODELS_TO_RUN`, `CLASSIFIER_MODEL`, `N_REPETITIONS`, `SUBMIT_BATCHES`, polling e confirmacoes de custo;
- validacao dos schemas finais dos tres CSVs;
- reproducao analitica com `statsmodels` para as regressoes legacy;
- exportacao de tabelas e figuras para `analysis/generated/notebook_analysis/`, incluindo figuras de familia/valencia, idioma/valencia, shot order legacy, posicoes do Teste 3 e tabelas visuais de regressao;
- comparacao automatica dos CSVs regenerados contra `data/derived/`;
- dry run pequeno para os tres testes, com JSONL de geracao e JSONL de classificacao-placeholder;
- manifest e inventario de outputs do dry run;
- helpers de Batch API: `submit_batch`, `wait_for_batch`, `wait_for_batches`, `download_completed_batch`, parsing robusto de JSONL de batch;
- protecoes para impedir submissao sem `CONFIRM_SUBMIT_BATCHES = "YES_SUBMIT_BATCHES"` e para impedir `full_generation` sem `CONFIRM_FULL_RUN = "YES_I_UNDERSTAND_COSTS"`;
- `requirements.txt` atualizado com `statsmodels`, `openai`, `tqdm`, `ipykernel`, `nbclient` e `nbformat`.

Validacoes realizadas:

- `python` leu e validou o JSON do notebook;
- dependencias instaladas na venv local;
- notebook executado com `nbclient` usando a venv local;
- comparacao gerada em `analysis/generated/notebook_analysis/comparison_with_data_derived.csv`;
- todos os nove CSVs comparados tiveram `passes=True` e `max_abs_numeric_diff=0.0`;
- `dry_run_jsonl_validation.csv` marcou `passes=True` para todos os seis JSONL gerados.

Perguntas novas/renovadas:

1. Para a versao destinada a peer reviewers, o default do notebook deve ser `RUN_MODE = "analysis_only"`? A primeira versao esta em `dry_run`, ainda sem custo, porque isso tambem gera JSONL pequeno automaticamente.
2. No proximo loop, a classificacao real do smoke deve ser implementada como uma secao imediatamente executavel apos download dos batches, ou como uma secao manual em duas etapas para facilitar auditoria?
3. Devemos transformar a correcao manual antiga da celula 128 em `data/supporting/manual_gender_overrides.csv`, mesmo que ela nao seja necessaria para os CSVs atuais?

### 2026-04-12 - Revisao critica do pipeline de geracao

Motivo:

- Otavio pediu uma comparacao cuidadosa com o plano e com o bloco historico, especialmente verificando se ha duas chamadas separadas: uma para gerar historias e outra para classificar genero.

Achado principal:

- a primeira versao preparava JSONL e polling, mas ainda deixava a montagem real `historias baixadas -> classificacao -> CSV final pequeno` como instrucao manual. Isso nao era suficiente para revisao humana do pipeline de geracao.

Correcoes implementadas:

- prompts de geracao alinhados mais de perto aos blocos historicos:
  - Teste 1 volta a usar a instrucao de historia em 1 paragrafo e inicio fixo `In this narrative, we follow` / `Nesta narrativa, acompanhamos`;
  - Teste 2 volta a usar o cenario de feedback no escritorio do gerente e inicio fixo `In this story we follow...` / `Nesta historia seguimos...`;
  - Teste 3 volta a usar o cenario em que o ocupante da posicao planeja iniciar um novo projeto;
- formato de `input` das chamadas `/v1/responses` alinhado ao notebook historico, usando itens `input_text`;
- schemas de geracao agora incluem metadados constantes e `historia`, em vez de apenas um campo generico `story`;
- schemas de classificacao agora incluem `story_id` constante alem de `gender` e `explanation`;
- acrescentado teste seco de ponta a ponta:
  1. simula outputs de batch de geracao;
  2. parseia esses outputs com os mesmos helpers usados para downloads reais;
  3. cria JSONL de classificacao a partir das historias parseadas;
  4. simula outputs de classificacao;
  5. faz merge historia + classificacao;
  6. grava `test1_dry_run_unified.csv`, `test2_dry_run_unified.csv` e `test3_dry_run_unified.csv` com os schemas finais;
  7. valida colunas, duplicatas, historias ausentes e generos ausentes.

Validacao nova:

- notebook executado novamente com `nbclient`;
- `dry_run_jsonl_validation.csv` passou para todos os JSONL;
- `dry_run_unified_csv_validation.csv` passou para os tres CSVs pequenos;
- contagens dos CSVs pequenos:
  - Teste 1: 8 linhas;
  - Teste 2: 4 linhas;
  - Teste 3: 6 linhas;
- todos os tres CSVs pequenos possuem exatamente as colunas finais documentadas.

Duvidas que permanecem antes de chamar API real:

1. O boundary live da OpenAI ainda nao foi testado: upload do arquivo, execucao do batch, polling real e download real.
2. A amostra `smoke` cobre apenas 2 categorias do Teste 1 e 6 posicoes do Teste 3; isso e bom para custo, mas nao prova o desenho completo.
3. A reproducao completa ainda precisa de uma tabela final de desenhos experimentais completos, nao apenas das amostras de smoke.
4. Ainda falta decidir se a correcao manual historica da celula 128 vira arquivo de provenance.
5. Quais outputs finais, alem dos nove CSVs ja comparados, devem ser comparados automaticamente com os versionados?
6. A correcao manual de genero da celula 128 deve virar um arquivo `manual_gender_overrides.csv` ou apenas uma nota de provenance?

### 2026-04-12 - Patch corretivo de exatidao historica

Decisao de Otavio:

- padrao metodologico deve ser byte-for-byte para prompts, schemas, nomes de campos, typos e peculiaridades historicas;
- escopo curto fica nos modelos modernos via Batch API;
- corrigir por patch em cima do historico atual, nao reverter tudo.

Correcoes aplicadas ao notebook:

- substituida a versao aproximada dos prompts por wrappers historicos fieis aos blocos originais:
  - Teste 1: `create_story_tasks_reasoning`, celulas 15/16 do notebook historico;
  - Teste 2: `create_story_tasks_feedback`, celulas 81/82;
  - Teste 3: `create_story_tasks_position`, celulas 81/83;
  - classificacao de genero: `create_gender_tasks`, celula 33;
- mantidos os padroes historicos de `custom_id`:
  - Teste 1: `story_0001_Liderança boa_pt_gpt-4o-mini_0`;
  - Teste 2: `analysis2_0001_positive_pt_gpt-4o-mini_0`;
  - Teste 3: `analysis3_0001_CEO_en_gpt-4o-mini_0`;
  - classificacao: `custom_id = story_id`, sem prefixo artificial;
- mantidos nomes e campos historicos de schema:
  - geracao usa `name = "story_response"`;
  - Teste 1 gera `caracteristica_neutra`, depois mapeada para `categoria` no CSV final;
  - Teste 3 gera `caracteristica` e `category`, depois mapeadas para `posicao` e `categoria`;
  - classificacao em portugues usa `classificacao_genero`, `gênero` e `explicação`;
  - classificacao em ingles usa `gender_classification`, `gender` e `explanation`;
- removida `temperature` das chamadas de geracao modernas, preservando o historico;
- mantida `temperature = 1.0` na classificacao, como no historico;
- parser ajustado para aceitar tanto campos em ingles quanto campos em portugues e normalizar apenas apos receber a resposta.

Validacao executada:

- notebook executado inteiro com `nbclient`;
- analise dos CSVs versionados continua batendo exatamente com `data/derived/`;
- dry run gerou 36 tarefas pequenas;
- CSVs pequenos `test1_dry_run_unified.csv`, `test2_dry_run_unified.csv` e `test3_dry_run_unified.csv` continuam passando validacao de schema final;
- validacao manual de forma historica passou para:
  - IDs historicos dos tres testes;
  - `story_response`;
  - ausencia de `temperature` em geracao;
  - prompt-ancora historico dos tres testes;
  - `caracteristica_neutra` no Teste 1;
  - `custom_id` da classificacao sem prefixo;
  - schema portugues `classificacao_genero` com `gênero` e `explicação`.

Risco remanescente:

- ainda falta um smoke real com chave para confirmar que a API aceita todos os `custom_id` historicos com acentos/espacos e que o download real tem a mesma forma que a simulacao.

## 9. Decisoes

| Data | Decisao | Motivo |
|------|---------|--------|
| 2026-04-11 | Criar plano vivo para o notebook replicavel. | Pedido do Otavio; plano antigo separado nao foi encontrado no repo local. |
| 2026-04-11 | Separar replicacao analitica de regeneracao via API. | Peer reviewers precisam de caminho sem custo/API; pesquisadores precisam de caminho modificavel. |
| 2026-04-11 | Notebook novo sera em ingles. | Melhor para peer review. |
| 2026-04-11 | Notebook sera unico, com secoes claramente separadas. | Mantem uma narrativa completa sem espalhar estado entre arquivos. |
| 2026-04-11 | Regressao no notebook usara `statsmodels`. | Mais legivel para revisao academica. |
| 2026-04-11 | Classificador default sera `gpt-4o-mini`, mas configuravel. | Preserva desenho original e permite extensoes por outros pesquisadores. |
| 2026-04-11 | Primeira implementacao deve criar `analysis_only` e `dry_run` dos tres testes antes de qualquer chamada real. | Reduz risco; garante que as chamadas pequenas sejam realmente pequenas e auditaveis. |
| 2026-04-11 | Depois de submeter batch, o notebook deve fazer polling periodico ate obter resposta ou estado terminal. | Pedido do Otavio; melhora experiencia e evita checagens manuais soltas. |
| 2026-04-11 | Polling inicial sera a cada 180 segundos. | Decisao do Otavio. |
| 2026-04-11 | `smoke` nao inclui modelos legacy. | O fluxo pequeno seguira o caminho moderno de batches do notebook original; legacy fica preservado nos CSVs finais/suporte. |
| 2026-04-11 | Outputs de teste nao devem escrever em `data/raw/` nem `data/derived/`. | Evita confusao entre dados finais versionados e reruns locais. |

## 10. Registro De Rodadas

| Data | Rodada | Resultado |
|------|--------|-----------|
| 2026-04-11 | Arqueologia inicial | Nao foi encontrado plano separado; foram encontrados CSVs finais, notebook historico e script limpo. |
| 2026-04-11 | Planejamento inicial | Documento vivo criado; agentes acionados para notebook, modo teste e experiencia reviewer. |
| 2026-04-11 | Agentes de planejamento | Notebook mapeado por celulas; estrategia `dry_run`/`smoke`/`pilot` proposta; checklist reviewer consolidado. |

## 11. Proxima Rodada

Decidir com Otavio:

1. se a chave sera configurada via `OPENAI_API_KEY`;
2. se o caminho recomendado para peer reviewers sera `analysis_only` por padrao;
3. se o full rerun deve ser prometido como executavel ou documentado como opcional/caro;
4. se `pilot` deve incluir `gpt-4.1-nano-2025-04-14` ou ficar so em `gpt-4o-mini` ate o smoke estar validado.

Proxima fatia tecnica recomendada:

1. decidir default reviewer (`analysis_only` ou `dry_run`);
2. implementar uma secao de smoke real que submeta os tres batches de geracao, aguarde polling, baixe respostas, crie os tres batches de classificacao, aguarde polling, baixe respostas e grave CSVs pequenos finais;
3. testar essa secao com `OPENAI_API_KEY` e `N_REPETITIONS = 1`;
4. criar tabela completa dos desenhos experimentais para futura execucao `full_generation`;
5. decidir e registrar o tratamento da correcao manual historica da celula 128.

# Objetivos de longo prazo — revisão do paper

Plano de **como vamos trabalhar** nesta fase de revisão. Subordinado ao **plano amplo** (próxima seção), do qual não devemos divergir.

## Plano amplo (acima deste documento)

O plano amplo do paper, ao qual este documento está subordinado e do qual **não devemos divergir**, é simples:

- **Manter o conteúdo do paper como está.** Otávio: "o grande plano é só manter o conteúdo do paper, ele tá baum, estamos nos blocos de revisão."
- **Snapshot antes de editar**: gerar cópia da versão atual dos documentos como **"PDF versão histórica 11/05"** antes de aplicar qualquer edição. Marco zero antes da revisão.
- **Commits no GitHub a cada update** em qualquer arquivo dentro de [`/home/otavio/Documents/vscode/Vies_de_Genero_Paper/`](..). Inclui as pastas internas (esta de comentários, `paper/`, `analysis/`, etc.). O repositório já existe (`.git` na raiz).

## Posicionamento desta revisão no workflow maior

Ler os 18 comentários da tia é *uma única tarefa* de uma frente maior. Pipeline atual:

1. **Entender o feedback** ✓ (sessão 2026-05-11)
2. **Criar snapshot histórico** (PDF 11/05) — antes de editar
3. **Priorizar e decidir cooperativamente** o que implementar
4. **Implementar nas fontes .tex** (commit a cada bloco)
5. **Compilar e revisar visualmente o PDF**
6. **Verificar conformidade Springer**
7. **Próxima rodada com orientador**

## Contexto

- **Paper**: *Reversal and Persistence of Gender Biases in GPT Models*
- **Autores**: Otávio Oliveira Bopp, Valdemar Pinho Neto
- **Fonte canônica**: [paper/latex/main_english.tex](../paper/latex/main_english.tex) + [appendix.tex](../paper/latex/appendix.tex) + [referencias.bib](../paper/latex/referencias.bib)
- **Versão PT**: [paper/latex/main_portuguese.tex](../paper/latex/main_portuguese.tex) — **histórica**, atualização adiada
- **Journal alvo**: Public Choice (Springer) — https://link.springer.com/journal/11127/submission-guidelines
- **Paper-template**: Motoki et al. (2024), *More human than human*, Public Choice 198:3-23. **Valdemar Pinho Neto (orientador) é co-autor**. Diretiva do orientador: "arroz com feijão" para o primeiro paper, seguir essa linha sempre que razoável.
- **Origem deste plano**: Otávio é, de saída, autor que prefere liberdade de estilo ("odeio seguir receitas") — mas neste primeiro paper aceita o conservadorismo. Quando o guia ou o template Motoki ofereçam dois caminhos, escolher o mais convencional.

## Stakeholders

- **Otávio Oliveira Bopp** — autor principal, decide.
- **Valdemar Pinho Neto** — co-autor + orientador. Também co-autor do Motoki et al. (2024). Validação obrigatória dos métodos quantitativos/econométricos (a tia explicitamente não tem como avaliar essa parte).
- **Tia Marilene** — revisora externa, da família. **Calibração**: forte em escrita acadêmica, normas de forma, estrutura textual; **explicitamente fora da econometria** ("Já a parte das análises quantitativa...é q não tive como acompanhar"). Peso das sugestões dela: alto em forma, calibrado para baixo em metodologia.
- **Editores/revisores do Public Choice** (futuros, indiretos via guia de estilo).

**Tom da colaboração com a tia**: respeitoso, agradecido, família-academia — não adversarial. Otávio em 5/7: "gostei MUITO das críticas. Muito obrigado!!!". Tia em 5/7: "vc está de parabéns".

## Hierarquia de autoridade

Quando recomendações conflitarem, a ordem é:

1. **Guia de estilo do Public Choice (Springer)** — vence sempre
2. **Otávio** (autor) — escolha minha quando o guia não restringe
3. **Paper-template Motoki** — usado como referência de estilo/estrutura
4. **Sugestões da tia Marilene** — revisão acadêmica/formato

> Exemplo: tia sugeriu abstract em parágrafo único (#0); guia permite mais; eu prefiro dois → **mantenho dois**.

## Princípios do processo

- **Cooperativo**: Claude **sempre confirma antes de aplicar qualquer comentário** — mecânicos inclusos. Nada de auto-aplicação silenciosa. Claude também **opina** quando perguntado (não só executa).
- **"Não declarar pronto"**: cada implementação tem que compilar e ser verificada no PDF final antes de marcar como feita. Inclui **verificação visual** (não só "compilou sem erro"): elementos como caixas/listings já apresentaram diferença Word vs LaTeX (ver `Cuidados específicos`).
- **Sincronia PT/EN**: somente EN nesta fase. PT entra em fase posterior.
- **Calibração das sugestões da tia**: alto peso em forma/escrita; baixo peso em econometria. Aceitar formato/normalização; validar com orientador qualquer sugestão metodológica.
- **"Arroz com feijão" como default**: na dúvida entre o convencional e o criativo neste paper, vai no convencional.
- **Log obrigatório**: cada ação aplicada (e cada erro do Claude) entra em [log de ações.md](log%20de%20a%C3%A7%C3%B5es.md).

## Cuidados específicos

- **Renderização Word vs LaTeX PDF**: Otávio observou em 5/7 que algumas caixas/listings ficam visualmente melhor no Word do que no PDF gerado pelo LaTeX. Em cada compilação, conferir os elementos visuais críticos (caixas de prompt do Listing, figuras com legendas).
- **Análise quantitativa / econometria**: tia explicitamente fora; **somente o Valdemar valida**. Não aceitar sugestão da tia que mexa em substância econométrica sem checar com ele.
- **Liberdade vs convenção**: Otávio tem preferência pessoal por afastar-se de receitas, mas neste paper a regra é seguir o template Motoki sempre que razoável. **Quando aparecer o impulso de inovar, pesar antes a diretiva "arroz com feijão"**.

## Frentes de trabalho

### A. Os 18 comentários da tia (docx) + 1 do WhatsApp

Decisão de cada um vai sendo registrada no log conforme passamos.

| Bloco | Comentários | Natureza | Status |
|---|---|---|---|
| Mecânicos | ~~#0~~, ~~#29~~, ~~#30~~, ~~#34~~ | ~~#0: parágrafos abstract~~ (rejeitado, 229 palavras OK); ~~#29: capitalização~~ (Good Leadership); ~~#30/#34: acentos PT~~ (aplicados em 3 listings + lstset com literate) | ✓ feito |
| Figuras | ~~#56, #61, #62~~ | Caption antes do gráfico + "Source: created by the authors" | ✗ rejeitados (hierarquia: Springer/Motoki põe caption ABAIXO e não exige "Source") |
| Citações/siglas | ~~#3~~, #4, ~~#24~~ | ~~#3 LLM~~ + ~~#24 i.i.d.~~ aplicados + 6 outras siglas expandidas (BERT, OLS, API, RLHF, EEOC, ML) via Explore-agent sweep; #4 (Obermeyer página) pendente | parcial: 8 expansões aplicadas, #4 pendente |
| Substantivos | ~~#5~~, ~~#7~~, ~~#52~~, ~~#73~~ | ~~#5: Objetivos específicos~~ (feito, C2); ~~#7: RQ+cortar resultados~~ (rejeitado); ~~#52: "Analyses and Results"~~ (rejeitado — Motoki também usa só "Results"); ~~#73: mover resultados~~ (rejeitado, contingente em #7) | #5 ✓; #7/#52/#73 ✗ |
| ~~Quali/quanti~~ | ~~#6, #23~~ | **REJEITADO** em 2026-05-11 — Otávio esclareceu que classificar pesquisa como quali/quanti é convenção de humanas, não comum em economia/Public Choice | rejeitado |
| Domínio técnico | #42 | Nota de rodapé sobre `temperature` | pendente |
| Elogio | #12 | Nada a fazer | n/a |

### B. Tarefas vindas da conversa do WhatsApp

- **B1. Adicionar discussão explícita de métodos econométricos.** Confirmada pela tia em 2026-05-11: "o importante é explicar q utilizou isso e o q é isso" (vantagens/desvantagens é plus). **O Motoki foi enviado pelo Otávio especificamente como referência para B1** (não como template geral). Localizar a passagem-modelo (Otávio sugeriu PDF p.4; a confirmar).
- **B2. Validar abstract.** Tia disse depois "Achei q o Abstract estava legal", mas o comentário #0 do docx diz para tirar quebra. Posição atual: manter dois parágrafos (guia permite). Confirmar contagem 150-250 palavras.
- **B3. Acrescentar "tipo de pesquisa"** (quali/quanti/quali-quanti) na metodologia, justificando depois. Tia confirmou no WhatsApp ("é só acrescentar mesmo o tipo de pesquisa").
- **B4. Reformular o estilo visual dos prompts no LaTeX/PDF — "problemão" segundo Otávio.** Não é checagem, é refatoração do estilo. Especificidades:
  - Remover símbolos sobrando (ex: `#` aparecendo no PDF).
  - Visual mais "fechado"/compacto.
  - Qualidade alvo: "MUITO melhor" — blocker, não polimento.
  - Afeta o Listing 19 e congêneres (provavelmente todos os prompts mostrados no paper e/ou appendix).
  - Provável necessidade de experimentar pacotes LaTeX alternativos: `lstlisting` (já em uso?), `tcolorbox`, `fancyvrb`, `minted`, ou caixa custom.
  - Validação visual obrigatória: comparar Word (que ficou bom) com PDF gerado para fechar.

### C. Conformidade com Public Choice (Springer)

Guia: https://link.springer.com/journal/11127/submission-guidelines

**Regras já confirmadas** (busca em 2026-05-11; reler antes de submissão):

- **Abstract**: 150–250 palavras. Não pode conter abreviações não definidas nem referências não especificadas. *Não há regra explícita contra múltiplos parágrafos* — Otávio decidiu manter os dois.
- **Citações**: sistema **author-date Chicago** — `(Author 1990)`. Para citação direta, formato Chicago padrão: `(Author 1990, p. 23)` ou variante (`p. X`).
- **Abreviações**: definir na primeira menção, usar consistentemente depois (vale para todo o texto e dentro do caption de figuras).
- **Figuras**: sequência **Figure Number → Figure Title → Figure Caption**. Material previamente publicado → referenciar no final do caption. **Para figuras criadas pelos autores, o Springer NÃO exige nota "Source: ..."** — isso é convenção brasileira (ABNT). → **Conflito com sugestões #56/#61/#62 da tia.**

**Pontos ainda a confirmar no guia**:

- Posição do caption (acima vs. abaixo do gráfico) — a tia disse "acima" (#56). Confirmar se Springer fixa ou aceita os dois.
- Estrutura de seções esperada (Introdução / Related literature / Empirical strategy / Results / Discussion / Conclusion?). Motoki segue essa.
- Limite de palavras do paper inteiro.
- Lista e número de palavras-chave.

### D. Fora de escopo desta revisão

- Atualizar `main_portuguese.tex` refletindo mudanças no EN. **Adiar.**
- Análise quantitativa precisa de validação do orientador (tia não tem como acompanhar).

## Itens em aberto neste plano

- Localizar o trecho exato do Motoki sobre econometria (frente B1) — Otávio sugeriu PDF p.4, mas conferir.
- Quando decidir cada comentário substantivo (A), registrar a decisão e a justificativa neste documento (não só no log).
- **Ritmo de trabalho**: em 5/7 Otávio sinalizou que queria implementar "o mais rápido possível". Hoje é 5/11 (~4 dias depois). Recombinar ritmo de retomada.
- **Princípios aplicáveis a próximos papers?** Otávio mencionou "papers, em geral, em inglês" (plural). Vale pensar se parte dos princípios deste plano vira convenção para os próximos artigos — depois, não agora.

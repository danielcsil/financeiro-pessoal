
# Release Candidate 1

## Objetivo

Esta versão representa o congelamento da arquitetura para a futura versão 1.0.

A partir deste ponto:

- não serão adicionadas novas funcionalidades ao núcleo do domínio;
- apenas correções de defeitos;
- melhorias de desempenho;
- ajustes de documentação;
- refinamentos da API pública.

## Arquitetura

O domínio passa a ser organizado em torno da API pública:

FinancialPlanner

que coordena:

- projeção do fluxo de caixa;
- análise de liquidez;
- cálculo do score financeiro;
- geração de estratégias;
- simulação;
- otimização;
- comparação de cenários;
- geração de relatórios.

## Critérios para o lançamento da v1.0

- Todos os testes executando com sucesso.
- Cobertura satisfatória dos casos críticos.
- API pública estável.
- Documentação revisada.
- Ausência de defeitos críticos conhecidos.

## Compatibilidade

A API pública definida nesta Release Candidate deve permanecer compatível com a versão 1.0.

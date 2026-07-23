# Aplicações do monorepo

Este diretório contém os adaptadores de entrega do produto. Eles dependem do
domínio em `src/`, mas não devem conter regras financeiras.

- `api/`: API HTTP em FastAPI que adapta requisições para o domínio Python.
- `web/`: interface Vue 3/Vite que consome a API.

## Executando localmente

Com as dependências da API instaladas, execute a partir da raiz:

```powershell
.\.venv\Scripts\python.exe -m uvicorn apps.api.app.main:app --reload
```

Para a interface:

```powershell
cd apps/web
npm install
npm run dev
```

O código de domínio permanece temporariamente em `src/`. Essa decisão evita
quebrar os imports existentes (`src.domain...`) durante a introdução da camada
web. Uma migração futura para `packages/core/` deve ser feita em uma alteração
dedicada, com os imports, testes e configuração de empacotamento atualizados
em conjunto.

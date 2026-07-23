
# Architecture Decision Records

## ADR-001

O domínio nunca conhecerá infraestrutura.

---

## ADR-002

Todo valor monetário será representado por Money.

---

## ADR-003

Decimal será utilizado em todas as operações financeiras.

Float é proibido no domínio.

---

## ADR-004

Excel será apenas mecanismo de persistência.

Nunca conterá regras de negócio.

---

## ADR-005

Toda regra pertence ao domínio.

Application apenas orquestra.

---

## ADR-006

Value Objects são imutáveis.

---

## ADR-007

Infrastructure depende do Domain.

Nunca o contrário.

---

## ADR-008

Repositórios serão interfaces.

Implementações concretas ficam em infrastructure.

---

## ADR-009

Todos os casos de uso serão independentes da interface.

---

## ADR-010

O sistema será preparado para múltiplas interfaces
(Colab, CLI, Desktop e Web).

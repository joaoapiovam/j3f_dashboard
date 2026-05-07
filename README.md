# J3F SPED Analyzer — Dashboard de Progresso

Dashboard público de acompanhamento do projeto de retificação automatizada de obrigações acessórias EFD ICMS/IPI no **J3F SPED Analyzer**, ferramenta proprietária da [J3F Consultoria Tributária](https://j3f.com.br).

## Acesso ao dashboard

[**Ver dashboard ao vivo**](https://joaoapiovam.github.io/j3f_dashboard/)


## Sobre o projeto

O J3F SPED Analyzer é um sistema interno da J3F Consultoria Tributária para revisão fiscal automatizada de arquivos SPED (EFD Contribuições, EFD ICMS/IPI, ECF, ECD, eSocial, EFD-Reinf, NF-e XML, CT-e, DCTF, DARF, PER/DCOMP, GIA-SP). Combina parsers em Polars/DuckDB com interpretação jurídica via inteligência artificial e fundamentação normativa rastreável em mais de 250 normas indexadas.

Este dashboard acompanha a evolução incremental do **motor de retificação para EFD ICMS/IPI**, distribuída em famílias de correção:

- **Família E (estrutural)** — marcação de retificadora, recálculo de Bloco 9 e contadores
- **Família M-ICMS** — CST, CFOP, ICMS-ST, DIFAL com modo experimental
- **Família CIAP** — crédito do ativo permanente, parcela 1/48
- **Família IPI** — CST IPI, alíquota, base de cálculo, crédito de entrada

## Estrutura

- `index.html` — dashboard autocontido (HTML + CSS + JavaScript vanilla)
- Sem dependências externas além de Google Fonts (família Manrope)

## Como atualizar

O conteúdo do dashboard é editado diretamente no `index.html`, em duas seções principais:

1. **Array `sprints` no JavaScript** (final do arquivo): atualiza status, posição e duração de cada sprint na linha do tempo
2. **Cards e seções HTML**: atualiza KPIs, riscos ativos, próximos marcos, decisões e histórico

Após editar, basta fazer commit no branch `main` — o GitHub Pages republica automaticamente em 1-2 minutos.

## Identidade visual

O dashboard segue o **Brand Kit J3F 2026**:

- Verde escuro institucional `#005263`
- Teal de acento `#00ACCA`
- Verde claro `#96C9D7`
- Tipografia Manrope (300 a 700)
- Dark mode automático conforme preferência do sistema

## Responsável técnico

Fábio Garcia da Silva — OAB/SP 232.079
J3F Consultoria Tributária

---

*Precisão técnica. Segurança jurídica.*

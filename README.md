# J3F SPED Analyzer — Dashboard de Progresso

Dashboard público de acompanhamento do projeto de retificação automatizada de obrigações acessórias EFD ICMS/IPI no **J3F SPED Analyzer**, ferramenta proprietária da [J3F Consultoria Tributária](https://j3f.com.br).

## Acesso ao dashboard

[**Ver dashboard ao vivo →**](https://joaoapiovam.github.io/j3f_dashboard/)

## Sobre o projeto

O J3F SPED Analyzer é um sistema interno da J3F Consultoria Tributária para revisão fiscal automatizada de arquivos SPED (EFD Contribuições, EFD ICMS/IPI, ECF, ECD, eSocial, EFD-Reinf, NF-e XML, CT-e, DCTF, DARF, PER/DCOMP, GIA-SP). Combina parsers em Polars/DuckDB com interpretação jurídica via inteligência artificial e fundamentação normativa rastreável em mais de 250 normas indexadas.

Este dashboard acompanha a evolução incremental do **motor de retificação para EFD ICMS/IPI**, distribuída em famílias de correção:

- **Família E (estrutural)** — marcação de retificadora, recálculo de Bloco 9 e contadores
- **Família M-ICMS** — CST, CFOP, ICMS-ST, DIFAL com modo experimental
- **Família CIAP** — crédito do ativo permanente, parcela 1/48
- **Família IPI** — CST IPI, alíquota, base de cálculo, crédito de entrada

## Estrutura

```
.
├── index.html              # Dashboard autocontido (HTML + CSS + JS vanilla)
├── README.md               # Este arquivo
├── LICENSE                 # MIT
├── .nojekyll               # Garante que o GitHub Pages sirva todos os arquivos
└── assets/
    ├── hero.png            # Hero institucional (Structural Resonance, 1280×400)
    ├── logo-j3f.png        # Logo oficial J3F Tax Intelligence
    ├── favicon.png         # Favicon 32×32 derivado do símbolo
    ├── favicon-64.png      # Favicon 64×64
    ├── favicon-180.png     # Apple touch icon 180×180
    └── _generators/
        └── build_hero.py   # Script Python que gera o hero.png
```

Sem dependências externas além de Google Fonts (família Manrope).

## Como atualizar

Quando o sprint avançar, mexa apenas nestas seções do `index.html`:

| Sprint avançou | O que atualizar |
|---|---|
| Data da última atualização | `<strong id="last-update">DD/MM/AAAA</strong>` no header |
| Sprint atual mudou | `<strong id="current-sprint">…</strong>` + status do `sprints[]` no JS no final do arquivo |
| Branch ativa mudou | `<strong>branch</strong>` no header e no footer |
| KPI de progresso | `<div class="kpi-value">XX%</div>` na seção "Visão executiva" |
| Riscos surgiram/foram resolvidos | Cards na seção "Riscos ativos" |
| Sprint concluído | Adicionar `<details>` em "Sprints concluídos" + atualizar status no `sprints[]` |
| Lição aprendida | Adicionar `<details>` em "Lições recentes capturadas" |
| Marcos próximos mudaram | Atualizar `<div class="milestone-item">` em "Próximos marcos" |

Após editar:

```bash
cd j3f-dashboard
git add index.html
git commit -m "docs(dashboard): atualiza progresso sprint <X>"
git push
```

GitHub Pages republica automaticamente em 1-2 minutos. URL do dashboard:
**https://joaoapiovam.github.io/j3f_dashboard/**

## Como regenerar o hero

O hero (`assets/hero.png`) é gerado proceduralmente por um script Python. Para regenerar (ex: ajustar paleta, densidade ou amplitude da senóide):

```bash
python assets/_generators/build_hero.py
```

Requer Python 3.x + Pillow (`pip install pillow`). A filosofia de design por trás do hero — **Structural Resonance** — está documentada no repositório principal do J3F SPED Analyzer em `docs/superpowers/specs/2026-05-07-hero-design-philosophy.md`.

## Identidade visual

O dashboard segue o **Brand Kit J3F 2026** (designer: Lucas Barreira / LB7, v2026.1):

| Token | Hex | Papel |
|---|---|---|
| Verde escuro | `#005263` | Fundo institucional, header |
| Teal | `#00ACCA` | Acento primário, CTAs, links |
| Verde claro | `#96C9D7` | Variação suave, badges |
| Cobre | `#9E947E` | Acento neutro quente, grid |
| Bege claro | `#EEE7D7` | Fundo de documentos |

- **Tipografia única:** Manrope (300 a 800)
- **Espaçamento base:** 8px
- **Dark mode** automático conforme preferência do sistema (`prefers-color-scheme`)
- **Animações** respeitam `prefers-reduced-motion`
- **Print** otimizado (sem hover, sem animação, hero invisível)

## Responsável técnico

Fábio Garcia da Silva — OAB/SP 232.079
J3F Consultoria Tributária

---

*Precisão técnica. Segurança jurídica.*

# Testovací scénář: Test dokumentace

## Cíl testu
Otestovat schopnost systému generovat kompletní a srozumitelnou dokumentaci. Tento test ověří, zda docs-writer agent dokáže efektivně vytvořit různé typy dokumentace pro existující aplikaci.

## Počáteční instrukce pro orchestrátora
```
Vytvoř kompletní dokumentaci pro následující existující aplikaci:

Aplikace "TaskMaster" je systém pro správu úkolů s následujícími funkcemi:
1. Vytváření, úprava a mazání úkolů
2. Organizace úkolů do projektů a kategorií
3. Přiřazování úkolů uživatelům
4. Sledování stavu a průběhu úkolů
5. Nastavování termínů a priorit
6. Notifikace o blížících se termínech
7. Generování reportů a statistik

Aplikace je implementována jako webová aplikace s architekturou klient-server:
- Frontend: React.js s TypeScript
- Backend: Node.js s Express a TypeScript
- Databáze: PostgreSQL
- API: RESTful API s autentizací pomocí JWT

Vytvoř následující typy dokumentace:
1. Uživatelská příručka
2. Vývojářská dokumentace
3. API dokumentace
4. Instalační a konfigurační příručka
5. Dokumentace architektury
6. Dokumentace databázového schématu

Dokumentace by měla být kompletní, srozumitelná a dobře strukturovaná. Používej diagramy, příklady a vysvětlení, kde je to vhodné.
```

## Očekávané výstupy

### Soubory
- `.project-memory/project_meta/project_overview.md`: Přehled projektu s popisem aplikace
- `.project-memory/documentation/`: Adresář obsahující všechny typy dokumentace
- `docs/user_guide/`: Adresář obsahující uživatelskou příručku
- `docs/developer_guide/`: Adresář obsahující vývojářskou dokumentaci
- `docs/api_docs/`: Adresář obsahující API dokumentaci
- `docs/installation_guide/`: Adresář obsahující instalační a konfigurační příručku
- `docs/architecture/`: Adresář obsahující dokumentaci architektury
- `docs/database/`: Adresář obsahující dokumentaci databázového schématu
- `README.md`: Hlavní dokumentace projektu

### Struktura projektu
```
.
├── .project-memory/
│   ├── project_meta/
│   │   ├── project_overview.md
│   │   └── ...
│   ├── documentation/
│   │   ├── documentation_plan.md
│   │   ├── user_guide_outline.md
│   │   ├── developer_guide_outline.md
│   │   ├── api_docs_outline.md
│   │   ├── installation_guide_outline.md
│   │   ├── architecture_docs_outline.md
│   │   ├── database_docs_outline.md
│   │   └── ...
│   └── ...
├── docs/
│   ├── user_guide/
│   │   ├── index.md
│   │   ├── getting_started.md
│   │   ├── tasks.md
│   │   ├── projects.md
│   │   ├── users.md
│   │   ├── reports.md
│   │   └── ...
│   ├── developer_guide/
│   │   ├── index.md
│   │   ├── setup.md
│   │   ├── code_structure.md
│   │   ├── contributing.md
│   │   ├── testing.md
│   │   └── ...
│   ├── api_docs/
│   │   ├── index.md
│   │   ├── authentication.md
│   │   ├── tasks.md
│   │   ├── projects.md
│   │   ├── users.md
│   │   └── ...
│   ├── installation_guide/
│   │   ├── index.md
│   │   ├── requirements.md
│   │   ├── installation.md
│   │   ├── configuration.md
│   │   ├── deployment.md
│   │   └── ...
│   ├── architecture/
│   │   ├── index.md
│   │   ├── overview.md
│   │   ├── frontend.md
│   │   ├── backend.md
│   │   ├── database.md
│   │   ├── diagrams/
│   │   │   ├── system_architecture.md
│   │   │   ├── component_diagram.md
│   │   │   ├── sequence_diagrams.md
│   │   │   └── ...
│   │   └── ...
│   ├── database/
│   │   ├── index.md
│   │   ├── schema.md
│   │   ├── relationships.md
│   │   ├── migrations.md
│   │   └── ...
│   └── index.md
└── README.md
```

## Kritéria úspěchu
- Všechny očekávané typy dokumentace byly vytvořeny
- Dokumentace je kompletní, srozumitelná a dobře strukturovaná
- Dokumentace obsahuje diagramy, příklady a vysvětlení, kde je to vhodné
- Uživatelská příručka pokrývá všechny funkce aplikace z pohledu uživatele
- Vývojářská dokumentace poskytuje dostatečné informace pro vývojáře
- API dokumentace popisuje všechny endpointy, parametry a odpovědi
- Instalační a konfigurační příručka obsahuje všechny potřebné kroky
- Dokumentace architektury popisuje strukturu a komponenty aplikace
- Dokumentace databázového schématu popisuje tabulky, vztahy a indexy
- Dokumentace je konzistentní a bez rozporů

## Časový limit
90 minut

## Postup testování
1. Vytvoření git větve: `git checkout -b test/documentation`
2. Předání počáteční instrukce orchestrátorovi
3. Čekání na dokončení úkolu (max. 90 minut)
4. Kontrola vytvořených souborů a jejich obsahu
5. Analýza kvality a úplnosti dokumentace
6. Vyhodnocení testu podle kritérií úspěchu

## Poznámky k vyhodnocení
- Klíčovým aspektem tohoto testu je schopnost docs-writer agenta vytvořit kompletní a srozumitelnou dokumentaci
- Je třeba sledovat, jak docs-writer agent strukturuje dokumentaci a jak efektivně komunikuje informace
- Důležité je, aby dokumentace byla konzistentní a pokrývala všechny aspekty aplikace
- Kvalita dokumentace by měla být hodnocena z pohledu různých cílových skupin (uživatelé, vývojáři, administrátoři)

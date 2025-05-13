# Testovací scénář: Základní end-to-end test

## Cíl testu
Otestovat schopnost systému vytvořit jednoduchou aplikaci od specifikace po implementaci. Tento test ověří základní funkčnost všech agentů v Boomerang módu a jejich schopnost spolupracovat na vytvoření kompletní aplikace.

## Počáteční instrukce pro orchestrátora
```
Vytvoř jednoduchou konzolovou kalkulačku v Pythonu, která bude podporovat základní matematické operace (sčítání, odčítání, násobení, dělení). Aplikace by měla mít následující funkce:
1. Přijímat vstup od uživatele ve formátu "číslo operátor číslo" (např. "5 + 3")
2. Podporovat operace +, -, *, /
3. Ošetřit základní chybové stavy (dělení nulou, neplatný vstup)
4. Umožnit uživateli ukončit aplikaci zadáním "exit" nebo "quit"
5. Zobrazit výsledek operace a čekat na další vstup

Aplikace by měla být dobře strukturovaná, testovatelná a dokumentovaná. Vytvoř kompletní řešení včetně specifikace, architektury, implementace, testů a dokumentace.
```

## Očekávané výstupy

### Soubory
- `.project-memory/project_meta/project_overview.md`: Přehled projektu s popisem kalkulačky
- `.project-memory/lld/calculator/`: Adresář obsahující low-level design kalkulačky
- `.project-memory/testing_strategy_and_plans/`: Adresář obsahující testovací plány
- `src/calculator.py`: Implementace kalkulačky
- `src/main.py`: Hlavní soubor aplikace
- `tests/test_calculator.py`: Jednotkové testy
- `README.md`: Dokumentace projektu

### Struktura projektu
```
.
├── .project-memory/
│   ├── project_meta/
│   │   ├── project_overview.md
│   │   └── ...
│   ├── lld/
│   │   ├── calculator/
│   │   │   ├── calculator_spec.md
│   │   │   └── ...
│   │   └── ...
│   ├── testing_strategy_and_plans/
│   │   ├── calculator_test_plan.md
│   │   └── ...
│   └── ...
├── src/
│   ├── calculator.py
│   ├── main.py
│   └── ...
├── tests/
│   ├── test_calculator.py
│   └── ...
└── README.md
```

## Kritéria úspěchu
- Všechny očekávané soubory byly vytvořeny
- Aplikace je funkční a splňuje všechny požadavky
- Kód je dobře strukturovaný a následuje best practices
- Testy pokrývají všechny základní funkce a hraniční případy
- Dokumentace je kompletní a srozumitelná
- Všichni agenti (Specification Writer, Architect, Auto-Coder, TDD Tester, Documentation Writer) se podíleli na vytvoření aplikace
- Orchestrátor úspěšně koordinoval celý proces

## Časový limit
60 minut

## Postup testování
1. Vytvoření git větve: `git checkout -b test/basic-e2e`
2. Předání počáteční instrukce orchestrátorovi
3. Čekání na dokončení úkolu (max. 60 minut)
4. Kontrola vytvořených souborů a jejich obsahu
5. Spuštění aplikace a ověření její funkčnosti
6. Spuštění testů a ověření jejich úspěšnosti
7. Vyhodnocení testu podle kritérií úspěchu

## Poznámky k vyhodnocení
- Při vyhodnocování je třeba brát v úvahu, že různé implementace mohou splňovat požadavky různými způsoby
- Důležité je, aby aplikace byla funkční, dobře strukturovaná a splňovala všechny požadavky
- Názvy souborů a adresářů se mohou lišit, důležitá je jejich funkce a obsah

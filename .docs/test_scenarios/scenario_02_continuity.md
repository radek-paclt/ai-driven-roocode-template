# Testovací scénář: Test kontinuity práce

## Cíl testu
Otestovat schopnost systému pokračovat v práci po restartu orchestrátora. Tento test ověří, zda je `.project-memory` struktura dostatečně robustní a informativní, aby umožnila orchestrátorovi znovu nabýt kontext a pokračovat v práci po restartu.

## Počáteční instrukce pro orchestrátora
```
Vytvoř jednoduchý webový server v Node.js s Express, který bude poskytovat REST API pro správu seznamu úkolů (todo list). API by mělo podporovat následující operace:
1. Získání seznamu všech úkolů (GET /todos)
2. Získání detailu konkrétního úkolu (GET /todos/:id)
3. Vytvoření nového úkolu (POST /todos)
4. Aktualizace existujícího úkolu (PUT /todos/:id)
5. Smazání úkolu (DELETE /todos/:id)

Každý úkol by měl mít následující atributy:
- id (unikátní identifikátor)
- title (název úkolu)
- description (popis úkolu)
- completed (boolean indikující, zda je úkol dokončen)
- createdAt (datum a čas vytvoření)
- updatedAt (datum a čas poslední aktualizace)

Aplikace by měla ukládat data v paměti (nemusí používat databázi). Vytvoř kompletní řešení včetně specifikace, architektury, implementace, testů a dokumentace.
```

## Postup přerušení a restartu
1. Nechat orchestrátora pracovat přibližně 20-30 minut
2. Ukončit rooCode aplikaci
3. Spustit rooCode aplikaci znovu
4. Předat orchestrátorovi instrukci: "Pokračuj v práci na vytvoření REST API pro správu seznamu úkolů."

## Očekávané výstupy

### Soubory
- `.project-memory/project_meta/project_overview.md`: Přehled projektu s popisem API
- `.project-memory/lld/todo_api/`: Adresář obsahující low-level design API
- `.project-memory/testing_strategy_and_plans/`: Adresář obsahující testovací plány
- `src/server.js`: Hlavní soubor serveru
- `src/routes/todos.js`: Definice API endpointů
- `src/controllers/todoController.js`: Implementace logiky API
- `src/models/todo.js`: Definice modelu úkolu
- `tests/`: Adresář obsahující testy
- `README.md`: Dokumentace projektu
- `package.json`: Definice závislostí projektu

### Struktura projektu
```
.
├── .project-memory/
│   ├── project_meta/
│   │   ├── project_overview.md
│   │   └── ...
│   ├── lld/
│   │   ├── todo_api/
│   │   │   ├── api_spec.md
│   │   │   └── ...
│   │   └── ...
│   ├── testing_strategy_and_plans/
│   │   ├── todo_api_test_plan.md
│   │   └── ...
│   └── ...
├── src/
│   ├── server.js
│   ├── routes/
│   │   ├── todos.js
│   │   └── ...
│   ├── controllers/
│   │   ├── todoController.js
│   │   └── ...
│   ├── models/
│   │   ├── todo.js
│   │   └── ...
│   └── ...
├── tests/
│   ├── routes/
│   │   ├── todos.test.js
│   │   └── ...
│   ├── controllers/
│   │   ├── todoController.test.js
│   │   └── ...
│   └── ...
├── README.md
└── package.json
```

## Kritéria úspěchu
- Orchestrátor byl schopen pokračovat v práci po restartu
- Orchestrátor správně pochopil kontext projektu z `.project-memory`
- Všechny očekávané soubory byly vytvořeny
- Aplikace je funkční a splňuje všechny požadavky
- Kód je dobře strukturovaný a následuje best practices
- Testy pokrývají všechny základní funkce a hraniční případy
- Dokumentace je kompletní a srozumitelná
- Nedošlo k duplicitní práci nebo ztrátě kontextu po restartu

## Časový limit
90 minut celkem (včetně času před a po restartu)

## Postup testování
1. Vytvoření git větve: `git checkout -b test/continuity`
2. Předání počáteční instrukce orchestrátorovi
3. Čekání přibližně 20-30 minut
4. Ukončení rooCode aplikace
5. Spuštění rooCode aplikace znovu
6. Předání instrukce pro pokračování
7. Čekání na dokončení úkolu (zbývající čas do limitu 90 minut)
8. Kontrola vytvořených souborů a jejich obsahu
9. Spuštění aplikace a ověření její funkčnosti
10. Spuštění testů a ověření jejich úspěšnosti
11. Vyhodnocení testu podle kritérií úspěchu

## Poznámky k vyhodnocení
- Klíčovým aspektem tohoto testu je schopnost orchestrátora pokračovat v práci po restartu
- Je třeba sledovat, zda orchestrátor správně pochopil kontext projektu a pokračoval v práci bez zbytečného opakování již dokončených úkolů
- Důležité je také sledovat, jak orchestrátor komunikuje s ostatními agenty po restartu

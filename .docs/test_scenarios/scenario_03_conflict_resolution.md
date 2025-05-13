# Testovací scénář: Test řešení konfliktů

## Cíl testu
Otestovat schopnost systému řešit konflikty mezi agenty. Tento test ověří, zda orchestrátor a mediátor dokáží efektivně řešit situace, kdy dochází k nesouladu mezi požadavky nebo návrhy různých agentů.

## Počáteční instrukce pro orchestrátora
```
Vytvoř jednoduchou webovou aplikaci pro správu osobních financí s následujícími požadavky:

1. Aplikace musí být implementována v Pythonu s využitím frameworku Flask
2. Aplikace musí být zároveň implementována v JavaScriptu s využitím frameworku React
3. Aplikace musí ukládat data v SQL databázi
4. Aplikace musí ukládat data v NoSQL databázi (MongoDB)
5. Aplikace musí být maximálně bezpečná a odolná proti útokům
6. Aplikace musí být co nejjednodušší na implementaci a údržbu
7. Aplikace musí mít minimalistické uživatelské rozhraní
8. Aplikace musí mít bohaté uživatelské rozhraní s mnoha vizualizacemi

Aplikace by měla umožňovat uživatelům:
- Přidávat příjmy a výdaje
- Kategorizovat transakce
- Zobrazovat přehledy a statistiky
- Nastavovat rozpočty
- Exportovat data

Vytvoř kompletní řešení včetně specifikace, architektury, implementace, testů a dokumentace.
```

## Očekávané výstupy

### Soubory
- `.project-memory/project_meta/project_overview.md`: Přehled projektu s popisem aplikace
- `.project-memory/project_meta/conflict_resolution_log.md`: Záznam o řešení konfliktů
- `.project-memory/lld/finance_app/`: Adresář obsahující low-level design aplikace
- `.project-memory/testing_strategy_and_plans/`: Adresář obsahující testovací plány
- Implementační soubory podle zvoleného řešení
- Testy podle zvoleného řešení
- `README.md`: Dokumentace projektu

### Struktura projektu
Struktura projektu bude záviset na zvoleném řešení konfliktů, ale měla by obsahovat:
- `.project-memory/` adresář s kompletní dokumentací a záznamy o řešení konfliktů
- Implementační soubory podle zvoleného řešení
- Testy podle zvoleného řešení
- Dokumentaci

## Kritéria úspěchu
- Orchestrátor identifikoval konflikty v požadavcích
- Mediátor byl zapojen do řešení konfliktů
- Konflikty byly vyřešeny logickým a odůvodněným způsobem
- Výsledné řešení je konzistentní a realizovatelné
- V `.project-memory/project_meta/conflict_resolution_log.md` je zdokumentován proces řešení konfliktů
- Aplikace je funkční a splňuje požadavky podle zvoleného řešení
- Kód je dobře strukturovaný a následuje best practices
- Testy pokrývají všechny základní funkce a hraniční případy
- Dokumentace je kompletní a srozumitelná

## Časový limit
90 minut

## Postup testování
1. Vytvoření git větve: `git checkout -b test/conflict-resolution`
2. Předání počáteční instrukce orchestrátorovi
3. Čekání na dokončení úkolu (max. 90 minut)
4. Kontrola vytvořených souborů a jejich obsahu
5. Analýza záznamu o řešení konfliktů
6. Ověření funkčnosti aplikace podle zvoleného řešení
7. Vyhodnocení testu podle kritérií úspěchu

## Poznámky k vyhodnocení
- Klíčovým aspektem tohoto testu je proces řešení konfliktů, nikoliv konkrétní technické řešení
- Je třeba sledovat, jak orchestrátor a mediátor komunikují a spolupracují na řešení konfliktů
- Důležité je, aby výsledné řešení bylo logické, odůvodněné a konzistentní
- Záznam o řešení konfliktů by měl obsahovat jasné zdůvodnění přijatých rozhodnutí

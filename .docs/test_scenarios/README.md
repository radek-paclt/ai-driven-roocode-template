# Testování rooCode Boomerang Mode

Tento adresář obsahuje testovací scénáře pro ověření funkčnosti rooCode Boomerang Mode. Každý scénář je navržen tak, aby testoval specifický aspekt systému a měl jasně definované očekávané výstupy a kritéria úspěchu.

## Proces testování

### 1. Příprava testu
- Vytvoření git větve pro testovací scénář
- Příprava počátečního stavu projektu (pokud je potřeba)

### 2. Provedení testu
- Spuštění rooCode aplikace
- Předání počáteční instrukce orchestrátorovi
- Čekání na dokončení úkolu nebo vypršení časového limitu

### 3. Vyhodnocení testu
- Kontrola vytvořených souborů a jejich obsahu
- Porovnání s očekávanými výstupy
- Vyhodnocení testu podle kritérií úspěchu

### 4. Dokumentace výsledků
- Zaznamenání výsledků testu
- Případné úpravy testovacího scénáře nebo systému

## Struktura testovacího scénáře

Každý testovací scénář je uložen v samostatném markdown souboru s následující strukturou:

```markdown
# Testovací scénář: [Název scénáře]

## Cíl testu
[Popis cíle testu]

## Počáteční instrukce pro orchestrátora
```
[Přesné znění instrukce, která bude předána orchestrátorovi]
```

## Očekávané výstupy
### Soubory
- [Cesta k souboru 1]: [Popis očekávaného obsahu]
- [Cesta k souboru 2]: [Popis očekávaného obsahu]
...

### Struktura projektu
[Očekávaná struktura adresářů a souborů]

## Kritéria úspěchu
- [Kritérium 1]
- [Kritérium 2]
...

## Časový limit
[Maximální doba trvání testu]

## Postup testování
1. Vytvoření git větve: `git checkout -b test/[název-scénáře]`
2. Předání počáteční instrukce orchestrátorovi
3. Čekání na dokončení úkolu
4. Kontrola výsledků
5. Vyhodnocení testu
```

## Seznam testovacích scénářů

1. [Základní end-to-end test](./scenario_01_basic_e2e.md) - Vytvoření jednoduché aplikace od specifikace po implementaci
2. [Test kontinuity práce](./scenario_02_continuity.md) - Test schopnosti systému pokračovat v práci po restartu orchestrátora
3. [Test řešení konfliktů](./scenario_03_conflict_resolution.md) - Test schopnosti systému řešit konflikty mezi agenty
4. [Test bezpečnostní revize](./scenario_04_security_review.md) - Test schopnosti systému identifikovat a řešit bezpečnostní problémy
5. [Test dokumentace](./scenario_05_documentation.md) - Test schopnosti systému generovat kompletní dokumentaci

## Vyhodnocení výsledků

Po provedení všech testů bude vytvořena souhrnná zpráva, která bude obsahovat:
- Přehled všech provedených testů
- Výsledky jednotlivých testů (úspěch/neúspěch)
- Identifikované problémy a návrhy na jejich řešení
- Celkové hodnocení systému

Tato zpráva bude sloužit jako podklad pro další vývoj a vylepšování systému.

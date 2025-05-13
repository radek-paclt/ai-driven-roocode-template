# Todo List: Upřesnění roleDefinitions a customInstructions pro rooCode Boomerang Mode

## Úvod
Tento dokument obsahuje plán pro další iteraci implementace rooCode konfiguračních souborů, se zaměřením na detailní definice rolí a instrukce pro jednotlivé agenty v Boomerang módu. Cílem je vytvořit jasné a komplexní instrukce pro každou roli, které zajistí, že agenti budou přesně plnit své úkoly bez vlastní invence.

## Obecné úkoly

1. **Revize stávajících definic rolí**
   - [x] Analyzovat současné roleDefinitions a customInstructions v `.roomodes`
   - [x] Identifikovat oblasti, které potřebují upřesnění nebo rozšíření
   - [x] Zajistit konzistenci mezi všemi rolemi

2. **Struktura instrukcí pro každou roli**
   - [x] Vytvořit jednotnou strukturu pro instrukce všech rolí
   - [x] Zahrnout sekce: Úvod, Odpovědnosti, Workflow, Komunikační protokoly, Omezení, Use Cases
   - [x] Zajistit, aby instrukce byly dostatečně detailní, ale nepřekročily 300-400 řádků

3. **Integrace s .project-memory strukturou**
   - [x] Zajistit, že instrukce pro každou roli jasně definují, jak pracovat s `.project-memory` adresářem
   - [x] Specifikovat, které soubory a adresáře každá role čte a upravuje
   - [x] Definovat formát a strukturu dokumentů, které role vytváří
   - [x] Navrhnout optimalizovanou strukturu `.project-memory` pro efektivní předávání kontextu mezi agenty
   - [x] Definovat standardy pro metadata dokumentů, která usnadní rychlé znovunabytí kontextu
   - [x] Vytvořit protokoly pro udržování aktuálních sumarizací a stavových informací v `.project-memory`

## Specifické úkoly pro jednotlivé role

### 1. SPARC Orchestrator (`orchestrator`)
- [x] Rozšířit instrukce pro správu Git verzování `.project-memory` adresáře
- [x] Detailně popsat proces delegace úkolů pomocí `new_task`
- [x] Definovat protokoly pro řešení konfliktů mezi agenty
- [x] Vytvořit podrobné instrukce pro facilitaci komunikace mezi BV a ostatními agenty
- [x] Přidat use cases pro typické scénáře orchestrace
- [x] Specifikovat proces monitorování a reportování stavu projektu
- [x] Implementovat mechanismy pro detekci a řešení zacyklení a opakování chyb
- [x] Vytvořit protokoly pro pravidelnou sumarizaci proběhlé práce pro efektivní využití kontextového okna
- [x] Definovat strategie pro kontinuitu práce při recyklaci Orchestratora (restart z důvodu přeplnění kontextového okna)
- [x] Navrhnout strukturu `.project-memory`, která umožní rychlé znovunabytí kontextu při restartu

### 2. Specification Writer (`spec-pseudocode`)
- [x] Detailně popsat proces transformace business požadavků na specifikace
- [x] Definovat strukturu a formát specifikačních dokumentů
- [x] Vytvořit instrukce pro tvorbu pseudokódu
- [x] Specifikovat spolupráci s Architect a TDD agentem
- [x] Přidat use cases pro různé typy specifikací (backend, frontend, API, atd.)
- [x] Definovat kritéria kvality pro specifikace

### 3. Architect (`architect`)
- [x] Rozšířit instrukce pro návrh systémové architektury
- [x] Definovat proces vytváření HLD a LLD dokumentů
- [x] Specifikovat formát a obsah architektonických diagramů
- [x] Detailně popsat proces komunikace a vysvětlování návrhů BV
- [x] Přidat use cases pro různé typy architektonických rozhodnutí
- [x] Definovat kritéria pro hodnocení kvality architektury

### 4. Auto-Coder (`code`)
- [x] Detailně popsat proces implementace kódu na základě specifikací a testů
- [x] Definovat standardy pro kvalitu kódu (čistota, modularita, atd.)
- [x] Specifikovat proces refaktoringu a optimalizace
- [x] Vytvořit instrukce pro dokumentaci kódu
- [x] Přidat use cases pro implementaci různých typů komponent
- [x] Definovat proces integrace s existujícím kódem

### 5. Tester (TDD) (`tdd`)
- [x] Rozšířit instrukce pro tvorbu testů před implementací
- [x] Definovat různé typy testů a kdy je použít
- [x] Specifikovat formát a strukturu testovacích plánů
- [x] Detailně popsat spolupráci s Auto-Coder agentem
- [x] Přidat use cases pro testování různých typů funkcionalit
- [x] Definovat kritéria pro pokrytí testy

### 6. Documentation Writer (`docs-writer`)
- [x] Detailně popsat proces generování finální dokumentace
- [x] Definovat strukturu a formát dokumentace pro různé cílové skupiny
- [x] Specifikovat proces extrakce informací z `.project-memory` a kódu
- [x] Vytvořit instrukce pro údržbu dokumentace
- [x] Přidat use cases pro různé typy dokumentace
- [x] Definovat kritéria kvality dokumentace

### 7. Security Reviewer (`security-review`)
- [x] Rozšířit instrukce pro provádění bezpečnostních auditů
- [x] Definovat proces identifikace a klasifikace bezpečnostních rizik
- [x] Specifikovat formát bezpečnostních reportů
- [x] Detailně popsat spolupráci s Auto-Coder agentem při opravách
- [x] Přidat use cases pro audit různých typů komponent
- [x] Definovat kritéria pro bezpečnostní standardy

### 8. Mediator Agent (`mediator`)
- [x] Detailně popsat proces mediace konfliktů mezi agenty
- [x] Definovat typy konfliktů a strategie jejich řešení
- [x] Specifikovat formát mediačních reportů
- [x] Vytvořit instrukce pro eskalaci neřešitelných konfliktů
- [x] Přidat use cases pro různé typy konfliktních situací
- [x] Definovat kritéria úspěšné mediace

## Implementační plán

1. **Fáze 1: Analýza a příprava**
   - [x] Revize stávajících definic rolí
   - [x] Vytvoření šablony pro instrukce
   - [x] Definování standardů a konvencí

2. **Fáze 2: Vytvoření detailních instrukcí**
   - [x] Vypracování instrukcí pro každou roli podle šablony
   - [x] Zajištění konzistence mezi rolemi
   - [x] Kontrola úplnosti a detailnosti

3. **Fáze 3: Integrace a testování**
   - [x] Integrace instrukcí do konfiguračních souborů
     - [x] Aktualizace `.roomodes` souboru
     - [x] Vytvoření/aktualizace pravidel pro Orchestratora
     - [x] Vytvoření/aktualizace pravidel pro ostatní role
       - [x] Specification Writer
       - [x] Architect
       - [x] Auto-Coder
       - [x] TDD Tester
       - [x] Documentation Writer
       - [x] Security Reviewer
       - [x] Mediator Agent
     - [x] Aktualizace globálních pravidel
   - [x] Aktualizace README souboru v rootu projektu
   - [x] Vytvoření struktury pro testování
     - [x] Vytvoření adresáře `.docs/test_scenarios/`
     - [x] Vytvoření README souboru pro testovací scénáře
     - [x] Definování procesu testování
   - [x] Vytvoření testovacích scénářů
     - [x] Základní end-to-end test
     - [x] Test kontinuity práce
     - [x] Test řešení konfliktů
     - [x] Test bezpečnostní revize
     - [x] Test dokumentace
   - [ ] Provedení testů
   - [ ] Ladění a optimalizace

4. **Fáze 4: Dokumentace a finalizace**
   - [ ] Vytvoření dokumentace pro uživatele systému
   - [ ] Provedení testů a vyhodnocení výsledků
     - [ ] Provedení základního end-to-end testu
     - [ ] Provedení testu kontinuity práce
     - [ ] Provedení testu řešení konfliktů
     - [ ] Provedení testu bezpečnostní revize
     - [ ] Provedení testu dokumentace
     - [ ] Vytvoření souhrnné zprávy o výsledcích testů
   - [ ] Finální revize a schválení
   - [ ] Nasazení aktualizovaných konfiguračních souborů

## Další kroky

Po dokončení tohoto todo listu a jeho schválení budeme postupovat podle implementačního plánu a vytvářet detailní instrukce pro každou roli. Každá role bude mít svůj vlastní soubor s instrukcemi, který bude následovat jednotnou strukturu, ale bude obsahovat specifické informace relevantní pro danou roli.

## Speciální požadavky na kontinuitu práce

Klíčovým aspektem celého systému je zajištění kontinuity práce i při recyklaci agentů (zejména Orchestratora) z důvodu přeplnění kontextového okna. Proto je třeba:

1. **Optimalizace struktury `.project-memory`**
   - [x] Navrhnout strukturu, která umožňuje rychlé znovunabytí kontextu
   - [x] Implementovat hierarchické sumarizace pro efektivní navigaci v projektu
   - [x] Zajistit, aby klíčové informace byly snadno dostupné a přehledně organizované

2. **Protokoly pro sumarizaci a stavové informace**
   - [x] Definovat standardy pro pravidelné sumarizace proběhlé práce
   - [x] Vytvořit mechanismy pro sledování stavu projektu a aktuálních úkolů
   - [x] Implementovat systém checkpointů pro snadné navázání práce

3. **Detekce a řešení zacyklení**
   - [x] Vytvořit mechanismy pro detekci opakujících se chyb a zacyklení
   - [x] Definovat protokoly pro analýzu a řešení těchto situací
   - [x] Implementovat strategie pro předcházení zacyklení

Tyto speciální požadavky musí být zohledněny v instrukcích pro všechny role, ale primární odpovědnost za jejich implementaci bude mít SPARC Orchestrator.

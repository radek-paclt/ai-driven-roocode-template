# RooCode - Iterace 001 - Todo List

## Úvod

Tento dokument obsahuje seznam úkolů pro první iteraci vylepšení RooCode na základě výsledků základního end-to-end testu. Hlavním cílem této iterace je vyřešit identifikované problémy a implementovat novou architekturu s rolí EpicCoordinator pro lepší správu kontextového okna.

## Identifikované problémy z testu

- [x] Orchestrátor má příliš velké kontextové okno
- [x] Auto-coder nevracel výsledek zpět orchestrátorovi
- [x] Tester nevracel výsledek subtasku zpět orchestrátorovi
- [x] Code si sám nekontroluje command line
- [x] Sumarizace v průběhu mění kontextové okno
- [x] Tester by měl předávat řízení zpět orchestrátorovi s výsledky testů
- [x] Chybí správný .gitignore
- [x] Některé soubory nejsou přidány do gitu

## Architektonické změny

### 1. Vytvoření nové role EpicCoordinator

- [ ] Vytvořit `.docs/role_instructions_epic-coordinator.md` s instrukcemi pro tuto roli
  - [ ] Definovat odpovědnosti EpicCoordinatora
  - [ ] Popsat workflow a procesy
  - [ ] Definovat spolupráci s ostatními rolemi
  - [ ] Popsat práci s `.project-memory`
  - [ ] Definovat omezení a hranice
  - [ ] Přidat use cases

- [ ] Aktualizovat `.roomodes` o novou roli
  - [ ] Přidat definici role
  - [ ] Nastavit správná oprávnění
  - [ ] Přidat custom instrukce

- [ ] Vytvořit `.roo/rules-epic-coordinator/` adresář s pravidly pro tuto roli
  - [ ] Vytvořit `01-epic-coordinator-responsibilities.md`
  - [ ] Vytvořit `02-epic-management.md`
  - [ ] Vytvořit `03-orchestrator-delegation.md`

### 2. Úprava role Orchestrátora

- [ ] Aktualizovat `.docs/role_instructions_orchestrator.md`
  - [ ] Přidat informace o spolupráci s EpicCoordinatorem
  - [ ] Omezit odpovědnosti orchestrátora pouze na jeden epic
  - [ ] Aktualizovat workflow a procesy

- [ ] Upravit `.roo/rules-orchestrator/`
  - [ ] Aktualizovat `01-orchestrator-responsibilities.md`
  - [ ] Upravit `03-task-delegation-protocols.md`
  - [ ] Aktualizovat `04-context-management-and-continuity.md`

### 3. Definice komunikačních protokolů

- [ ] Aktualizovat `.roo/rules/03-communication-protocols.md`
  - [ ] Přidat protokoly pro komunikaci mezi EpicCoordinatorem a Orchestrátorem
  - [ ] Rozšířit protokol `attempt_completion` pro lepší předávání výsledků
  - [ ] Přidat příklady správného použití protokolů

## Vylepšení komunikace mezi agenty

### 1. Úprava instrukcí pro Auto-Codera

- [ ] Aktualizovat `.docs/role_instructions_code.md`
  - [ ] Zdůraznit nutnost vracení výsledků orchestrátorovi
  - [ ] Přidat sekci o kontrole command line argumentů
  - [ ] Aktualizovat příklady použití protokolu `attempt_completion`

- [ ] Upravit `.roo/rules-code/`
  - [ ] Aktualizovat `01-auto-coder-guidelines.md`
  - [ ] Přidat příklady správného použití protokolu `attempt_completion`
  - [ ] Přidat sekci o kontrole command line argumentů

### 2. Úprava instrukcí pro Testera

- [ ] Aktualizovat `.docs/role_instructions_tdd.md`
  - [ ] Zdůraznit nutnost vracení výsledků testů orchestrátorovi
  - [ ] Přidat sekci o předávání výsledků testů
  - [ ] Aktualizovat příklady použití protokolu `attempt_completion`

- [ ] Upravit `.roo/rules-tdd/`
  - [ ] Aktualizovat `01-tdd-guidelines.md`
  - [ ] Přidat příklady správného použití protokolu `attempt_completion`
  - [ ] Přidat sekci o předávání výsledků testů

## Technické vylepšení

### 1. Správa gitu

- [ ] Vytvořit standardní `.gitignore`
  - [ ] Přidat běžné vzory pro různé typy projektů
  - [ ] Přidat specifické vzory pro RooCode

- [ ] Aktualizovat instrukce pro správu gitu
  - [ ] Přidat do role orchestrátora nebo EpicCoordinatora
  - [ ] Zajistit používání `git add .` místo selektivního přidávání souborů
  - [ ] Implementovat pravidelnou kontrolu nepřidaných souborů

### 2. Sumarizace a kontextové okno

- [ ] Upravit proces sumarizace
  - [ ] Implementovat inkrementální sumarizaci místo kompletní
  - [ ] Ukládat sumarizace do samostatných souborů v `.project-memory/project_context/summaries/`
  - [ ] Aktualizovat instrukce pro orchestrátora ohledně sumarizace

## Dokumentace a příklady

- [ ] Aktualizovat dokumentaci pro všechny role
  - [ ] Přidat informace o nové architektuře
  - [ ] Aktualizovat workflow a procesy
  - [ ] Přidat příklady správného použití protokolů

- [ ] Vytvořit vzorové workflow pro různé scénáře
  - [ ] Workflow pro vytvoření nového projektu
  - [ ] Workflow pro implementaci nové funkcionality
  - [ ] Workflow pro opravy chyb
  - [ ] Workflow pro testování

## Testování změn

- [ ] Vytvořit testovací scénář pro ověření změn
  - [ ] Definovat cíl testu
  - [ ] Připravit počáteční instrukce pro EpicCoordinatora
  - [ ] Definovat očekávané výstupy
  - [ ] Stanovit kritéria úspěchu

- [ ] Provést test a vyhodnotit výsledky
  - [ ] Zaznamenat výsledky testu
  - [ ] Identifikovat případné další problémy
  - [ ] Navrhnout další vylepšení pro budoucí iterace

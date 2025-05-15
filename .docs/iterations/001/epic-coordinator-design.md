# Návrh role EpicCoordinator

## Úvod

Tento dokument popisuje návrh nové role "EpicCoordinator" (nebo "ProjectManager"), která bude nadřazená orchestrátorovi a bude zodpovědná za rozdělení projektu na epicy a recyklaci orchestrátora mezi epicy. Tím vyřešíme problém s příliš velkým kontextovým oknem orchestrátora.

## Architektura

### Hierarchie rolí

```
EpicCoordinator
    |
    +-- Orchestrátor (pro Epic 1)
    |       |
    |       +-- Specializovaní agenti (Architect, Spec-Writer, TDD, Code, atd.)
    |
    +-- Orchestrátor (pro Epic 2)
    |       |
    |       +-- Specializovaní agenti
    |
    +-- ...
```

### Odpovědnosti EpicCoordinatora

1. **Správa projektu na úrovni epiců**
   - Rozdělení projektu na epicy (větší celky práce)
   - Prioritizace epiců
   - Sledování celkového postupu projektu
   - Udržování vysokoúrovňového přehledu o projektu

2. **Správa orchestrátorů**
   - Spouštění nového orchestrátora pro každý epic pomocí `new_task`
   - Přijímání výsledků od orchestrátora po dokončení epicu
   - Recyklace orchestrátora mezi epicy
   - Zajištění kontinuity mezi epicy

3. **Správa paměti projektu**
   - Udržování vysokoúrovňového přehledu v `.project-memory/project_context/epic_tracker.md`
   - Zajištění, že důležité informace jsou zachovány mezi epicy
   - Správa checkpointů a sumarizací

4. **Komunikace s Business Vlastníkem**
   - Vysokoúrovňová komunikace o stavu projektu
   - Získávání priorit a požadavků pro epicy
   - Prezentace výsledků dokončených epiců

### Odpovědnosti Orchestrátora (upravené)

1. **Správa jednoho epicu**
   - Rozdělení epicu na menší úkoly
   - Delegování úkolů specializovaným agentům
   - Sledování postupu úkolů v rámci epicu
   - Vrácení výsledků EpicCoordinatorovi po dokončení epicu

2. **Správa paměti v rámci epicu**
   - Udržování detailních informací o úkolech v rámci epicu
   - Vytváření checkpointů a sumarizací pro epic
   - Zajištění, že všechny důležité informace jsou zachovány

## Komunikační protokoly

### EpicCoordinator -> Orchestrátor: `new_task` protokol

```json
{
  "taskId": "EPIC-001",
  "delegatedToMode": "orchestrator",
  "objective": "Implementovat základní strukturu aplikace",
  "context": "Vytváříme novou aplikaci pro správu úkolů. V tomto epicu je potřeba implementovat základní strukturu aplikace včetně databázového modelu, API a základního UI.",
  "inputs": [
    {
      "type": "document",
      "path": ".project-memory/idea_clarification/04_refined_idea_and_scope.md",
      "version": "1.0.0",
      "description": "Upřesněná myšlenka a rozsah projektu"
    },
    {
      "type": "document",
      "path": ".project-memory/hld/HLD-MAIN-001_main_architecture.md",
      "version": "1.0.0",
      "description": "Hlavní architektura aplikace"
    }
  ],
  "expectedOutputs": [
    {
      "type": "document",
      "path": ".project-memory/project_context/epic_summaries/EPIC-001_summary.md",
      "description": "Souhrn dokončeného epicu"
    },
    {
      "type": "code",
      "path": "src/",
      "description": "Implementovaný kód pro základní strukturu aplikace"
    }
  ],
  "constraintsAndRules": [
    "Zaměřit se pouze na základní strukturu aplikace",
    "Neimplementovat pokročilé funkce",
    "Zajistit, že kód je dobře testovaný"
  ],
  "acceptanceCriteria": [
    "Databázový model je implementován",
    "API je implementováno a testováno",
    "Základní UI je implementováno",
    "Všechny testy procházejí"
  ],
  "priority": "high",
  "deadlineHint": "2 dny"
}
```

### Orchestrátor -> EpicCoordinator: `attempt_completion` protokol

```json
{
  "taskId": "EPIC-001",
  "result": "completed",
  "summary": "Implementace základní struktury aplikace byla úspěšně dokončena",
  "outputArtifacts": [
    {
      "type": "document",
      "path": ".project-memory/project_context/epic_summaries/EPIC-001_summary.md",
      "version": "1.0.0",
      "description": "Souhrn dokončeného epicu"
    },
    {
      "type": "code",
      "path": "src/",
      "description": "Implementovaný kód pro základní strukturu aplikace"
    }
  ],
  "metrics": {
    "tasksCompleted": 12,
    "testsPassing": 45,
    "codeLines": 1200
  },
  "nextSteps": [
    "Implementovat pokročilé funkce",
    "Vylepšit UI",
    "Optimalizovat výkon"
  ]
}
```

## Workflow

### Inicializace projektu

1. **EpicCoordinator** vytvoří základní strukturu `.project-memory/`
2. **EpicCoordinator** zachytí počáteční myšlenku od Business Vlastníka
3. **EpicCoordinator** deleguje upřesnění architektury na **Orchestrátora** pomocí `new_task`
4. **Orchestrátor** deleguje úkoly na specializované agenty
5. **Orchestrátor** vrátí výsledky **EpicCoordinatorovi** pomocí `attempt_completion`
6. **EpicCoordinator** prezentuje výsledky Business Vlastníkovi

### Implementace epicu

1. **EpicCoordinator** rozdělí projekt na epicy
2. **EpicCoordinator** deleguje implementaci epicu na **Orchestrátora** pomocí `new_task`
3. **Orchestrátor** rozdělí epic na menší úkoly
4. **Orchestrátor** deleguje úkoly na specializované agenty
5. **Orchestrátor** sleduje postup úkolů a zajišťuje jejich dokončení
6. **Orchestrátor** vrátí výsledky **EpicCoordinatorovi** pomocí `attempt_completion`
7. **EpicCoordinator** aktualizuje stav projektu a přechází k dalšímu epicu

## Implementace v RooCode

### Nové soubory

1. `.docs/role_instructions_epic-coordinator.md` - Instrukce pro roli EpicCoordinator
2. `.roo/rules-epic-coordinator/01-epic-coordinator-responsibilities.md` - Odpovědnosti EpicCoordinatora
3. `.roo/rules-epic-coordinator/02-epic-management.md` - Správa epiců
4. `.roo/rules-epic-coordinator/03-orchestrator-delegation.md` - Delegování úkolů orchestrátorovi
5. `.project-memory/project_context/epic_tracker.md` - Sledování stavu epiců

### Úpravy existujících souborů

1. `.roomodes` - Přidání nové role EpicCoordinator
2. `.docs/role_instructions_orchestrator.md` - Úprava odpovědností orchestrátora
3. `.roo/rules-orchestrator/01-orchestrator-responsibilities.md` - Aktualizace odpovědností
4. `.roo/rules-orchestrator/03-task-delegation-protocols.md` - Úprava protokolů
5. `.roo/rules-orchestrator/04-context-management-and-continuity.md` - Úprava správy kontextu
6. `.roo/rules/03-communication-protocols.md` - Přidání nových protokolů

## Závěr

Implementace role EpicCoordinator pomůže vyřešit problém s příliš velkým kontextovým oknem orchestrátora a zlepší celkovou správu projektu. EpicCoordinator bude zodpovědný za vysokoúrovňovou správu projektu, zatímco orchestrátor se bude soustředit na implementaci jednotlivých epiců. Tím se zajistí lepší škálovatelnost a kontinuita projektu.

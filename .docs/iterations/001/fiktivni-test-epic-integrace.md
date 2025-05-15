# Fiktivní test integrace epic struktury

## Úvod

Tento dokument popisuje fiktivní scénář pro testování integrace epic struktury do současného návrhu `.project-memory`. Scénář simuluje vývoj jednoduché konzolové kalkulačky v Pythonu, rozdělený do několika epiců.

## Struktura projektu

Projekt je rozdělen do následujících epiců:

1. **EPIC-000**: Nastavení projektu a základní architektura
2. **EPIC-001**: Implementace základních matematických operací
3. **EPIC-002**: Implementace pokročilých funkcí
4. **EPIC-003**: Implementace uživatelského rozhraní

## Workflow a generované dokumenty

### 1. EpicCoordinator inicializuje projekt

**Generované dokumenty**:
- `.project-memory/idea_clarification/01_initial_idea_capture.md`
- `.project-memory/project_context/product_overview.md`
- `.project-memory/project_context/epic_tracker.md`
- `.project-memory/project_postulates.md`
- `.gitignore`

### 2. EpicCoordinator deleguje EPIC-000 orchestrátorovi

**Komunikace**:
- EpicCoordinator -> Orchestrátor: `new_task` s ID "EPIC-000"

```json
{
  "taskId": "EPIC-000",
  "delegatedToMode": "orchestrator",
  "objective": "Nastavení projektu a základní architektura",
  "context": "Vytváříme konzolovou kalkulačku v Pythonu. V tomto epicu je potřeba nastavit základní strukturu projektu a navrhnout architekturu.",
  "epicContext": {
    "epicId": "EPIC-000",
    "epicName": "Nastavení projektu a základní architektura",
    "epicStatus": "NotStarted",
    "epicProgress": "0%"
  },
  "inputs": [
    {
      "type": "document",
      "path": ".project-memory/idea_clarification/01_initial_idea_capture.md",
      "version": "1.0.0",
      "description": "Počáteční zachycení myšlenky"
    }
  ],
  "expectedOutputs": [
    {
      "type": "document",
      "path": ".project-memory/project_context/summaries/EPIC-000_summary.md",
      "description": "Souhrn dokončeného epicu"
    },
    {
      "type": "document",
      "path": ".project-memory/hld/HLD-MAIN-001_main_architecture.md",
      "description": "Hlavní architektura aplikace"
    },
    {
      "type": "code",
      "path": "src/",
      "description": "Základní struktura projektu"
    }
  ],
  "priority": "high",
  "deadlineHint": "1 den"
}
```

**Orchestrátor vytvoří strukturu pro epic**:
- `.project-memory/epics/EPIC-000/epic_state.md`
- `.project-memory/epics/EPIC-000/task_tracker.md`
- `.project-memory/epics/EPIC-000/epic_decision_log.md`
- `.project-memory/epics/EPIC-000/agent_communication_log.md`

### 3. Orchestrátor deleguje úkoly specializovaným agentům

#### Úkol pro Architect agenta

**Komunikace**:
- Orchestrátor -> Architect: `new_task` s ID "TASK-001"

```json
{
  "taskId": "TASK-001",
  "delegatedToMode": "architect",
  "objective": "Navrhnout architekturu konzolové kalkulačky",
  "context": "Vytváříme konzolovou kalkulačku v Pythonu. Potřebujeme navrhnout celkovou architekturu aplikace.",
  "inputs": [
    {
      "type": "document",
      "path": ".project-memory/idea_clarification/01_initial_idea_capture.md",
      "version": "1.0.0",
      "description": "Počáteční zachycení myšlenky"
    }
  ],
  "expectedOutputs": [
    {
      "type": "document",
      "path": ".project-memory/hld/HLD-MAIN-001_main_architecture.md",
      "description": "Hlavní architektura aplikace"
    },
    {
      "type": "document",
      "path": ".project-memory/lld/LLD-MAIN-001_component_design.md",
      "description": "Návrh komponent"
    }
  ],
  "priority": "high",
  "deadlineHint": "4 hodiny"
}
```

**Architect generuje**:
- `.project-memory/hld/HLD-MAIN-001_main_architecture.md` (Globální architektura)
- `.project-memory/lld/LLD-MAIN-001_component_design.md` (Globální komponenty)

**Architect vrací výsledek**:
- Architect -> Orchestrátor: `attempt_completion` s ID "TASK-001"

```json
{
  "taskId": "TASK-001",
  "result": "completed",
  "summary": "Architektura konzolové kalkulačky byla navržena",
  "outputArtifacts": [
    {
      "type": "document",
      "path": ".project-memory/hld/HLD-MAIN-001_main_architecture.md",
      "version": "1.0.0",
      "description": "Hlavní architektura aplikace"
    },
    {
      "type": "document",
      "path": ".project-memory/lld/LLD-MAIN-001_component_design.md",
      "version": "1.0.0",
      "description": "Návrh komponent"
    }
  ]
}
```

**Orchestrátor aktualizuje**:
- `.project-memory/epics/EPIC-000/epic_state.md`
- `.project-memory/epics/EPIC-000/task_tracker.md`
- `.project-memory/epics/EPIC-000/agent_communication_log.md`

#### Úkol pro Specification Writer agenta

**Komunikace**:
- Orchestrátor -> Spec-Writer: `new_task` s ID "TASK-002"

```json
{
  "taskId": "TASK-002",
  "delegatedToMode": "spec-pseudocode",
  "objective": "Vytvořit specifikaci konzolové kalkulačky",
  "context": "Vytváříme konzolovou kalkulačku v Pythonu. Potřebujeme vytvořit detailní specifikaci aplikace.",
  "inputs": [
    {
      "type": "document",
      "path": ".project-memory/idea_clarification/01_initial_idea_capture.md",
      "version": "1.0.0",
      "description": "Počáteční zachycení myšlenky"
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
      "path": ".project-memory/lld/specifications/SPEC-MAIN-001_calculator_specification.md",
      "description": "Specifikace kalkulačky"
    }
  ],
  "priority": "high",
  "deadlineHint": "4 hodiny"
}
```

**Specification Writer generuje**:
- `.project-memory/lld/specifications/SPEC-MAIN-001_calculator_specification.md` (Globální specifikace)

**Specification Writer vrací výsledek**:
- Spec-Writer -> Orchestrátor: `attempt_completion` s ID "TASK-002"

```json
{
  "taskId": "TASK-002",
  "result": "completed",
  "summary": "Specifikace konzolové kalkulačky byla vytvořena",
  "outputArtifacts": [
    {
      "type": "document",
      "path": ".project-memory/lld/specifications/SPEC-MAIN-001_calculator_specification.md",
      "version": "1.0.0",
      "description": "Specifikace kalkulačky"
    }
  ]
}
```

**Orchestrátor aktualizuje**:
- `.project-memory/epics/EPIC-000/epic_state.md`
- `.project-memory/epics/EPIC-000/task_tracker.md`
- `.project-memory/epics/EPIC-000/agent_communication_log.md`

#### Úkol pro Auto-Coder agenta

**Komunikace**:
- Orchestrátor -> Auto-Coder: `new_task` s ID "TASK-003"

```json
{
  "taskId": "TASK-003",
  "delegatedToMode": "code",
  "objective": "Vytvořit základní strukturu projektu",
  "context": "Vytváříme konzolovou kalkulačku v Pythonu. Potřebujeme vytvořit základní strukturu projektu.",
  "inputs": [
    {
      "type": "document",
      "path": ".project-memory/hld/HLD-MAIN-001_main_architecture.md",
      "version": "1.0.0",
      "description": "Hlavní architektura aplikace"
    },
    {
      "type": "document",
      "path": ".project-memory/lld/LLD-MAIN-001_component_design.md",
      "version": "1.0.0",
      "description": "Návrh komponent"
    }
  ],
  "expectedOutputs": [
    {
      "type": "code",
      "path": "src/calculator/__init__.py",
      "description": "Inicializační soubor balíčku"
    },
    {
      "type": "code",
      "path": "src/calculator/main.py",
      "description": "Hlavní soubor aplikace"
    },
    {
      "type": "code",
      "path": "tests/__init__.py",
      "description": "Inicializační soubor testů"
    },
    {
      "type": "code",
      "path": "setup.py",
      "description": "Instalační skript"
    },
    {
      "type": "code",
      "path": "README.md",
      "description": "Dokumentace projektu"
    }
  ],
  "priority": "high",
  "deadlineHint": "4 hodiny"
}
```

**Auto-Coder generuje**:
- `src/calculator/__init__.py`
- `src/calculator/main.py`
- `tests/__init__.py`
- `setup.py`
- `README.md`

**Auto-Coder vrací výsledek**:
- Auto-Coder -> Orchestrátor: `attempt_completion` s ID "TASK-003"

```json
{
  "taskId": "TASK-003",
  "result": "completed",
  "summary": "Základní struktura projektu byla vytvořena",
  "outputArtifacts": [
    {
      "type": "code",
      "path": "src/calculator/__init__.py",
      "description": "Inicializační soubor balíčku"
    },
    {
      "type": "code",
      "path": "src/calculator/main.py",
      "description": "Hlavní soubor aplikace"
    },
    {
      "type": "code",
      "path": "tests/__init__.py",
      "description": "Inicializační soubor testů"
    },
    {
      "type": "code",
      "path": "setup.py",
      "description": "Instalační skript"
    },
    {
      "type": "code",
      "path": "README.md",
      "description": "Dokumentace projektu"
    }
  ]
}
```

**Orchestrátor aktualizuje**:
- `.project-memory/epics/EPIC-000/epic_state.md`
- `.project-memory/epics/EPIC-000/task_tracker.md`
- `.project-memory/epics/EPIC-000/agent_communication_log.md`

### 4. Orchestrátor vytváří checkpoint a vrací výsledky EpicCoordinatorovi

**Orchestrátor generuje**:
- `.project-memory/epics/EPIC-000/checkpoints/checkpoint_final.md`
- `.project-memory/project_context/summaries/EPIC-000_summary.md`

**Orchestrátor vrací výsledek**:
- Orchestrátor -> EpicCoordinator: `attempt_completion` s ID "EPIC-000"

```json
{
  "taskId": "EPIC-000",
  "result": "completed",
  "summary": "Nastavení projektu a základní architektura byly dokončeny",
  "outputArtifacts": [
    {
      "type": "document",
      "path": ".project-memory/project_context/summaries/EPIC-000_summary.md",
      "version": "1.0.0",
      "description": "Souhrn dokončeného epicu"
    },
    {
      "type": "document",
      "path": ".project-memory/hld/HLD-MAIN-001_main_architecture.md",
      "version": "1.0.0",
      "description": "Hlavní architektura aplikace"
    },
    {
      "type": "document",
      "path": ".project-memory/lld/LLD-MAIN-001_component_design.md",
      "version": "1.0.0",
      "description": "Návrh komponent"
    },
    {
      "type": "document",
      "path": ".project-memory/lld/specifications/SPEC-MAIN-001_calculator_specification.md",
      "version": "1.0.0",
      "description": "Specifikace kalkulačky"
    },
    {
      "type": "code",
      "path": "src/calculator/__init__.py",
      "description": "Inicializační soubor balíčku"
    },
    {
      "type": "code",
      "path": "src/calculator/main.py",
      "description": "Hlavní soubor aplikace"
    },
    {
      "type": "code",
      "path": "tests/__init__.py",
      "description": "Inicializační soubor testů"
    },
    {
      "type": "code",
      "path": "setup.py",
      "description": "Instalační skript"
    },
    {
      "type": "code",
      "path": "README.md",
      "description": "Dokumentace projektu"
    }
  ],
  "metrics": {
    "tasksCompleted": 3,
    "testsPassing": 0,
    "codeLines": 100
  },
  "nextSteps": [
    "Implementovat základní matematické operace",
    "Vytvořit testy pro základní operace"
  ]
}
```

**EpicCoordinator aktualizuje**:
- `.project-memory/project_context/epic_tracker.md`

### 5. EpicCoordinator deleguje EPIC-001 novému orchestrátorovi

**Komunikace**:
- EpicCoordinator -> Orchestrátor: `new_task` s ID "EPIC-001"

```json
{
  "taskId": "EPIC-001",
  "delegatedToMode": "orchestrator",
  "objective": "Implementace základních matematických operací",
  "context": "Vytváříme konzolovou kalkulačku v Pythonu. V tomto epicu je potřeba implementovat základní matematické operace (sčítání, odčítání, násobení, dělení).",
  "epicContext": {
    "epicId": "EPIC-001",
    "epicName": "Implementace základních matematických operací",
    "epicStatus": "NotStarted",
    "epicProgress": "0%"
  },
  "inputs": [
    {
      "type": "document",
      "path": ".project-memory/project_context/summaries/EPIC-000_summary.md",
      "version": "1.0.0",
      "description": "Souhrn předchozího epicu"
    },
    {
      "type": "document",
      "path": ".project-memory/hld/HLD-MAIN-001_main_architecture.md",
      "version": "1.0.0",
      "description": "Hlavní architektura aplikace"
    },
    {
      "type": "document",
      "path": ".project-memory/lld/specifications/SPEC-MAIN-001_calculator_specification.md",
      "version": "1.0.0",
      "description": "Specifikace kalkulačky"
    }
  ],
  "expectedOutputs": [
    {
      "type": "document",
      "path": ".project-memory/project_context/summaries/EPIC-001_summary.md",
      "description": "Souhrn dokončeného epicu"
    },
    {
      "type": "code",
      "path": "src/calculator/operations.py",
      "description": "Implementace základních operací"
    },
    {
      "type": "code",
      "path": "tests/test_basic_operations.py",
      "description": "Testy pro základní operace"
    }
  ],
  "priority": "high",
  "deadlineHint": "1 den"
}
```

**Nový orchestrátor vytvoří strukturu pro epic**:
- `.project-memory/epics/EPIC-001/epic_state.md`
- `.project-memory/epics/EPIC-001/task_tracker.md`
- `.project-memory/epics/EPIC-001/epic_decision_log.md`
- `.project-memory/epics/EPIC-001/agent_communication_log.md`

### 6. Nový orchestrátor deleguje úkoly pro EPIC-001

#### Úkol pro Specification Writer agenta

**Komunikace**:
- Orchestrátor -> Spec-Writer: `new_task` s ID "TASK-101"

```json
{
  "taskId": "TASK-101",
  "delegatedToMode": "spec-pseudocode",
  "objective": "Vytvořit specifikaci základních matematických operací",
  "context": "Vytváříme konzolovou kalkulačku v Pythonu. Potřebujeme vytvořit detailní specifikaci základních matematických operací.",
  "inputs": [
    {
      "type": "document",
      "path": ".project-memory/lld/specifications/SPEC-MAIN-001_calculator_specification.md",
      "version": "1.0.0",
      "description": "Specifikace kalkulačky"
    }
  ],
  "expectedOutputs": [
    {
      "type": "document",
      "path": ".project-memory/epics/EPIC-001/epic_lld/SPEC-EPIC001-001_basic_operations.md",
      "description": "Specifikace základních operací"
    }
  ],
  "priority": "high",
  "deadlineHint": "2 hodiny"
}
```

**Specification Writer generuje**:
- `.project-memory/epics/EPIC-001/epic_lld/SPEC-EPIC001-001_basic_operations.md` (Epic-specifická specifikace)

**Specification Writer vrací výsledek**:
- Spec-Writer -> Orchestrátor: `attempt_completion` s ID "TASK-101"

```json
{
  "taskId": "TASK-101",
  "result": "completed",
  "summary": "Specifikace základních matematických operací byla vytvořena",
  "outputArtifacts": [
    {
      "type": "document",
      "path": ".project-memory/epics/EPIC-001/epic_lld/SPEC-EPIC001-001_basic_operations.md",
      "version": "1.0.0",
      "description": "Specifikace základních operací"
    }
  ]
}
```

#### Úkol pro TDD agenta

**Komunikace**:
- Orchestrátor -> TDD: `new_task` s ID "TASK-102"

```json
{
  "taskId": "TASK-102",
  "delegatedToMode": "tdd",
  "objective": "Vytvořit testy pro základní matematické operace",
  "context": "Vytváříme konzolovou kalkulačku v Pythonu. Potřebujeme vytvořit testy pro základní matematické operace.",
  "inputs": [
    {
      "type": "document",
      "path": ".project-memory/epics/EPIC-001/epic_lld/SPEC-EPIC001-001_basic_operations.md",
      "version": "1.0.0",
      "description": "Specifikace základních operací"
    }
  ],
  "expectedOutputs": [
    {
      "type": "code",
      "path": "tests/test_basic_operations.py",
      "description": "Testy pro základní operace"
    },
    {
      "type": "document",
      "path": ".project-memory/epics/EPIC-001/epic_lld/TEST-EPIC001-001_basic_operations_tests.md",
      "description": "Testovací plán pro základní operace"
    }
  ],
  "priority": "high",
  "deadlineHint": "2 hodiny"
}
```

**TDD generuje**:
- `tests/test_basic_operations.py`
- `.project-memory/epics/EPIC-001/epic_lld/TEST-EPIC001-001_basic_operations_tests.md` (Epic-specifický testovací plán)

**TDD vrací výsledek**:
- TDD -> Orchestrátor: `attempt_completion` s ID "TASK-102"

```json
{
  "taskId": "TASK-102",
  "result": "completed",
  "summary": "Testy pro základní matematické operace byly vytvořeny",
  "outputArtifacts": [
    {
      "type": "code",
      "path": "tests/test_basic_operations.py",
      "description": "Testy pro základní operace"
    },
    {
      "type": "document",
      "path": ".project-memory/epics/EPIC-001/epic_lld/TEST-EPIC001-001_basic_operations_tests.md",
      "version": "1.0.0",
      "description": "Testovací plán pro základní operace"
    }
  ]
}
```

#### Úkol pro Auto-Coder agenta

**Komunikace**:
- Orchestrátor -> Auto-Coder: `new_task` s ID "TASK-103"

```json
{
  "taskId": "TASK-103",
  "delegatedToMode": "code",
  "objective": "Implementovat základní matematické operace",
  "context": "Vytváříme konzolovou kalkulačku v Pythonu. Potřebujeme implementovat základní matematické operace.",
  "inputs": [
    {
      "type": "document",
      "path": ".project-memory/epics/EPIC-001/epic_lld/SPEC-EPIC001-001_basic_operations.md",
      "version": "1.0.0",
      "description": "Specifikace základních operací"
    },
    {
      "type": "code",
      "path": "tests/test_basic_operations.py",
      "description": "Testy pro základní operace"
    }
  ],
  "expectedOutputs": [
    {
      "type": "code",
      "path": "src/calculator/operations.py",
      "description": "Implementace základních operací"
    },
    {
      "type": "document",
      "path": ".project-memory/epics/EPIC-001/epic_lld/CODE-EPIC001-001_basic_operations_implementation_notes.md",
      "description": "Implementační poznámky"
    }
  ],
  "priority": "high",
  "deadlineHint": "4 hodiny"
}
```

**Auto-Coder generuje**:
- `src/calculator/operations.py`
- `.project-memory/epics/EPIC-001/epic_lld/CODE-EPIC001-001_basic_operations_implementation_notes.md` (Epic-specifické implementační poznámky)

**Auto-Coder vrací výsledek**:
- Auto-Coder -> Orchestrátor: `attempt_completion` s ID "TASK-103"

```json
{
  "taskId": "TASK-103",
  "result": "completed",
  "summary": "Základní matematické operace byly implementovány",
  "outputArtifacts": [
    {
      "type": "code",
      "path": "src/calculator/operations.py",
      "description": "Implementace základních operací"
    },
    {
      "type": "document",
      "path": ".project-memory/epics/EPIC-001/epic_lld/CODE-EPIC001-001_basic_operations_implementation_notes.md",
      "version": "1.0.0",
      "description": "Implementační poznámky"
    }
  ],
  "testResults": {
    "total": 8,
    "passing": 8,
    "failing": 0
  }
}
```

**Orchestrátor aktualizuje po každém úkolu**:
- `.project-memory/epics/EPIC-001/epic_state.md`
- `.project-memory/epics/EPIC-001/task_tracker.md`
- `.project-memory/epics/EPIC-001/agent_communication_log.md`

### 7. Orchestrátor vytváří checkpoint a vrací výsledky EpicCoordinatorovi

**Orchestrátor generuje**:
- `.project-memory/epics/EPIC-001/checkpoints/checkpoint_final.md`
- `.project-memory/project_context/summaries/EPIC-001_summary.md`

**Orchestrátor vrací výsledek**:
- Orchestrátor -> EpicCoordinator: `attempt_completion` s ID "EPIC-001"

```json
{
  "taskId": "EPIC-001",
  "result": "completed",
  "summary": "Implementace základních matematických operací byla dokončena",
  "outputArtifacts": [
    {
      "type": "document",
      "path": ".project-memory/project_context/summaries/EPIC-001_summary.md",
      "version": "1.0.0",
      "description": "Souhrn dokončeného epicu"
    },
    {
      "type": "code",
      "path": "src/calculator/operations.py",
      "description": "Implementace základních operací"
    },
    {
      "type": "code",
      "path": "tests/test_basic_operations.py",
      "description": "Testy pro základní operace"
    }
  ],
  "metrics": {
    "tasksCompleted": 3,
    "testsPassing": 8,
    "codeLines": 150
  },
  "nextSteps": [
    "Implementovat pokročilé matematické funkce",
    "Vytvořit testy pro pokročilé funkce"
  ]
}
```

**EpicCoordinator aktualizuje**:
- `.project-memory/project_context/epic_tracker.md`

## Analýza scénáře z hlediska duplicit

V tomto scénáři jsme se zaměřili na eliminaci duplicit:

1. **Globální vs. Epic-specifické specifikace**:
   - Globální specifikace (`.project-memory/lld/specifications/SPEC-MAIN-001_calculator_specification.md`) obsahuje celkové požadavky na kalkulačku
   - Epic-specifické specifikace (`.project-memory/epics/EPIC-001/epic_lld/SPEC-EPIC001-001_basic_operations.md`) obsahují pouze detaily pro základní operace

2. **Komunikační logy**:
   - Každá komunikace je zaznamenána pouze jednou, na příslušné úrovni
   - Orchestrátor zaznamenává komunikaci s agenty v rámci epicu v `.project-memory/epics/EPIC-XXX/agent_communication_log.md`

3. **Rozhodnutí**:
   - Každé rozhodnutí je zaznamenáno pouze jednou, na příslušné úrovni
   - Globální architektonická rozhodnutí jsou v globálních dokumentech
   - Rozhodnutí specifická pro epic jsou v `.project-memory/epics/EPIC-XXX/epic_decision_log.md`

4. **Sledování úkolů**:
   - EpicCoordinator sleduje epicy jako celky v `.project-memory/project_context/epic_tracker.md`
   - Orchestrátor sleduje jednotlivé úkoly v rámci epicu v `.project-memory/epics/EPIC-XXX/task_tracker.md`

5. **Sumarizace a checkpointy**:
   - Orchestrátor vytváří checkpointy pro epic v `.project-memory/epics/EPIC-XXX/checkpoints/`
   - Po dokončení epicu vytvoří souhrn v `.project-memory/project_context/summaries/EPIC-XXX_summary.md`

## Závěr

Tento fiktivní scénář demonstruje, jak může být epic struktura integrována do současného návrhu `.project-memory` bez vytváření duplicit. Klíčem je jasné oddělení globálních a epic-specifických informací a definování jasných odpovědností pro aktualizaci dokumentů.

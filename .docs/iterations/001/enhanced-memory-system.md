# Vylepšený systém memorizace pro recyklaci orchestrátora

## Úvod

Tento dokument popisuje vylepšený systém memorizace, který zajistí, že při recyklaci orchestrátora bude mít nový orchestrátor všechny potřebné informace k efektivnímu pokračování v práci na daném epicu.

## Současné nedostatky

Současný systém memorizace má několik potenciálních nedostatků, které by mohly způsobit ztrátu kontextu při recyklaci orchestrátora:

1. **Nedostatečný detail o stavu epicu** - Chybí strukturovaný záznam o aktuálním stavu epicu
2. **Chybějící informace o rozpracovaných úkolech** - Není jasné, které úkoly jsou v průběhu a v jakém stavu
3. **Neúplná historie rozhodnutí** - Důležitá rozhodnutí a jejich zdůvodnění nemusí být explicitně zaznamenána
4. **Omezená komunikační historie** - Historie komunikace s agenty může být ztracena

## Vylepšení systému memorizace

### 1. Strukturované soubory stavu epicu

Vytvořit strukturované soubory pro každý epic, které budou obsahovat všechny potřebné informace:

```
.project-memory/
├── epics/
│   ├── EPIC-001/
│   │   ├── epic_state.md
│   │   ├── task_tracker.md
│   │   ├── decision_log.md
│   │   ├── communication_log.md
│   │   └── checkpoints/
│   │       ├── checkpoint_001.md
│   │       ├── checkpoint_002.md
│   │       └── ...
│   ├── EPIC-002/
│   │   └── ...
```

#### epic_state.md

```markdown
---
title: "Epic State: Implement Basic Application Structure"
epic_id: "EPIC-001"
version: "1.2.0"
status: "In Progress"
created_by: "EpicCoordinator"
created_date: "YYYY-MM-DDTHH:MM:SSZ"
last_modified_by: "Orchestrator"
last_modified_date: "YYYY-MM-DDTHH:MM:SSZ"
progress: "65%"
tags: ["epic", "state", "basic_structure"]
---

# Epic State: Implement Basic Application Structure

## Overview
This epic involves implementing the basic structure of the application, including database models, API endpoints, and basic UI components.

## Current Status
- **Progress**: 65%
- **Status**: In Progress
- **Last Updated**: YYYY-MM-DD HH:MM

## Completed Tasks
- [x] Define database schema
- [x] Implement database models
- [x] Create basic API endpoints
- [x] Write tests for database models

## In-Progress Tasks
- [ ] Implement authentication middleware (assigned to Auto-Coder, 50% complete)
- [ ] Create basic UI components (assigned to Auto-Coder, 30% complete)

## Pending Tasks
- [ ] Integrate API with UI
- [ ] Implement error handling
- [ ] Add validation

## Blockers and Issues
- Need clarification on authentication requirements (raised on YYYY-MM-DD)

## Recent Developments
- Database models were refactored to improve performance
- Added additional validation rules based on Business Owner feedback

## Next Steps
1. Complete authentication middleware
2. Finish UI components
3. Integrate API with UI
```

#### task_tracker.md

```markdown
---
title: "Task Tracker: Implement Basic Application Structure"
epic_id: "EPIC-001"
version: "1.3.0"
status: "Active"
created_by: "Orchestrator"
created_date: "YYYY-MM-DDTHH:MM:SSZ"
last_modified_by: "Orchestrator"
last_modified_date: "YYYY-MM-DDTHH:MM:SSZ"
tags: ["tasks", "tracker", "basic_structure"]
---

# Task Tracker: Implement Basic Application Structure

## Active Tasks

### TASK-001: Define Database Schema
- **Status**: Completed
- **Assigned To**: Architect
- **Started**: YYYY-MM-DD
- **Completed**: YYYY-MM-DD
- **Deliverables**: 
  - `.project-memory/lld/database/schema.md`
- **Notes**: Schema approved by Business Owner

### TASK-002: Implement Database Models
- **Status**: Completed
- **Assigned To**: Auto-Coder
- **Started**: YYYY-MM-DD
- **Completed**: YYYY-MM-DD
- **Deliverables**: 
  - `src/models/user.py`
  - `src/models/task.py`
  - `src/models/project.py`
- **Notes**: All tests passing

### TASK-003: Implement Authentication Middleware
- **Status**: In Progress
- **Assigned To**: Auto-Coder
- **Started**: YYYY-MM-DD
- **Expected Completion**: YYYY-MM-DD
- **Progress**: 50%
- **Current Work**: Implementing JWT validation
- **Blockers**: None
- **Notes**: Using JWT for authentication

## Planned Tasks

### TASK-004: Integrate API with UI
- **Status**: Planned
- **Assigned To**: TBD
- **Dependencies**: TASK-002, TASK-003
- **Priority**: High
- **Notes**: Will use Axios for API calls

## Completed Tasks

### TASK-000: Set Up Project Structure
- **Status**: Completed
- **Assigned To**: Orchestrator
- **Started**: YYYY-MM-DD
- **Completed**: YYYY-MM-DD
- **Deliverables**: 
  - Project directory structure
  - Initial configuration files
- **Notes**: Basic project structure set up
```

#### decision_log.md

```markdown
---
title: "Decision Log: Implement Basic Application Structure"
epic_id: "EPIC-001"
version: "1.1.0"
status: "Active"
created_by: "Orchestrator"
created_date: "YYYY-MM-DDTHH:MM:SSZ"
last_modified_by: "Orchestrator"
last_modified_date: "YYYY-MM-DDTHH:MM:SSZ"
tags: ["decisions", "log", "basic_structure"]
---

# Decision Log: Implement Basic Application Structure

## Decision 001: Database Technology
- **Date**: YYYY-MM-DD
- **Decision**: Use PostgreSQL for the database
- **Alternatives Considered**: 
  - MySQL
  - SQLite
  - MongoDB
- **Rationale**: 
  - Better support for complex queries
  - Strong data integrity
  - Good performance for expected workload
- **Implications**: 
  - Need to set up PostgreSQL in development and production
  - Need to use appropriate ORM
- **Status**: Approved by Business Owner

## Decision 002: Authentication Method
- **Date**: YYYY-MM-DD
- **Decision**: Use JWT for authentication
- **Alternatives Considered**: 
  - Session-based authentication
  - OAuth
- **Rationale**: 
  - Stateless authentication
  - Good for API-based applications
  - Easy to implement
- **Implications**: 
  - Need to implement token refresh mechanism
  - Need to secure tokens properly
- **Status**: Approved by Architect

## Decision 003: API Framework
- **Date**: YYYY-MM-DD
- **Decision**: Use FastAPI for the API
- **Alternatives Considered**: 
  - Flask
  - Django REST Framework
- **Rationale**: 
  - Automatic OpenAPI documentation
  - Good performance
  - Type checking with Pydantic
- **Implications**: 
  - Need to learn FastAPI specifics
  - Need to set up proper dependency injection
- **Status**: Approved by Architect
```

#### communication_log.md

```markdown
---
title: "Communication Log: Implement Basic Application Structure"
epic_id: "EPIC-001"
version: "1.4.0"
status: "Active"
created_by: "Orchestrator"
created_date: "YYYY-MM-DDTHH:MM:SSZ"
last_modified_by: "Orchestrator"
last_modified_date: "YYYY-MM-DDTHH:MM:SSZ"
tags: ["communication", "log", "basic_structure"]
---

# Communication Log: Implement Basic Application Structure

## Communication 001: Task Assignment to Architect
- **Date**: YYYY-MM-DD
- **From**: Orchestrator
- **To**: Architect
- **Subject**: Define Database Schema
- **Message**: 
  ```json
  {
    "taskId": "TASK-001",
    "delegatedToMode": "architect",
    "objective": "Define database schema for the application",
    "context": "We need a database schema that supports users, tasks, and projects.",
    "inputs": [
      {
        "type": "document",
        "path": ".project-memory/idea_clarification/04_refined_idea_and_scope.md",
        "version": "1.0.0",
        "description": "Refined idea and scope of the project"
      }
    ],
    "expectedOutputs": [
      {
        "type": "document",
        "path": ".project-memory/lld/database/schema.md",
        "description": "Database schema definition"
      }
    ],
    "constraintsAndRules": [
      "Follow database best practices",
      "Consider scalability"
    ],
    "acceptanceCriteria": [
      "Schema supports all required entities",
      "Relationships are properly defined",
      "Indexes are specified where appropriate"
    ],
    "priority": "high",
    "deadlineHint": "1 day"
  }
  ```

## Communication 002: Task Completion by Architect
- **Date**: YYYY-MM-DD
- **From**: Architect
- **To**: Orchestrator
- **Subject**: Database Schema Defined
- **Message**: 
  ```json
  {
    "taskId": "TASK-001",
    "result": "completed",
    "summary": "Database schema has been defined with support for users, tasks, and projects",
    "outputArtifacts": [
      {
        "type": "document",
        "path": ".project-memory/lld/database/schema.md",
        "version": "1.0.0",
        "description": "Database schema definition"
      }
    ],
    "notes": "Added indexes for frequently queried fields to improve performance"
  }
  ```

## Communication 003: Clarification Request from Auto-Coder
- **Date**: YYYY-MM-DD
- **From**: Auto-Coder
- **To**: Orchestrator
- **Subject**: Authentication Requirements Clarification
- **Message**: 
  ```json
  {
    "taskId": "TASK-003",
    "result": "clarification_needed",
    "summary": "Need clarification on authentication requirements",
    "questions": [
      "Should we implement token refresh?",
      "What should be the token expiration time?",
      "Do we need to support multiple devices?"
    ]
  }
  ```

## Communication 004: Clarification Response to Auto-Coder
- **Date**: YYYY-MM-DD
- **From**: Orchestrator
- **To**: Auto-Coder
- **Subject**: Authentication Requirements Clarification
- **Message**: 
  ```json
  {
    "taskId": "TASK-003",
    "result": "clarification_provided",
    "answers": [
      {
        "question": "Should we implement token refresh?",
        "answer": "Yes, implement token refresh for better user experience"
      },
      {
        "question": "What should be the token expiration time?",
        "answer": "Access tokens should expire after 15 minutes, refresh tokens after 7 days"
      },
      {
        "question": "Do we need to support multiple devices?",
        "answer": "Yes, users should be able to be logged in from multiple devices"
      }
    ]
  }
  ```
```

### 2. Checkpoint systém

Vylepšit checkpoint systém tak, aby zachycoval kompletní stav epicu v pravidelných intervalech:

#### checkpoint_001.md

```markdown
---
title: "Checkpoint 001: Implement Basic Application Structure"
epic_id: "EPIC-001"
checkpoint_id: "001"
version: "1.0.0"
status: "Active"
created_by: "Orchestrator"
created_date: "YYYY-MM-DDTHH:MM:SSZ"
tags: ["checkpoint", "basic_structure"]
---

# Checkpoint 001: Implement Basic Application Structure

## Epic Status at Checkpoint
- **Progress**: 30%
- **Status**: In Progress
- **Checkpoint Date**: YYYY-MM-DD HH:MM

## Completed Since Last Checkpoint
- Defined database schema
- Implemented database models
- Created basic API endpoints

## Current Work
- Implementing authentication middleware
- Creating basic UI components

## Next Steps
- Integrate API with UI
- Implement error handling
- Add validation

## Important Decisions
- Decided to use PostgreSQL for the database
- Decided to use JWT for authentication
- Decided to use FastAPI for the API

## Issues and Blockers
- Need clarification on authentication requirements

## Relevant Documents
- `.project-memory/lld/database/schema.md` (v1.0.0)
- `.project-memory/lld/api/endpoints.md` (v1.0.0)
- `src/models/user.py` (implemented)
- `src/models/task.py` (implemented)
- `src/models/project.py` (implemented)
- `src/api/auth.py` (in progress)

## Context Recovery Notes
If you are a new Orchestrator taking over this epic, please:
1. Review the epic_state.md file for current status
2. Check task_tracker.md for detailed task status
3. Review decision_log.md for important decisions
4. Check communication_log.md for recent communications
5. Focus on completing the authentication middleware first
```

### 3. Přehled epiců pro EpicCoordinator

Vytvořit strukturovaný přehled epiců pro EpicCoordinator:

#### epic_tracker.md

```markdown
---
title: "Epic Tracker"
version: "1.0.0"
status: "Active"
created_by: "EpicCoordinator"
created_date: "YYYY-MM-DDTHH:MM:SSZ"
last_modified_by: "EpicCoordinator"
last_modified_date: "YYYY-MM-DDTHH:MM:SSZ"
tags: ["epic", "tracker", "project_management"]
---

# Epic Tracker

## Active Epics

### EPIC-001: Implement Basic Application Structure
- **Objective**: Implement the basic structure of the application
- **Status**: In Progress
- **Priority**: High
- **Dependencies**: None
- **Assigned To**: Orchestrator
- **Started**: YYYY-MM-DD
- **Estimated Completion**: YYYY-MM-DD
- **Progress**: 65%
- **Last Checkpoint**: Checkpoint 003 (YYYY-MM-DD)
- **Key Deliverables**:
  - Database models
  - API endpoints
  - Basic UI components
- **Notes**: Authentication middleware in progress

## Planned Epics

### EPIC-002: Implement User Authentication
- **Objective**: Implement user authentication and authorization
- **Status**: Planned
- **Priority**: High
- **Dependencies**: EPIC-001
- **Assigned To**: 
- **Started**: 
- **Estimated Completion**: 
- **Progress**: 0%
- **Key Deliverables**:
  - User registration
  - User login
  - Password reset
  - Role-based access control
- **Notes**: Will use JWT for authentication

### EPIC-003: Implement Task Management
- **Objective**: Implement task creation, editing, and deletion
- **Status**: Planned
- **Priority**: Medium
- **Dependencies**: EPIC-001, EPIC-002
- **Assigned To**: 
- **Started**: 
- **Estimated Completion**: 
- **Progress**: 0%
- **Key Deliverables**:
  - Task CRUD operations
  - Task assignment
  - Task status tracking
  - Task filtering and sorting
- **Notes**: 

## Completed Epics

### EPIC-000: Project Setup
- **Objective**: Set up project structure and initial configuration
- **Status**: Completed
- **Priority**: High
- **Dependencies**: None
- **Assigned To**: Orchestrator
- **Started**: YYYY-MM-DD
- **Completed**: YYYY-MM-DD
- **Key Deliverables**:
  - Project structure
  - Git initialization
  - Basic configuration
- **Notes**: Project structure set up, Git initialized, basic configuration completed
- **Summary Document**: `.project-memory/project_context/epic_summaries/EPIC-000_summary.md`
```

### 4. Protokol pro předávání epicu

Rozšířit protokoly `new_task` a `attempt_completion` pro lepší předávání kontextu mezi EpicCoordinatorem a Orchestrátorem:

#### Rozšířený protokol `new_task` pro delegování epicu

```json
{
  "taskId": "EPIC-001",
  "delegatedToMode": "orchestrator",
  "objective": "Implement basic application structure",
  "context": "We are creating a task management application. In this epic, we need to implement the basic structure including database models, API, and basic UI.",
  "epicContext": {
    "epicId": "EPIC-001",
    "epicName": "Implement Basic Application Structure",
    "epicStatus": "In Progress",
    "epicProgress": "30%",
    "lastCheckpoint": "checkpoint_001.md",
    "stateFile": ".project-memory/epics/EPIC-001/epic_state.md",
    "taskTrackerFile": ".project-memory/epics/EPIC-001/task_tracker.md",
    "decisionLogFile": ".project-memory/epics/EPIC-001/decision_log.md",
    "communicationLogFile": ".project-memory/epics/EPIC-001/communication_log.md"
  },
  "inputs": [
    {
      "type": "document",
      "path": ".project-memory/idea_clarification/04_refined_idea_and_scope.md",
      "version": "1.0.0",
      "description": "Refined idea and scope of the project"
    },
    {
      "type": "document",
      "path": ".project-memory/hld/HLD-MAIN-001_main_architecture.md",
      "version": "1.0.0",
      "description": "Main architecture of the application"
    }
  ],
  "expectedOutputs": [
    {
      "type": "document",
      "path": ".project-memory/project_context/epic_summaries/EPIC-001_summary.md",
      "description": "Summary of the completed epic"
    },
    {
      "type": "code",
      "path": "src/",
      "description": "Implemented code for the basic application structure"
    }
  ],
  "constraintsAndRules": [
    "Focus only on the basic structure of the application",
    "Do not implement advanced features",
    "Ensure the code is well-tested"
  ],
  "acceptanceCriteria": [
    "Database model is implemented",
    "API is implemented and tested",
    "Basic UI is implemented",
    "All tests pass"
  ],
  "priority": "high",
  "deadlineHint": "2 days",
  "contextRecoveryInstructions": "1. Review epic_state.md for current status\n2. Check task_tracker.md for detailed task status\n3. Review decision_log.md for important decisions\n4. Check communication_log.md for recent communications"
}
```

## Závěr

Tyto vylepšení systému memorizace zajistí, že při recyklaci orchestrátora bude mít nový orchestrátor všechny potřebné informace k efektivnímu pokračování v práci na daném epicu. Strukturované soubory stavu epicu, vylepšený checkpoint systém, přehled epiců pro EpicCoordinator a rozšířené protokoly pro předávání epicu poskytují robustní mechanismus pro zachování kontextu mezi recyklacemi.

# AI-Driven RooCode Template

This repository contains a RooCode configuration for implementing the SPARC methodology for AI-driven software development. The configuration is based on the concept described in `.docs/idea.md` and uses RooCode's Custom Modes and Boomerang Tasks features to orchestrate a team of specialized AI agents.

## Release Notes

### Current Version: 1.0.0

#### Iterations
- **Iteration 000: MVP** ✅ DONE
  - Initial implementation of SPARC methodology
  - Basic agent roles and communication protocols
  - Project memory structure
  - Cycle detection and context continuity mechanisms

- **Iteration 001: Orchestrator Improvements** 🔄 IN PROGRESS
  - New EpicCoordinator role for managing orchestrator recycling
  - Enhanced memory system for better context preservation
  - Improved agent communication with better result handling
  - Standardized .gitignore and git management
  - Command line validation for code execution

## Overview

The SPARC methodology (Specification, Pseudocode, Architecture, Refinement, Completion) provides a structured approach to AI-driven software development. This implementation uses RooCode's Custom Modes to define specialized agents for each aspect of the development process, with the SPARC Orchestrator coordinating the workflow.

Key features:
- **Specialized AI Agents**: Each agent has a specific role and expertise
- **Orchestrated Workflow**: The SPARC Orchestrator delegates tasks and manages the process
- **Persistent Memory**: The `.project-memory/` directory serves as the project's persistent memory
- **Test-Driven Development**: Tests are written before implementation code
- **Structured Communication**: Agents communicate using standardized protocols
- **Cycle Detection**: System detects and resolves cyclic errors
- **Context Continuity**: Mechanisms ensure work continuity across context window recycling
- **Epic-Based Development**: Projects are divided into epics managed by the EpicCoordinator

## Agent Roles

The following custom modes (agents) are defined:

| Agent | Role | Description |
|-------|------|-------------|
| 🌟 EpicCoordinator | Project Management | Manages the project at epic level, recycles orchestrators, and maintains high-level project overview |
| ⚡️ SPARC Orchestrator | Epic Coordination | Manages the development process for a single epic, delegates tasks, maintains epic memory, and ensures context continuity |
| 📋 Specification Writer | Requirements | Transforms business requirements into detailed specifications and pseudocode with focus on testability |
| 🏗️ Architect | Design | Designs system architecture, data models, and APIs through HLD and LLD documents |
| 🧠 Auto-Coder | Implementation | Implements code based on specifications and tests following TDD principles |
| 🧪 Tester (TDD) | Testing | Writes comprehensive tests before implementation code for various test types |
| 📚 Documentation Writer | Documentation | Generates and maintains project documentation for different audience types |
| 🛡️ Security Reviewer | Security | Conducts security audits, vulnerability analysis, and recommends mitigations |
| 🤝 Mediator Agent | Conflict Resolution | Resolves conflicts, prevents cyclic errors, and ensures alignment between agents |

## Directory Structure

```
.
├── .roo/                           # RooCode configuration
│   ├── .roomodes                   # Custom modes definitions
│   ├── rules/                      # Global rules for all modes
│   │   └── 06-context-continuity-guidelines.md  # Context continuity guidelines
│   ├── rules-epic-coordinator/     # Rules for EpicCoordinator
│   ├── rules-orchestrator/         # Rules for SPARC Orchestrator
│   │   └── 04-context-management-and-continuity.md  # Context management rules
│   ├── rules-spec-pseudocode/      # Rules for Specification Writer
│   ├── rules-architect/            # Rules for Architect
│   ├── rules-code/                 # Rules for Auto-Coder
│   ├── rules-tdd/                  # Rules for TDD Tester
│   ├── rules-docs-writer/          # Rules for Documentation Writer
│   ├── rules-security/             # Rules for Security Reviewer
│   └── rules-mediator/             # Rules for Mediator Agent
├── .docs/                          # Project documentation
│   ├── idea.md                     # Original concept document
│   ├── iterations/                 # Iteration planning and documentation
│   │   └── 001/                    # Current iteration
│   │       ├── todo.md             # Todo list for the iteration
│   │       ├── epic-coordinator-design.md  # Design of EpicCoordinator
│   │       └── enhanced-memory-system.md   # Enhanced memory system design
│   ├── test_scenarios/             # Test scenarios for validation
│   ├── role_instructions_todolist.md  # Implementation todolist
│   └── sample-instructions.md      # Sample role instructions
└── README.md                       # This file
```

During project execution, the EpicCoordinator and Orchestrators will create and maintain the `.project-memory/` directory, which serves as the project's persistent memory.

## Getting Started

To use this template:

1. Ensure you have RooCode installed in your VS Code environment
2. Clone this repository
3. Open the repository in VS Code
4. Start a conversation with the EpicCoordinator mode
5. Describe your project requirements
6. The EpicCoordinator will guide you through the development process

## Development Workflow

The typical workflow follows the SPARC methodology with epic-based development:

1. **Project Initialization**:
   - The Business Owner describes requirements to the EpicCoordinator
   - The EpicCoordinator captures the initial idea and divides the project into epics
   - The EpicCoordinator delegates the first epic to an Orchestrator

2. **Epic Implementation** (for each epic):
   - **Specification**: The Orchestrator delegates to the Specification Writer to create detailed specifications
   - **Pseudocode**: The Specification Writer creates pseudocode to guide implementation
   - **Architecture**: The Architect designs or refines the system architecture
   - **Refinement**:
     - The TDD Tester writes tests based on specifications
     - The Auto-Coder implements code that passes the tests
     - The Security Reviewer conducts security audits
   - **Completion**:
     - The Documentation Writer creates or updates documentation
     - The Orchestrator returns results to the EpicCoordinator
     - The EpicCoordinator updates the epic tracker and delegates the next epic

Throughout this process, the EpicCoordinator maintains the high-level project overview, while each Orchestrator manages the workflow for a single epic. This approach ensures that the context window remains manageable and that all important information is preserved between orchestrator recycling.

## Cycle Detection and Context Continuity

The system includes mechanisms to detect and resolve cyclic errors (zacyklení) and ensure work continuity across context window recycling:

### Cycle Detection

- **Pattern Recognition**: Identifies repetitive patterns in agent interactions
- **Root Cause Analysis**: Determines underlying causes of cyclic errors
- **Intervention Strategies**: Implements techniques to break cycles
- **Documentation**: Records cycles and resolutions in `cycle_detection_log.md`

### Context Continuity

- **Regular Summarization**: Creates concise summaries of project state
- **Checkpoints**: Establishes checkpoints at natural project milestones
- **Context Recovery**: Implements protocols for recovering context after recycling
- **Hierarchical Documentation**: Maintains documentation at multiple levels of detail

## Communication Protocols

Agents communicate using standardized protocols:

### Task Delegation (`new_task`)

The Orchestrator delegates tasks to specialized agents using the `new_task` protocol:

```json
{
  "taskId": "UNIQUE-TASK-ID-001",
  "parentTaskId": "PARENT-TASK-ID-001",
  "delegatedToMode": "agent-slug",
  "objective": "Clear, concise description of what needs to be accomplished",
  "context": "Summary of relevant project context and background information",
  "inputs": [
    {
      "type": "document",
      "path": ".project-memory/path/to/input_document.md",
      "version": "commit-hash or version",
      "description": "Description of this input"
    }
  ],
  "expectedOutputs": [
    {
      "type": "document",
      "path": ".project-memory/path/to/expected_output.md",
      "description": "Description of what this output should contain"
    }
  ],
  "constraintsAndRules": [
    "Constraint or rule 1",
    "Constraint or rule 2"
  ],
  "acceptanceCriteria": [
    "Criterion 1",
    "Criterion 2"
  ],
  "priority": "high|medium|low",
  "deadlineHint": "YYYY-MM-DDTHH:MM:SSZ or descriptive timeframe"
}
```

### Task Completion (`attempt_completion`)

Agents report task completion (or issues) back to the Orchestrator using the `attempt_completion` protocol:

```json
{
  "taskId": "UNIQUE-TASK-ID-001",
  "result": "success|failure|clarification_needed|conflict_detected",
  "summary": "Concise summary of what was accomplished or the issues encountered",
  "outputArtifacts": [
    {
      "type": "document",
      "path": ".project-memory/path/to/output_document.md",
      "version": "commit-hash or version",
      "description": "Description of this output"
    }
  ],
  "issues_encountered": [
    {
      "type": "clarification_needed|technical_issue|conflict|other",
      "description": "Detailed description of the issue",
      "suggestedResolution": "Suggested approach to resolve this issue"
    }
  ]
}
```

## Project Memory

The `.project-memory/` directory serves as the project's persistent memory. It is structured as follows:

```
.project-memory/
├── project_meta/                  # Metadata projektu
│   ├── documentation_structure_config.md
│   └── project_glossary.md
├── idea_clarification/            # Počáteční myšlenka a upřesnění
│   ├── 01_initial_idea_capture.md
│   ├── 02_architect_clarification_log.md
│   ├── 03_architectural_explanations_for_bv.md
│   ├── 04_refined_idea_and_scope.md
│   └── bv_architect_sync_log.md
├── project_context/               # Globální kontext projektu
│   ├── product_overview.md        # Přehled produktu
│   ├── epic_tracker.md            # Přehled všech epiců
│   ├── global_decision_log.md     # Globální rozhodnutí
│   ├── bv_communication_log.md    # Komunikace s Business Vlastníkem
│   ├── system_patterns.md         # Vzory systému
│   ├── progress_tracker.md        # Sledování postupu
│   ├── conflict_resolution_log.md # Řešení konfliktů
│   ├── cycle_detection_log.md     # Detekce cyklů
│   └── summaries/                 # Sumarizace projektu (vysoká úroveň)
├── hld/                           # Globální High-Level Design
├── lld/                           # Globální Low-Level Design (architektura)
├── epics/                         # Struktura pro epicy
│   ├── EPIC-001/                  # Specifické informace pro Epic 1
│   │   ├── epic_state.md          # Stav epicu
│   │   ├── task_tracker.md        # Sledování úkolů v rámci epicu
│   │   ├── epic_decision_log.md   # Rozhodnutí specifická pro epic
│   │   ├── agent_communication_log.md # Komunikace mezi agenty v rámci epicu
│   │   ├── epic_lld/              # LLD specifické pro implementaci epicu
│   │   └── checkpoints/           # Checkpointy epicu
│   │       └── ...
│   └── ...
└── project_postulates.md          # Postuláty projektu
```

Additional directories may be added as needed based on project requirements.

## Customization

You can customize this template by:

1. Modifying the agent definitions in `.roo/custom_modes.json`
2. Updating the rules in the `.roo/rules/` and `.roo/rules-*/` directories
3. Adjusting the project memory structure in the Orchestrator's guidelines
4. Customizing the cycle detection and context continuity mechanisms
5. Modifying the communication protocols between agents

## License

This project is licensed under the BSD 3-Clause License - see the LICENSE file for details.

## Acknowledgments

- Based on the SPARC methodology concept in `.docs/idea.md`
- Implemented using RooCode's Custom Modes and Boomerang Tasks features
- Enhanced with cycle detection and context continuity mechanisms
- Detailed role instructions available in `.docs/` directory

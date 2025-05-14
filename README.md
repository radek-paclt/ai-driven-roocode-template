# AI-Driven RooCode Template

This repository contains a RooCode configuration for implementing the SPARC methodology for AI-driven software development. The configuration is based on the concept described in `.docs/idea.md` and uses RooCode's Custom Modes and Boomerang Tasks features to orchestrate a team of specialized AI agents.

## Overview

The SPARC methodology (Specification, Pseudocode, Architecture, Refinement, Completion) provides a structured approach to AI-driven software development. This implementation uses RooCode's Custom Modes to define specialized agents for each aspect of the development process, with the SPARC Orchestrator coordinating the workflow.

Key features:
- **Specialized AI Agents**: Each agent has a specific role and expertise
- **Orchestrated Workflow**: The SPARC Orchestrator delegates tasks and manages the process
- **Persistent Memory**: The `.project-memory/` directory serves as the project's persistent memory
- **Test-Driven Development**: Tests are written before implementation code
- **Structured Communication**: Agents communicate using standardized protocols
- **Cycle Detection**: System detects and resolves cyclic errors (zacyklení)
- **Context Continuity**: Mechanisms ensure work continuity across context window recycling

## Agent Roles

The following custom modes (agents) are defined:

| Agent | Role | Description |
|-------|------|-------------|
| ⚡️ SPARC Orchestrator | Coordination | Manages the development process, delegates tasks, maintains project memory, and ensures context continuity |
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
│   ├── rules-sparc/                # Rules for SPARC Orchestrator
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
│   ├── role_instructions_todolist.md  # Implementation todolist
│   └── sample-instructions.md      # Sample role instructions
└── README.md                       # This file
```

During project execution, the SPARC Orchestrator will create and maintain the `.project-memory/` directory, which serves as the project's persistent memory.

## Getting Started

To use this template:

1. Ensure you have RooCode installed in your VS Code environment
2. Clone this repository
3. Open the repository in VS Code
4. Start a conversation with the SPARC Orchestrator mode
5. Describe your project requirements
6. The Orchestrator will guide you through the development process

## Development Workflow

The typical workflow follows the SPARC methodology:

1. **Specification**: The Business Owner describes requirements to the Orchestrator, who delegates to the Specification Writer to create detailed specifications
2. **Pseudocode**: The Specification Writer creates pseudocode to guide implementation
3. **Architecture**: The Architect designs the system architecture, data models, and APIs
4. **Refinement**:
   - The TDD Tester writes tests based on specifications
   - The Auto-Coder implements code that passes the tests
   - The Security Reviewer conducts security audits
5. **Completion**:
   - The Documentation Writer creates user documentation
   - The system is integrated and deployed

Throughout this process, the SPARC Orchestrator manages the workflow, delegates tasks, and maintains the project's memory in the `.project-memory/` directory.

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
├── project_meta/
│   ├── documentation_structure_config.md
│   └── project_glossary.md
├── idea_clarification/
│   ├── 01_initial_idea_capture.md
│   ├── 02_architect_clarification_log.md
│   ├── 03_architectural_explanations_for_bv.md
│   ├── 04_refined_idea_and_scope.md
│   └── bv_architect_sync_log.md
├── project_context/
│   ├── product_overview.md
│   ├── active_threads.md
│   ├── decision_log.md
│   ├── system_patterns.md
│   ├── progress_tracker.md
│   ├── conflict_resolution_log.md
│   ├── cycle_detection_log.md
│   └── state_summaries/           # Project state summaries for continuity
├── hld/                           # High-Level Design documents
│   └── summaries/                 # Architecture summaries for quick context recovery
├── lld/                           # Low-Level Design documents
└── project_postulates.md
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

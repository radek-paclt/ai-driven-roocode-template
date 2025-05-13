# Project Memory Guidelines

This document outlines the structure, usage, and management principles for the `.project-memory/` directory, which serves as the persistent memory for the project.

## Purpose and Concept

The `.project-memory/` directory is the primary, structured, internal working memory for AI agents. It:
- Serves as a "single source of truth" for all project-related information
- Is versioned using Git (managed by the Orchestrator)
- Contains Markdown files and diagrams (e.g., Mermaid)
- Is NOT intended for direct consumption by end users (use `docs/` for that)

## Directory Structure

The `.project-memory/` directory has a modular and configurable structure:

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
│   └── conflict_resolution_log.md
└── project_postulates.md
```

Additional modules may include:
- `hld/` - High-Level Design documents
- `lld/` - Low-Level Design documents
- `api_design_artifacts/` - API design documentation
- `ui_ux_working_docs/` - UI/UX design documentation
- `testing_strategy_and_plans/` - Testing documentation
- `coding_guidelines_and_notes/` - Coding standards and notes

## File Naming and Structure

### Naming Conventions
- Use `snake_case_with_prefixes.md`
- Use numerical prefixes for ordering (e.g., `01_`, `02_`)

### Markdown Structure
Each Markdown file in `.project-memory/` MUST include:

```yaml
---
title: "Descriptive title of the document"
version: "major.minor.patch"
status: "Draft | InReview | ApprovedByBV | ApprovedByTechLead | Implemented | Obsolete"
created_by: "Agent ID or 'BusinessOwner' or 'SPARC_Orchestrator'"
created_date: "YYYY-MM-DDTHH:MM:SSZ"
last_modified_by: "Agent ID or 'SPARC_Orchestrator'"
last_modified_date: "YYYY-MM-DDTHH:MM:SSZ"
related_tasks: ["TASK-ID-001", "FEATURE-XYZ"]
relevant_links: ["./02_related_document.md"]
tags: ["architecture", "iot", "backend"]
parent_document: "./relative/path/to/parent_doc.md"
child_documents: ["./details/specific_module_spec.md"]
related_concepts: ["concept_id_1", "glossary_term_X"]
project_type_tags: ["web-app", "api-backend"]
visibility: "internal"
---
```

## Usage Guidelines

### For All Agents
1. **Reading**: Always reference the latest version of documents
2. **Writing**: Never modify files directly; request the Orchestrator to make changes
3. **Referencing**: Use relative paths when linking between documents
4. **Versioning**: Be aware of document versions and statuses

### For the Orchestrator
1. **Creation**: Create new files with proper metadata
2. **Updates**: Update metadata when modifying files
3. **Versioning**: Commit changes with semantic commit messages
4. **Structure**: Maintain the directory structure according to `documentation_structure_config.md`

## Examples

### Example: Creating a New Document

```markdown
---
title: "Authentication Service Design"
version: "0.1.0"
status: "Draft"
created_by: "architect"
created_date: "2023-05-15T14:30:00Z"
last_modified_by: "architect"
last_modified_date: "2023-05-15T14:30:00Z"
related_tasks: ["AUTH-SERVICE-DESIGN"]
relevant_links: ["../hld/system_architecture.md"]
tags: ["authentication", "security", "backend"]
parent_document: "../hld/system_architecture.md"
child_documents: []
related_concepts: ["jwt", "oauth"]
project_type_tags: ["web-app", "api-backend"]
visibility: "internal"
---

# Authentication Service Design

## Overview
This document describes the design of the authentication service...
```

### Example: Updating a Document

When updating a document, the Orchestrator should:
1. Update the `version` field according to semantic versioning
2. Change the `status` if appropriate
3. Update the `last_modified_by` and `last_modified_date` fields
4. Commit the changes with a semantic commit message

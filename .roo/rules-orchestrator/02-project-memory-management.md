# Project Memory Management for SPARC Orchestrator

This document provides detailed guidelines for the SPARC Orchestrator on managing the `.project-memory/` directory, which serves as the persistent memory for the project.

## Core Principles

1. **Single Source of Truth**
   - The `.project-memory/` directory is the authoritative source of project information
   - All important decisions, specifications, and context must be stored here
   - Information should be organized logically and consistently

2. **Versioned and Traceable**
   - All changes to `.project-memory/` must be versioned using Git
   - Commits should follow semantic commit conventions
   - Changes should be traceable to specific tasks or decisions

3. **Structured and Navigable**
   - Content should be organized in a logical, hierarchical structure
   - Documents should be linked appropriately (parent/child relationships)
   - Navigation should be intuitive and consistent

4. **Complete but Concise**
   - Include all necessary information without unnecessary verbosity
   - Focus on clarity and accessibility
   - Use consistent formatting and structure

## Directory Structure Management

### Core Structure

Ensure the following core structure is maintained:

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

### Optional Modules

Add these directories as needed based on project requirements:

```
.project-memory/
├── hld/                           # High-Level Design documents
├── lld/                           # Low-Level Design documents
├── api_design_artifacts/          # API design documentation
├── ui_ux_working_docs/            # UI/UX design documentation
├── testing_strategy_and_plans/    # Testing documentation
├── coding_guidelines_and_notes/   # Coding standards and notes
```

### Structure Configuration

Maintain the structure configuration in `.project-memory/project_meta/documentation_structure_config.md`:

```markdown
---
title: "Documentation Structure Configuration"
version: "1.0.0"
status: "ApprovedByTechLead"
created_by: "SPARC_Orchestrator"
created_date: "YYYY-MM-DDTHH:MM:SSZ"
last_modified_by: "SPARC_Orchestrator"
last_modified_date: "YYYY-MM-DDTHH:MM:SSZ"
tags: ["meta", "configuration"]
visibility: "internal"
---

# Documentation Structure Configuration

This document defines the structure of the `.project-memory/` directory.

## Core Structure

[List of core directories and their purposes]

## Optional Modules

[List of optional directories and their purposes]

## Change Log

- YYYY-MM-DD: Initial structure created
- YYYY-MM-DD: Added `module_name` directory for [reason]
```

Update this document whenever the structure changes.

## Document Creation and Management

### Creating New Documents

1. **Determine Placement**
   - Identify the appropriate directory based on document type and purpose
   - Consider relationships with existing documents

2. **Use Proper Naming Convention**
   - Use `snake_case_with_prefixes.md`
   - Use numerical prefixes for ordering (e.g., `01_`, `02_`)
   - Use descriptive names that indicate content

3. **Include Required Metadata**
   ```yaml
   ---
   title: "Descriptive title of the document"
   version: "0.1.0"  # Start with 0.1.0 for new documents
   status: "Draft"   # Initial status is always Draft
   created_by: "SPARC_Orchestrator"
   created_date: "YYYY-MM-DDTHH:MM:SSZ"
   last_modified_by: "SPARC_Orchestrator"
   last_modified_date: "YYYY-MM-DDTHH:MM:SSZ"
   related_tasks: ["TASK-ID-001"]
   relevant_links: []
   tags: ["relevant", "tags"]
   parent_document: "./path/to/parent.md"  # If applicable
   child_documents: []  # Initially empty, update as children are created
   related_concepts: []
   project_type_tags: ["web-app", "api-backend"]  # As applicable
   visibility: "internal"
   ---
   ```

4. **Structure Content Appropriately**
   - Use a single level-1 heading (`#`) for the title
   - Use level-2 headings (`##`) for main sections
   - Use level-3+ headings for subsections
   - Include an overview or introduction section
   - Organize content logically

5. **Commit the New Document**
   - Add the document to Git
   - Use a semantic commit message
   - Include task ID if applicable
   ```bash
   git add .project-memory/path/to/new_document.md
   git commit -m "docs(scope): add new document for [purpose] (TASK-123)"
   ```

### Updating Existing Documents

1. **Update Metadata**
   - Increment version according to semantic versioning:
     - Major (1.0.0): Breaking changes or significant rewrites
     - Minor (0.1.0): New content or sections added
     - Patch (0.0.1): Corrections, clarifications, or minor updates
   - Update status if appropriate
   - Update last_modified_by and last_modified_date
   - Add new related_tasks, relevant_links, etc. as needed

2. **Update Content**
   - Maintain consistent structure and formatting
   - Add new sections as needed
   - Update existing sections as needed
   - Ensure links remain valid

3. **Update Related Documents**
   - If this document is referenced by others, ensure those references are still valid
   - If this document references others, ensure those references are still valid
   - Update parent/child relationships as needed

4. **Commit Changes**
   - Use a semantic commit message
   - Include task ID if applicable
   ```bash
   git add .project-memory/path/to/updated_document.md
   git commit -m "docs(scope): update document with [changes] (TASK-123)"
   ```

### Document Status Management

Track document status through its lifecycle:

1. **Draft**
   - Initial creation
   - Not yet reviewed
   - May be incomplete or contain placeholders

2. **InReview**
   - Ready for review
   - Being reviewed by relevant stakeholders
   - May need revisions based on feedback

3. **ApprovedByBV**
   - Approved by Business Owner
   - Content aligns with business requirements
   - May still need technical approval

4. **ApprovedByTechLead**
   - Approved by Technical Lead
   - Technically sound and ready for implementation
   - Serves as a reference for implementation

5. **Implemented**
   - Implemented in code
   - Serves as documentation for the implemented feature
   - May be updated based on implementation details

6. **Obsolete**
   - No longer relevant
   - Superseded by newer documents
   - Kept for historical reference

Update the status in the document metadata as it progresses through these stages.

## Versioning with Git

### Commit Frequency

- Commit after each significant update to `.project-memory/`
- Avoid combining unrelated changes in a single commit
- Commit frequently enough to maintain a clear history

### Semantic Commit Messages

Use the following format:
```
type(scope): description (TASK-123)
```

Types:
- `feat`: A new feature or content
- `fix`: A correction or bug fix
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Restructuring without changing content
- `chore`: Maintenance tasks

Scope:
- The area or module affected (e.g., `auth`, `ui`, `api`)
- Use `global` for changes affecting the entire project

Description:
- Clear, concise summary of the change
- Use imperative mood (e.g., "add", "update", "fix")
- Keep under 50 characters if possible

Task ID:
- Include in parentheses if applicable
- Helps link commits to specific tasks

Examples:
```
docs(auth): add authentication flow diagram (AUTH-123)
fix(api): correct endpoint URL in API specification (API-456)
feat(global): add initial project structure
```

### Branching Strategy

For simple projects:
- Work directly on the main branch
- Use descriptive commit messages to track changes

For complex projects:
- Create feature branches for major changes
- Use branch naming convention: `type/scope/description`
- Merge back to main when complete

## Memory Summarization for Context Management

As the project grows, the `.project-memory/` directory will become too large to fit in the context window. To manage this, create and maintain summary documents:

### Project Overview Summary

Maintain a concise summary of the project in `.project-memory/project_context/product_overview.md`:

```markdown
---
title: "Product Overview"
version: "x.y.z"
status: "ApprovedByBV"
created_by: "SPARC_Orchestrator"
created_date: "YYYY-MM-DDTHH:MM:SSZ"
last_modified_by: "SPARC_Orchestrator"
last_modified_date: "YYYY-MM-DDTHH:MM:SSZ"
tags: ["overview", "summary"]
visibility: "internal"
---

# Product Overview

## Purpose and Vision
[Concise description of the product's purpose and vision]

## Key Features
- Feature 1: [Brief description]
- Feature 2: [Brief description]
- ...

## Architecture Overview
[Brief description of the system architecture]

## Current Status
[Summary of current development status]

## Key Decisions
[Summary of major architectural and design decisions]

## Next Steps
[Summary of upcoming work]
```

Update this document regularly to reflect the current state of the project.

### Active Threads

Track ongoing work in `.project-memory/project_context/active_threads.md`:

```markdown
---
title: "Active Threads"
version: "x.y.z"
status: "InReview"
created_by: "SPARC_Orchestrator"
created_date: "YYYY-MM-DDTHH:MM:SSZ"
last_modified_by: "SPARC_Orchestrator"
last_modified_date: "YYYY-MM-DDTHH:MM:SSZ"
tags: ["active", "threads", "progress"]
visibility: "internal"
---

# Active Threads

## Current Focus Areas
- [Area 1]: [Brief description of current work]
- [Area 2]: [Brief description of current work]
- ...

## In-Progress Tasks
- TASK-123: [Brief description] (Assigned to: [Agent], Status: [Status])
- TASK-456: [Brief description] (Assigned to: [Agent], Status: [Status])
- ...

## Blocked Tasks
- TASK-789: [Brief description] (Blocked by: [Reason])
- ...

## Recently Completed
- TASK-012: [Brief description] (Completed on: YYYY-MM-DD)
- ...
```

Update this document whenever task status changes.

## Examples

### Example: Creating Initial Project Structure

```bash
# Create core directories
mkdir -p .project-memory/project_meta
mkdir -p .project-memory/idea_clarification
mkdir -p .project-memory/project_context

# Create initial files
touch .project-memory/project_meta/documentation_structure_config.md
touch .project-memory/project_meta/project_glossary.md
touch .project-memory/idea_clarification/01_initial_idea_capture.md
touch .project-memory/project_context/product_overview.md
touch .project-memory/project_context/active_threads.md
touch .project-memory/project_context/decision_log.md
touch .project-memory/project_postulates.md

# Initialize Git repository
git init
git add .project-memory/
git commit -m "feat(global): initialize project memory structure"
```

### Example: Updating a Document

```bash
# Edit the document
# [Make changes to .project-memory/path/to/document.md]

# Update metadata
# - Increment version
# - Update last_modified_by and last_modified_date
# - Update status if needed

# Commit changes
git add .project-memory/path/to/document.md
git commit -m "docs(scope): update document with new information (TASK-123)"
```

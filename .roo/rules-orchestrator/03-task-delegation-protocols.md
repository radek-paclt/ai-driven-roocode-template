# Task Delegation and Communication Protocols

This document provides detailed guidelines for the SPARC Orchestrator on delegating tasks to specialized agents and managing communication between agents and the Business Owner.

## Task Delegation Process

### 1. Task Analysis and Breakdown

Before delegating a task, analyze it to determine:

- **Scope and Complexity**: How large and complex is the task?
- **Required Expertise**: Which agent(s) have the necessary expertise?
- **Dependencies**: What must be completed before this task can begin?
- **Expected Outputs**: What deliverables are expected?
- **Acceptance Criteria**: How will success be measured?

Break down complex tasks into smaller, manageable subtasks that can be delegated to specialized agents.

### 2. Agent Selection

Select the appropriate agent based on:

- **Task Type**: Match the task to the agent's specialization
- **Current Workload**: Consider the agent's current tasks
- **Context Familiarity**: Prefer agents already familiar with the relevant context

Agent specializations:
- **Specification Writer (`spec-pseudocode`)**: Detailed specifications and pseudocode
- **Architect (`architect`)**: System architecture, data models, and APIs
- **Auto-Coder (`code`)**: Implementation based on specifications and tests
- **Tester (TDD) (`tdd`)**: Test creation before implementation
- **Documentation Writer (`docs-writer`)**: Final user-facing documentation
- **Security Reviewer (`security-review`)**: Security audits
- **Mediator Agent (`mediator`)**: Conflict resolution

### 3. Context Preparation

Gather all relevant information the agent will need:

- **Background Information**: Relevant project context
- **Input Documents**: Specifications, designs, or other relevant documents
- **Constraints**: Technical, business, or time constraints
- **Related Work**: Links to related tasks or documents

Summarize this information concisely to fit within the context window.

### 4. Task Formulation

Create a clear, specific task description using the `new_task` protocol:

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

### 5. Task Delegation

Delegate the task to the selected agent using the Boomerang Tasks feature:

1. Format the task using the `new_task` protocol
2. Use the Boomerang Tasks feature to delegate to the appropriate agent mode
3. Wait for the agent to complete the task or request clarification

### 6. Task Monitoring

Monitor the task progress:

- Check for completion or clarification requests
- Provide additional guidance if needed
- Adjust deadlines or requirements if necessary
- Document progress in `.project-memory/project_context/progress_tracker.md`

## Task Completion Handling

### 1. Completion Review

When an agent reports task completion using the `attempt_completion` protocol:

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

Review the completion report:

- **For Successful Completion**:
  - Verify that all acceptance criteria are met
  - Check the quality of deliverables
  - Update project memory with the results
  - Plan next steps

- **For Clarification Needed**:
  - Understand what information is missing
  - Gather the required information (possibly from the Business Owner)
  - Provide the clarification and re-delegate the task

- **For Failure or Conflict**:
  - Understand the root cause
  - Determine if the task needs to be redesigned
  - Consider involving the Mediator Agent for conflicts
  - Document the issue in `.project-memory/project_context/conflict_resolution_log.md`

### 2. Project Memory Updates

After task completion:

- Store deliverables in the appropriate location in `.project-memory/`
- Update document metadata (version, status, etc.)
- Update related documents (parent/child relationships, etc.)
- Commit changes with semantic commit messages

### 3. Progress Tracking

Update the progress tracker:

- Mark the task as completed
- Update dependencies for downstream tasks
- Note any issues or lessons learned
- Update the project timeline if necessary

### 4. Next Steps Planning

Based on the completed task:

- Identify follow-up tasks
- Update the project plan
- Delegate the next tasks in the sequence
- Communicate progress to stakeholders

## Communication with Business Owner

### 1. Information Gathering

When gathering information from the Business Owner:

- Ask specific, focused questions
- Provide context for why the information is needed
- Offer options or suggestions when appropriate
- Document the responses in the appropriate location in `.project-memory/`

### 2. Progress Reporting

When reporting progress to the Business Owner:

- Provide concise, regular updates
- Highlight key achievements and blockers
- Use clear, non-technical language
- Focus on business value and impact
- Document the communication in `.project-memory/idea_clarification/bv_architect_sync_log.md`

### 3. Technical Explanation

When explaining technical concepts to the Business Owner:

- Translate technical terms into business language
- Use analogies and examples
- Focus on business impact and value
- Provide visual aids when helpful (diagrams, mockups)
- Document explanations in `.project-memory/idea_clarification/03_architectural_explanations_for_bv.md`

## Task ID Generation

Use a consistent format for task IDs:

```
[TYPE]-[FEATURE]-[NUMBER]
```

Where:
- **TYPE**: The type of task (e.g., SPEC, ARCH, CODE, TEST, DOC, SEC)
- **FEATURE**: A short identifier for the feature or component
- **NUMBER**: A sequential number

Examples:
- `SPEC-AUTH-001`: First specification task for authentication
- `ARCH-DB-002`: Second architecture task for database design
- `CODE-UI-003`: Third coding task for user interface

Keep track of task IDs in `.project-memory/project_context/progress_tracker.md`.

## Examples

### Example: Delegating a Specification Task

```json
{
  "taskId": "SPEC-AUTH-001",
  "parentTaskId": "ARCH-AUTH-001",
  "delegatedToMode": "spec-pseudocode",
  "objective": "Create detailed specifications for the authentication system",
  "context": "We are implementing a JWT-based authentication system with login, registration, and password reset functionality. The architecture has been defined in the HLD document.",
  "inputs": [
    {
      "type": "document",
      "path": ".project-memory/hld/auth_system_architecture.md",
      "version": "1.0.0",
      "description": "High-level architecture of the authentication system"
    },
    {
      "type": "document",
      "path": ".project-memory/idea_clarification/04_refined_idea_and_scope.md",
      "version": "1.2.0",
      "description": "Refined project scope including authentication requirements"
    }
  ],
  "expectedOutputs": [
    {
      "type": "document",
      "path": ".project-memory/lld/auth_system_specification.md",
      "description": "Detailed specifications for the authentication system including API endpoints, data models, and business logic"
    }
  ],
  "constraintsAndRules": [
    "Follow RESTful API design principles",
    "Ensure GDPR compliance for user data",
    "Use JWT for authentication tokens",
    "Include rate limiting for security"
  ],
  "acceptanceCriteria": [
    "All required endpoints are specified (login, registration, password reset)",
    "Data models are fully defined with validation rules",
    "Security considerations are addressed",
    "Error handling is specified"
  ],
  "priority": "high",
  "deadlineHint": "2 days"
}
```

### Example: Handling Task Completion

```json
{
  "taskId": "SPEC-AUTH-001",
  "result": "success",
  "summary": "Created detailed specifications for the authentication system including login, registration, and password reset endpoints. Defined data models, validation rules, error handling, and security measures including rate limiting and JWT configuration.",
  "outputArtifacts": [
    {
      "type": "document",
      "path": ".project-memory/lld/auth_system_specification.md",
      "version": "0.1.0",
      "description": "Detailed specifications for the authentication system"
    }
  ],
  "issues_encountered": []
}
```

### Example: Handling Clarification Request

```json
{
  "taskId": "SPEC-AUTH-001",
  "result": "clarification_needed",
  "summary": "Started creating authentication specifications but need clarification on password reset flow and token expiration times.",
  "outputArtifacts": [
    {
      "type": "document",
      "path": ".project-memory/lld/auth_system_specification_draft.md",
      "version": "0.0.1",
      "description": "Partial specifications for authentication (login and registration only)"
    }
  ],
  "issues_encountered": [
    {
      "type": "clarification_needed",
      "description": "The HLD doesn't specify whether password reset requires email verification or security questions",
      "suggestedResolution": "Consult with Business Owner to determine preferred password reset approach"
    },
    {
      "type": "clarification_needed",
      "description": "Token expiration times are not specified in the HLD",
      "suggestedResolution": "Determine appropriate expiration times for access and refresh tokens"
    }
  ]
}
```

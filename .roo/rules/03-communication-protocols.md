# Communication Protocols

This document defines the structured communication protocols used between the Orchestrator and other agents. These protocols ensure clear, consistent, and traceable task delegation and completion.

## Task Delegation: `new_task` Protocol

The `new_task` protocol is used by the Orchestrator to delegate tasks to specialized agents. It follows a structured JSON format:

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

### Field Descriptions

- **taskId**: A unique identifier for this task
- **parentTaskId**: The ID of the parent task (if this is a subtask)
- **delegatedToMode**: The slug of the agent mode this task is delegated to
- **objective**: A clear, concise description of what needs to be accomplished
- **context**: A summary of relevant project context and background information
- **inputs**: An array of input artifacts (primarily from `.project-memory/`)
  - **type**: The type of input (document, code, etc.)
  - **path**: The path to the input artifact
  - **version**: The version or commit hash of the input
  - **description**: A description of this input
- **expectedOutputs**: An array of expected output artifacts
  - **type**: The type of output (document, code, etc.)
  - **path**: The expected path for the output artifact
  - **description**: A description of what this output should contain
- **constraintsAndRules**: An array of constraints or rules for this task
- **acceptanceCriteria**: An array of criteria that must be met for the task to be considered complete
- **priority**: The priority of this task (high, medium, low)
- **deadlineHint**: A suggested deadline or timeframe for this task

## Task Completion: `attempt_completion` Protocol

The `attempt_completion` protocol is used by agents to report task completion (or issues) back to the Orchestrator. It follows a structured JSON format:

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

### Field Descriptions

- **taskId**: The unique identifier of the completed task (matching the original `new_task` taskId)
- **result**: The outcome of the task attempt
  - **success**: The task was completed successfully
  - **failure**: The task could not be completed
  - **clarification_needed**: More information is needed to complete the task
  - **conflict_detected**: A conflict was detected that prevents task completion
- **summary**: A concise summary of what was accomplished or the issues encountered
- **outputArtifacts**: An array of output artifacts produced during the task
  - **type**: The type of output (document, code, etc.)
  - **path**: The path to the output artifact
  - **version**: The version or commit hash of the output
  - **description**: A description of this output
- **issues_encountered**: An array of issues encountered during the task (if any)
  - **type**: The type of issue
  - **description**: A detailed description of the issue
  - **suggestedResolution**: A suggested approach to resolve this issue

## Examples

### Example: Delegating a Task to Create an API Specification

```json
{
  "taskId": "API-SPEC-001",
  "parentTaskId": "FEATURE-AUTH-001",
  "delegatedToMode": "spec-pseudocode",
  "objective": "Create a detailed API specification for the authentication endpoints",
  "context": "We are implementing a JWT-based authentication system with login, registration, and password reset endpoints",
  "inputs": [
    {
      "type": "document",
      "path": ".project-memory/hld/auth_system_design.md",
      "version": "1.0.0",
      "description": "High-level design of the authentication system"
    }
  ],
  "expectedOutputs": [
    {
      "type": "document",
      "path": ".project-memory/lld/api_specifications/auth_api_spec.md",
      "description": "Detailed API specification for authentication endpoints"
    }
  ],
  "constraintsAndRules": [
    "Follow RESTful API design principles",
    "Include request/response examples for each endpoint",
    "Document all error responses"
  ],
  "acceptanceCriteria": [
    "All endpoints from the HLD are specified",
    "Request/response formats are clearly defined",
    "Security considerations are addressed"
  ],
  "priority": "high",
  "deadlineHint": "2 days"
}
```

### Example: Reporting Task Completion

```json
{
  "taskId": "API-SPEC-001",
  "result": "success",
  "summary": "Created detailed API specification for authentication endpoints including login, registration, and password reset. Documented request/response formats, error handling, and security considerations.",
  "outputArtifacts": [
    {
      "type": "document",
      "path": ".project-memory/lld/api_specifications/auth_api_spec.md",
      "version": "0.1.0",
      "description": "Detailed API specification for authentication endpoints"
    }
  ],
  "issues_encountered": []
}
```

### Example: Reporting Clarification Needed

```json
{
  "taskId": "API-SPEC-001",
  "result": "clarification_needed",
  "summary": "Started creating API specification but need clarification on password reset flow",
  "outputArtifacts": [
    {
      "type": "document",
      "path": ".project-memory/lld/api_specifications/auth_api_spec_draft.md",
      "version": "0.0.1",
      "description": "Partial API specification (login and registration only)"
    }
  ],
  "issues_encountered": [
    {
      "type": "clarification_needed",
      "description": "The HLD doesn't specify whether password reset requires email verification or security questions",
      "suggestedResolution": "Consult with Business Owner to determine preferred password reset approach"
    }
  ]
}
```

# Context Continuity Guidelines

This document provides guidelines for maintaining continuity of work across context window recycling and preventing cyclic errors (zacyklení). These guidelines apply to all agents but are primarily the responsibility of the SPARC Orchestrator.

## Context Window Management

### Summarization Practices

1. **Regular Summarization**
   - Regularly summarize the current state of work
   - Focus on key information and decisions
   - Create concise, structured summaries
   - Include timestamps and version information
   - Store summaries in appropriate locations in `.project-memory/`

2. **Hierarchical Summarization**
   - Create summaries at multiple levels of detail:
     - High-level project overview
     - Component or feature-level summaries
     - Detailed summaries for active work areas
   - Link between summary levels for easy navigation
   - Update higher-level summaries when significant changes occur

3. **Summarization Format**
   ```markdown
   # [Topic] Summary - [Date]
   
   ## Current Status
   [Brief description of current status]
   
   ## Key Points
   - [Key point 1]
   - [Key point 2]
   - [Key point 3]
   
   ## Active Threads
   1. [Thread 1]: [Status]
   2. [Thread 2]: [Status]
   
   ## Next Steps
   1. [Next step 1]
   2. [Next step 2]
   
   ## References
   - [Reference to detailed document 1]
   - [Reference to detailed document 2]
   ```

### Checkpoint Creation

1. **When to Create Checkpoints**
   - At natural project milestones
   - Before complex task sequences
   - Periodically (e.g., daily or after X interactions)
   - When context window is approaching capacity
   - Before expected context recycling

2. **Checkpoint Content**
   - Current project state summary
   - Active threads and their status
   - Pending decisions and their context
   - Recently completed work
   - Immediate next steps
   - Critical context that would be difficult to reconstruct

3. **Checkpoint Format**
   ```markdown
   # Checkpoint [ID] - [Date]
   
   ## Project Phase
   [Current phase of the project]
   
   ## Summary
   [Brief summary of current project state]
   
   ## Active Threads
   1. [Thread ID]: [Description]
      - Status: [Status]
      - Next steps: [Next steps]
      - Assigned to: [Agent]
      - Related documents: [Links]
   
   2. [Thread ID]: [Description]
      ...
   
   ## Recent Completions
   - [Recently completed task 1]
   - [Recently completed task 2]
   
   ## Pending Decisions
   1. [Decision 1]
      - Context: [Context]
      - Options: [Options]
      - Deadline: [Deadline]
   
   2. [Decision 2]
      ...
   
   ## Next Steps
   1. [Next step 1]
   2. [Next step 2]
   
   ## Critical Context
   [Any critical context that would be difficult to reconstruct]
   
   ## Related Documents
   - [Document 1]: [Version]
   - [Document 2]: [Version]
   ```

### Context Recovery

1. **Recovery Protocol**
   - When restarting after context recycling:
     1. Read the latest checkpoint
     2. Review active threads document
     3. Check recent Git commits to `.project-memory/`
     4. Review the progress tracker
     5. Identify the most urgent next steps

2. **Depth-First Recovery**
   - Start with high-level summaries
   - Progressively dive deeper into specific areas as needed
   - Focus on recovering context for active threads first
   - Defer loading context for completed or inactive areas

3. **Explicit Context Status**
   - Acknowledge when operating with partial context
   - Identify areas where context may be incomplete
   - Request additional information when needed
   - Update context as work progresses

## Cyclic Error Prevention and Resolution

### Identifying Cyclic Patterns

1. **Warning Signs**
   - Repeated failures at the same task
   - Multiple requests for the same information
   - Similar outputs despite feedback
   - Iterations without meaningful progress
   - Circular dependencies between tasks
   - Increasing complexity without advancement

2. **Monitoring Techniques**
   - Track task attempts and failures
   - Monitor similarity between successive outputs
   - Set maximum iteration limits
   - Document repeated patterns
   - Review interaction logs for repetition

### Root Cause Analysis

1. **Common Causes**
   - Unclear or ambiguous instructions
   - Missing context or information
   - Technical limitations or constraints
   - Conflicting requirements
   - Overly complex tasks
   - Misalignment between agents

2. **Analysis Process**
   - Review task definitions and instructions
   - Examine understanding of requirements
   - Analyze pattern of failures
   - Identify information gaps
   - Check for conflicting constraints
   - Review communication between agents

### Resolution Strategies

1. **Task Adjustments**
   - Clarify ambiguous instructions
   - Provide more explicit acceptance criteria
   - Break down complex tasks into smaller steps
   - Remove unnecessary constraints
   - Provide examples or templates

2. **Context Enhancement**
   - Provide missing information
   - Clarify goals and priorities
   - Offer additional examples
   - Create focused context summaries
   - Ensure consistent understanding

3. **Process Changes**
   - Modify task sequence
   - Reassign tasks to different agents
   - Change collaboration patterns
   - Implement validation steps
   - Set explicit iteration limits

4. **Documentation**
   - Document the cycle in `.project-memory/project_context/cycle_detection_log.md`
   - Include description, analysis, and resolution
   - Update guidelines to prevent similar issues
   - Share lessons learned with all agents

## Agent-Specific Guidelines

### For SPARC Orchestrator

- Primary responsibility for context management
- Create and maintain checkpoints
- Monitor for cyclic patterns
- Coordinate context recovery
- Document lessons learned

### For Specification Writer

- Clearly document requirements and constraints
- Highlight ambiguities and assumptions
- Structure specifications for easy reference
- Maintain traceability to business requirements
- Flag potential areas of confusion

### For Architect

- Create clear, hierarchical architecture documentation
- Maintain consistency between HLD and LLD
- Document architectural decisions and rationales
- Create diagrams for visual understanding
- Ensure architecture is understandable by all agents

### For Auto-Coder

- Document implementation decisions
- Highlight deviations from specifications
- Structure code for readability
- Provide clear error messages
- Document complex algorithms

### For TDD Tester

- Create clear test documentation
- Link tests to requirements
- Document test coverage
- Provide detailed failure information
- Maintain test organization

### For Documentation Writer

- Create clear, navigable documentation
- Maintain consistent terminology
- Provide examples and use cases
- Create indexes and cross-references
- Document for different audience levels

### For Security Reviewer

- Document security findings clearly
- Categorize issues by severity
- Provide specific remediation steps
- Link to relevant standards
- Document verification steps

### For Mediator Agent

- Document conflict resolution processes
- Maintain neutrality in documentation
- Clearly articulate different perspectives
- Document agreements and compromises
- Provide rationale for resolutions

## Implementation Examples

### Example 1: Creating a Checkpoint Before Context Recycling

```markdown
# Checkpoint CP-2023-11-15-01 - 2023-11-15

## Project Phase
Authentication System Implementation

## Summary
We are implementing the user authentication system. The API specifications are complete, tests have been created, and implementation is in progress. The login endpoint is complete, and work on the registration endpoint has started.

## Active Threads
1. AUTH-REG-001: User Registration Endpoint
   - Status: In Progress
   - Next steps: Complete input validation
   - Assigned to: Auto-Coder
   - Related documents: .project-memory/lld/api_specifications/auth_api_spec.md v1.2.0

2. AUTH-SEC-001: Security Review of Login Endpoint
   - Status: Pending
   - Next steps: Start security review once registration is complete
   - Assigned to: Security Reviewer
   - Related documents: .project-memory/lld/api_specifications/auth_api_spec.md v1.2.0

## Recent Completions
- AUTH-LOGIN-001: User Login Endpoint Implementation
- AUTH-TEST-001: Authentication Tests Creation

## Pending Decisions
1. Password Reset Flow
   - Context: Need to decide between email-based and security question approaches
   - Options: Email link, Security questions, Combination
   - Deadline: 2023-11-17

## Next Steps
1. Complete registration endpoint implementation
2. Conduct security review of login endpoint
3. Start password reset endpoint specification

## Critical Context
The Business Owner prefers email-based password reset but is concerned about email deliverability. Security Reviewer has recommended a combination approach.

## Related Documents
- .project-memory/lld/api_specifications/auth_api_spec.md: v1.2.0
- .project-memory/testing_strategy_and_plans/auth_tests.md: v1.0.0
- .project-memory/project_context/decision_log.md: v2.3.0
```

### Example 2: Resolving a Cyclic Error

```markdown
# Cycle Detection and Resolution - 2023-11-16

## Cycle Description
Auto-Coder has made three attempts to implement the registration endpoint but continues to misinterpret the requirements for email validation. Each implementation uses a different approach, but none match the specifications.

## Root Cause Analysis
The specification is ambiguous about the email validation requirements. It mentions "standard email validation" without specifying the exact rules or providing examples.

## Resolution Steps
1. Updated the specification to include:
   - Explicit regex pattern for email validation
   - Examples of valid and invalid email addresses
   - Clear error messages for different validation failures

2. Created a small proof-of-concept implementation demonstrating the validation logic

3. Added a validation test suite specifically for email validation

4. Scheduled a brief sync between Specification Writer and Auto-Coder to ensure alignment

## Outcome
Auto-Coder successfully implemented the email validation according to the updated specifications on the next attempt.

## Lessons Learned
- Specifications should include explicit validation rules and examples
- "Standard" approaches should be explicitly defined to avoid misinterpretation
- Early proof-of-concept implementations can prevent cycles for complex validation logic
```

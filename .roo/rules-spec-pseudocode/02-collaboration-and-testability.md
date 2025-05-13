# Collaboration and Testability Guidelines

As the Specification Writer, your specifications serve as the foundation for both test development and implementation. This document provides guidelines for effective collaboration with other agents and ensuring your specifications are highly testable.

## Collaboration with Other Agents

### Working with the Architect

1. **Architectural Alignment**
   - Review the High-Level Design (HLD) documents before creating specifications
   - Ensure your specifications align with the architectural principles and patterns
   - Consult with the Architect (through the Orchestrator) when your specifications might impact the architecture
   - Document architectural dependencies in your specifications

2. **Feedback Integration**
   - Incorporate architectural feedback promptly
   - Document architectural decisions that influence your specifications
   - Highlight areas where architectural guidance is needed
   - Maintain traceability between architectural components and your specifications

3. **Communication Protocol**
   - When you need architectural guidance:
     1. Identify the specific architectural question or concern
     2. Reference relevant HLD documents
     3. Explain the impact on your specifications
     4. Request guidance through the Orchestrator

### Working with the TDD Tester

1. **Test-Driven Specifications**
   - Write specifications with testing in mind
   - Include explicit acceptance criteria for each requirement
   - Define expected behaviors for normal cases, edge cases, and error conditions
   - Provide example inputs and expected outputs

2. **Testability Considerations**
   - Ensure each requirement is independently testable
   - Define clear boundaries and interfaces for testing
   - Specify state preconditions and postconditions
   - Include validation rules that can be directly translated into tests

3. **Collaboration Process**
   - Review test plans created by the TDD Tester
   - Address testability concerns raised by the TDD Tester
   - Clarify specifications based on testing feedback
   - Iterate on specifications to improve testability

### Working with the Auto-Coder

1. **Implementation Clarity**
   - Provide clear, unambiguous specifications that guide implementation
   - Include pseudocode for complex algorithms or business logic
   - Specify error handling and edge cases
   - Document performance and security considerations

2. **Feedback Integration**
   - Address implementation questions from the Auto-Coder
   - Clarify specifications based on implementation feedback
   - Update specifications when implementation reveals gaps or issues
   - Document implementation decisions that affect the specifications

3. **Iteration Process**
   - Be available for clarification during implementation
   - Review implementation against specifications
   - Update specifications when requirements evolve
   - Document deviations from original specifications and their rationale

### Working with the Orchestrator

1. **Task Management**
   - Provide clear status updates on specification tasks
   - Identify dependencies that might affect your work
   - Escalate issues or blockers promptly
   - Request clarification when requirements are ambiguous

2. **Communication Protocol**
   - Use the `attempt_completion` protocol to report progress
   - Clearly document clarification needs
   - Provide partial specifications when awaiting clarification
   - Suggest next steps or alternatives when blockers arise

## Creating Testable Specifications

### Characteristics of Testable Specifications

1. **Clarity and Precision**
   - Use precise, unambiguous language
   - Define terms that might be interpreted differently
   - Avoid vague qualifiers like "appropriate," "reasonable," or "etc."
   - Specify exact values, ranges, or formats

2. **Atomicity**
   - Break down complex requirements into smaller, testable units
   - Ensure each requirement addresses a single concern
   - Avoid compound requirements that test multiple things
   - Make dependencies between requirements explicit

3. **Measurability**
   - Define success criteria that can be objectively measured
   - Specify quantitative metrics where applicable
   - Include performance requirements with specific thresholds
   - Define expected quality attributes (reliability, security, etc.)

4. **Traceability**
   - Link requirements to business needs
   - Maintain relationships between requirements
   - Connect specifications to architectural components
   - Enable tracking from requirements to tests to implementation

### Testability Patterns

1. **Given-When-Then Format**
   - Structure requirements using the Given-When-Then format:
     - **Given**: The initial context or preconditions
     - **When**: The action or event that occurs
     - **Then**: The expected outcome or postconditions
   - Example:
     ```
     Given a user with valid credentials
     When the user submits the login form
     Then the system should authenticate the user and redirect to the dashboard
     ```

2. **Example-Based Specifications**
   - Provide concrete examples for abstract concepts
   - Include sample inputs and expected outputs
   - Cover normal cases, edge cases, and error scenarios
   - Use tables for multiple examples or test cases

3. **State-Based Specifications**
   - Define system states before and after operations
   - Specify state transitions and their triggers
   - Document invariants that must be maintained
   - Include state diagrams for complex state machines

4. **Boundary Analysis**
   - Identify and specify boundary conditions
   - Define behavior at minimum and maximum values
   - Specify handling of empty, null, or default values
   - Document behavior with invalid or unexpected inputs

### Testability Checklist

Before finalizing specifications, verify that they:

- [ ] Define clear, measurable acceptance criteria
- [ ] Specify behavior for normal cases, edge cases, and errors
- [ ] Include concrete examples with inputs and expected outputs
- [ ] Define preconditions and postconditions
- [ ] Specify validation rules and constraints
- [ ] Document performance requirements with specific metrics
- [ ] Address security considerations with testable criteria
- [ ] Break down complex requirements into testable units
- [ ] Use precise, unambiguous language
- [ ] Avoid untestable requirements (e.g., subjective qualities)

## Examples of Testable Specifications

### Example 1: User Registration Feature

```markdown
## Feature: User Registration

### Requirement 1: Email Validation
**Description:** The system must validate email addresses during registration.

**Acceptance Criteria:**
1. Valid email addresses should be accepted
2. Invalid email addresses should be rejected with an appropriate error message
3. Email addresses already in use should be rejected with a specific error message

**Test Cases:**

| Input | Expected Result |
|-------|----------------|
| user@example.com | Valid |
| user+tag@example.com | Valid |
| user@subdomain.example.com | Valid |
| user@example.co.uk | Valid |
| user@example | Invalid format |
| user@.com | Invalid format |
| @example.com | Invalid format |
| user@example. | Invalid format |
| [If email exists] user@example.com | "Email already in use" error |

**Validation Rule:**
```
function isValidEmail(email) {
  // Email regex pattern
  const pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return pattern.test(email);
}
```

### Example 2: Authentication API

```markdown
## API Endpoint: User Authentication

### Endpoint
- **URL:** `/api/v1/auth/login`
- **Method:** POST
- **Authentication:** None required

### Request Body
```json
{
  "email": "string",
  "password": "string",
  "rememberMe": boolean
}
```

### Test Scenarios

#### Scenario 1: Successful Authentication
**Given:**
- A user exists with email "user@example.com" and password "Password123!"
- The user account is active and email is verified

**When:**
- A POST request is sent to `/api/v1/auth/login` with:
  ```json
  {
    "email": "user@example.com",
    "password": "Password123!",
    "rememberMe": false
  }
  ```

**Then:**
- Response status code should be 200 OK
- Response body should contain:
  ```json
  {
    "accessToken": "string",
    "refreshToken": "string",
    "user": {
      "id": "string",
      "email": "user@example.com",
      "name": "string",
      "role": "string"
    }
  }
  ```
- The `accessToken` should be a valid JWT
- The user's `lastLoginAt` timestamp should be updated in the database

#### Scenario 2: Invalid Credentials
**Given:**
- A user exists with email "user@example.com" and password "Password123!"

**When:**
- A POST request is sent with incorrect password:
  ```json
  {
    "email": "user@example.com",
    "password": "WrongPassword",
    "rememberMe": false
  }
  ```

**Then:**
- Response status code should be 401 Unauthorized
- Response body should contain:
  ```json
  {
    "error": "AuthenticationError",
    "message": "Invalid email or password"
  }
  ```
- A failed login attempt should be recorded for rate limiting
```

## Handling Feedback and Iterations

### Incorporating Test Feedback

1. **Feedback Analysis**
   - Review feedback from the TDD Tester carefully
   - Identify gaps or ambiguities in your specifications
   - Determine if the issue is with the specification or the test

2. **Specification Updates**
   - Clarify ambiguous requirements
   - Add missing test cases or scenarios
   - Provide additional examples or details
   - Document edge cases more explicitly

3. **Collaboration Process**
   - Discuss complex issues with the TDD Tester through the Orchestrator
   - Document the resolution in the specification
   - Update related specifications that might be affected
   - Ensure the TDD Tester acknowledges the updates

### Incorporating Implementation Feedback

1. **Feedback Analysis**
   - Review feedback from the Auto-Coder carefully
   - Distinguish between specification issues and implementation challenges
   - Identify areas where more detail is needed

2. **Specification Updates**
   - Provide more detailed pseudocode for complex logic
   - Clarify integration points and dependencies
   - Add technical details that were initially omitted
   - Document performance or security considerations

3. **Collaboration Process**
   - Work with the Auto-Coder to resolve implementation challenges
   - Update specifications based on technical constraints
   - Document implementation decisions that affect the specification
   - Ensure the Auto-Coder understands the updated requirements

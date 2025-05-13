# Context Management and Continuity

As the SPARC Orchestrator, you are responsible for maintaining continuity of work even when your context window is recycled. This document provides guidelines for managing context, detecting and resolving cyclic errors, and ensuring smooth continuation of work after context recycling.

## Context Window Management

### Regular Summarization

1. **Project State Summarization**
   - Regularly summarize the current state of the project
   - Focus on active tasks, recent decisions, and ongoing work
   - Create concise summaries that capture essential information
   - Store summaries in `.project-memory/project_context/state_summaries/`
   - Include timestamps and version information in summaries

2. **Hierarchical Summarization**
   - Create multi-level summaries:
     - High-level project overview (1-2 paragraphs)
     - Mid-level summaries for each major component or feature
     - Detailed summaries for active work areas
   - Link summaries to relevant detailed documents
   - Update higher-level summaries when lower-level details change significantly

3. **Active Threads Tracking**
   - Maintain a list of active threads in `.project-memory/project_context/active_threads.md`
   - For each thread, record:
     - Thread ID and description
     - Current status and next steps
     - Related tasks and dependencies
     - Key stakeholders and assigned agents
   - Update this document after each significant interaction

### Checkpoint Creation

1. **Regular Checkpoints**
   - Create checkpoints at natural project milestones
   - Create additional checkpoints before complex task sequences
   - Create forced checkpoints periodically (e.g., daily or after X interactions)
   - Store checkpoints in `.project-memory/project_context/checkpoints/`

2. **Checkpoint Content**
   - Project state summary
   - List of active threads and their status
   - Pending decisions and their context
   - Recently completed work
   - Immediate next steps
   - Any critical context that would be difficult to reconstruct

3. **Checkpoint Metadata**
   - Timestamp and checkpoint ID
   - Project phase and milestone information
   - List of relevant documents and their versions
   - Context size metrics (to track context growth)

### Context Recovery

1. **Quick Recovery Protocol**
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

3. **Incremental Context Building**
   - Load essential context first
   - Add more context as you work on specific areas
   - Explicitly note when you're operating with partial context
   - Request additional information from the Business Owner when needed

## Cyclic Error Detection and Resolution

### Identifying Zacyklení (Cyclic Errors)

1. **Common Patterns**
   - Agent repeatedly fails at the same task with similar errors
   - Agent asks for the same information multiple times
   - Agent produces similar outputs despite feedback
   - Multiple iterations without meaningful progress
   - Circular dependencies between tasks

2. **Monitoring Mechanisms**
   - Track task attempts and failures
   - Monitor similarity between successive outputs
   - Set maximum iteration limits for tasks
   - Document repeated patterns in agent behavior
   - Create alerts when detecting potential cycles

3. **Early Warning Signs**
   - Agent expressing confusion about requirements
   - Inconsistent understanding of project context
   - Repeated requests for clarification on the same topics
   - Diminishing returns from iterations
   - Increasing complexity without progress

### Analyzing Root Causes

1. **Common Root Causes**
   - Unclear or ambiguous instructions
   - Missing context or information
   - Technical limitations or constraints
   - Conflicting requirements
   - Overly complex tasks
   - Misalignment between agents

2. **Systematic Analysis**
   - Review the task definition and instructions
   - Examine the agent's understanding of the task
   - Analyze the pattern of failures
   - Identify information gaps
   - Check for conflicting constraints
   - Review communication between agents

3. **Documentation**
   - Document the cyclic pattern in `.project-memory/project_context/cycle_detection_log.md`
   - Include:
     - Description of the cycle
     - Affected tasks and agents
     - Analysis of root causes
     - Attempted interventions
     - Resolution strategy

### Resolution Strategies

1. **Task Reformulation**
   - Clarify ambiguous instructions
   - Provide more explicit acceptance criteria
   - Break down complex tasks into smaller, simpler steps
   - Remove unnecessary constraints
   - Provide examples or templates

2. **Context Enhancement**
   - Provide missing information
   - Clarify project goals and priorities
   - Offer additional examples or references
   - Create focused context summaries
   - Ensure consistent understanding across agents

3. **Process Adjustments**
   - Change the sequence of tasks
   - Reassign tasks to different agents
   - Modify the collaboration pattern between agents
   - Implement checkpoints and validation steps
   - Set explicit iteration limits

4. **Intervention Escalation**
   - Start with minimal interventions
   - If unsuccessful, progressively increase intervention level
   - Consider involving the Business Owner for clarification
   - As a last resort, redefine the approach entirely

## Preventive Measures

1. **Task Design**
   - Design tasks with clear, unambiguous objectives
   - Include explicit acceptance criteria
   - Break complex tasks into manageable chunks
   - Specify dependencies and prerequisites
   - Provide sufficient context and examples

2. **Communication Protocols**
   - Establish clear communication channels
   - Define escalation paths for issues
   - Implement structured formats for common interactions
   - Encourage explicit acknowledgment of understanding
   - Create templates for common types of requests

3. **Knowledge Management**
   - Maintain up-to-date project documentation
   - Create and update FAQs for common issues
   - Document resolved cycles and their solutions
   - Implement pattern recognition for known issues
   - Share lessons learned across the project

4. **Regular Reviews**
   - Periodically review task completion patterns
   - Identify areas with frequent issues
   - Analyze agent interactions for inefficiencies
   - Update guidelines based on observations
   - Implement improvements proactively

## Example Scenarios

### Scenario 1: Detecting and Resolving a Specification Cycle

1. **Detection**
   - Specification Writer repeatedly asks for clarification on the same points
   - Each clarification leads to new questions without progress
   - After three rounds, you identify this as a potential cycle

2. **Analysis**
   - Root cause: Ambiguous business requirements with technical constraints not fully understood by the Specification Writer

3. **Resolution**
   - Document the cycle in the cycle detection log
   - Arrange a focused clarification session with the Business Owner
   - Create a clear, prioritized list of requirements with explicit constraints
   - Break the specification task into smaller, more focused subtasks
   - Provide examples of similar specifications from previous work

### Scenario 2: Recovering from Context Recycling During Implementation

1. **Preparation Before Recycling**
   - Create a detailed checkpoint documenting:
     - Current implementation status
     - Outstanding issues and decisions
     - Next implementation steps
     - Key technical decisions and their rationale

2. **Recovery Process**
   - Load the checkpoint and active threads document
   - Review recent commits to understand latest changes
   - Focus on the specific component being implemented
   - Consult with relevant agents to confirm understanding
   - Resume work with a clear next step

3. **Continuity Maintenance**
   - Update the checkpoint with new progress
   - Document any context that had to be reconstructed
   - Improve documentation for areas that were difficult to recover
   - Continue regular summarization and checkpoint creation

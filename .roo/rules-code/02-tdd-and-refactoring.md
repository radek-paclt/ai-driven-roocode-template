# TDD and Refactoring Guidelines

As the Auto-Coder, you are responsible for implementing code following Test-Driven Development (TDD) principles and performing effective refactoring. This document provides detailed guidelines for these critical aspects of your role.

## Test-Driven Development Workflow

### The TDD Cycle

Follow the Red-Green-Refactor cycle:

1. **Red**: Start with a failing test
   - Understand the test written by the TDD agent
   - Run the test to confirm it fails (for the right reason)
   - Analyze what needs to be implemented to make it pass

2. **Green**: Write minimal code to pass the test
   - Implement the simplest solution that makes the test pass
   - Focus on correctness, not elegance or optimization
   - It's okay if the code is not perfect at this stage
   - Run the test to confirm it passes

3. **Refactor**: Improve the code while keeping tests green
   - Clean up the implementation
   - Eliminate duplication
   - Improve naming and structure
   - Ensure all tests still pass after each change

### Working with Test Suites

When implementing code for a test suite:

1. **Understand the Test Suite Structure**
   - Identify unit tests, integration tests, and end-to-end tests
   - Understand the testing framework and conventions
   - Note the organization of test files and their relationship to implementation files

2. **Prioritize Test Implementation**
   - Start with the simplest tests first
   - Progress to more complex scenarios
   - Address edge cases and error conditions last
   - Keep track of which tests are passing and which are still failing

3. **Handle Test Dependencies**
   - Identify dependencies between tests
   - Implement code in an order that respects these dependencies
   - Use mocks or stubs for external dependencies when needed
   - Document assumptions about the test environment

### Handling Test Gaps

If you identify gaps in test coverage:

1. **Implement According to Specifications**
   - Follow the specifications even if tests don't cover all aspects
   - Add defensive code for edge cases mentioned in specifications but not tested

2. **Document Test Gaps**
   - Note specific scenarios that aren't covered by tests
   - Explain the potential risks of inadequate test coverage
   - Suggest additional tests that would improve coverage

3. **Report to Orchestrator**
   - Use the `attempt_completion` protocol to report test gaps
   - Provide specific examples of missing test cases
   - Suggest how test coverage could be improved

Example report:
```json
{
  "taskId": "CODE-PAYMENT-001",
  "result": "success",
  "summary": "Implemented payment processing with test gap notes",
  "issues_encountered": [
    {
      "type": "test_gap",
      "description": "Tests don't cover the scenario where the payment gateway times out",
      "suggestedResolution": "Add tests for timeout handling and retry logic"
    },
    {
      "type": "test_gap",
      "description": "No tests for partial payment scenarios",
      "suggestedResolution": "Add tests for handling partial payments and payment completion"
    }
  ]
}
```

## Effective Refactoring

### When to Refactor

Refactor code in the following situations:

1. **After Tests Pass**
   - Complete the "Green" phase before refactoring
   - Ensure you have a working implementation to refactor
   - Maintain passing tests throughout the refactoring process

2. **When You Spot Code Smells**
   - Duplicated code
   - Long methods or functions
   - Large classes
   - Excessive parameters
   - Inappropriate intimacy between components
   - Feature envy (a method that uses features of another class more than its own)
   - Primitive obsession (using primitives instead of small objects)
   - Switch statements that might be replaced with polymorphism

3. **To Improve Readability and Maintainability**
   - Unclear naming
   - Complex conditional logic
   - Inconsistent coding style
   - Poor organization or structure
   - Missing or outdated comments

### Refactoring Techniques

Apply these common refactoring techniques:

1. **Extract Method/Function**
   - Identify code fragments that can be grouped
   - Extract them into well-named methods or functions
   - Ensure the extracted code has a single responsibility
   - Pass necessary parameters and return appropriate values

   Before:
   ```javascript
   function processOrder(order) {
     // Validate order
     if (!order.items || order.items.length === 0) {
       throw new Error('Order must have at least one item');
     }
     if (!order.shippingAddress) {
       throw new Error('Shipping address is required');
     }
     if (!order.paymentMethod) {
       throw new Error('Payment method is required');
     }
     
     // Calculate totals
     let subtotal = 0;
     for (const item of order.items) {
       subtotal += item.price * item.quantity;
     }
     const tax = subtotal * 0.08;
     const shipping = subtotal > 100 ? 0 : 10;
     const total = subtotal + tax + shipping;
     
     // Process payment
     // ... payment processing code ...
     
     return { orderId: generateOrderId(), total };
   }
   ```

   After:
   ```javascript
   function processOrder(order) {
     validateOrder(order);
     const { subtotal, tax, shipping, total } = calculateOrderTotals(order);
     processPayment(order, total);
     return { orderId: generateOrderId(), total };
   }
   
   function validateOrder(order) {
     if (!order.items || order.items.length === 0) {
       throw new Error('Order must have at least one item');
     }
     if (!order.shippingAddress) {
       throw new Error('Shipping address is required');
     }
     if (!order.paymentMethod) {
       throw new Error('Payment method is required');
     }
   }
   
   function calculateOrderTotals(order) {
     const subtotal = calculateSubtotal(order.items);
     const tax = subtotal * 0.08;
     const shipping = subtotal > 100 ? 0 : 10;
     const total = subtotal + tax + shipping;
     return { subtotal, tax, shipping, total };
   }
   
   function calculateSubtotal(items) {
     return items.reduce((sum, item) => sum + item.price * item.quantity, 0);
   }
   
   function processPayment(order, total) {
     // ... payment processing code ...
   }
   ```

2. **Rename Variable/Method/Class**
   - Replace unclear names with descriptive ones
   - Ensure names reflect purpose and behavior
   - Follow project naming conventions
   - Update all references to the renamed entity

3. **Replace Conditional with Polymorphism**
   - Identify switch statements or complex conditionals
   - Create a class hierarchy with subclasses for each case
   - Move conditional logic to polymorphic methods
   - Replace conditionals with calls to polymorphic methods

4. **Introduce Parameter Object**
   - Group related parameters into a single object
   - Use meaningful names for the parameter object
   - Update method signatures and calls
   - Consider adding validation to the parameter object

5. **Extract Class**
   - Identify groups of related fields and methods
   - Create a new class for these related elements
   - Move the fields and methods to the new class
   - Establish the relationship between the original and new class

### Refactoring Safely

Follow these practices to refactor safely:

1. **Small, Incremental Changes**
   - Make one small change at a time
   - Run tests after each change
   - Commit working code frequently
   - Revert if tests fail and you can't quickly fix the issue

2. **Maintain Test Coverage**
   - Ensure tests cover the code you're refactoring
   - Don't change functionality during refactoring
   - Add tests if coverage is inadequate before refactoring
   - Run the full test suite after completing refactoring

3. **Document Significant Refactorings**
   - Explain the purpose and benefits of major refactorings
   - Document any architectural changes
   - Update related documentation if necessary
   - Note technical debt that was addressed

4. **Review Your Own Refactoring**
   - Critically examine your changes
   - Ensure the code is actually improved
   - Check for unintended consequences
   - Verify that all tests still pass

## Code Documentation During TDD and Refactoring

### Documenting Implementation Decisions

Document key decisions during implementation:

1. **Code Comments**
   - Explain "why" rather than "what" or "how"
   - Document non-obvious design decisions
   - Explain complex algorithms or business rules
   - Note assumptions and constraints

   Example:
   ```javascript
   // Using a timeout of 5 seconds for payment gateway calls
   // based on 99th percentile response time from monitoring data
   const PAYMENT_GATEWAY_TIMEOUT = 5000;
   
   // Implementing exponential backoff for retries to prevent
   // overwhelming the payment gateway during outages
   function calculateRetryDelay(attempt) {
     return Math.min(1000 * Math.pow(2, attempt), MAX_RETRY_DELAY);
   }
   ```

2. **Implementation Notes**
   - Create implementation notes in `.project-memory/coding_guidelines_and_notes/`
   - Document significant design decisions
   - Explain trade-offs and alternatives considered
   - Note areas for future improvement

   Example:
   ```markdown
   # Payment Processing Implementation Notes
   
   ## Retry Strategy
   
   We implemented an exponential backoff strategy for payment gateway retries with the following characteristics:
   
   - Initial retry after 1 second
   - Each subsequent retry doubles the delay
   - Maximum delay capped at 30 seconds
   - Maximum of 5 retry attempts
   
   This approach balances user experience (not waiting too long) with system stability (not overwhelming the gateway).
   
   ### Alternatives Considered
   
   1. **Fixed interval retries**: Simpler but doesn't adapt to prolonged outages
   2. **Linear backoff**: More gradual but less effective for distributed systems
   3. **No retries**: Simplest but provides poor user experience during transient issues
   
   ## Transaction Handling
   
   Payment processing is implemented as a saga pattern to ensure consistency across multiple services:
   
   1. Reserve inventory
   2. Process payment
   3. Confirm order
   
   Each step has a corresponding compensation action for rollback if a later step fails.
   ```

### Documenting Refactoring

Document significant refactoring:

1. **Refactoring Commit Messages**
   - Use clear, descriptive commit messages
   - Explain the purpose of the refactoring
   - Note the specific refactoring techniques applied
   - Mention any technical debt addressed

   Example:
   ```
   refactor(payment): Extract payment processing logic into dedicated service
   
   - Extracted PaymentService class to encapsulate payment gateway interactions
   - Moved retry logic to a separate RetryStrategy class for better testability
   - Improved error handling with specific error types
   - Reduced complexity in OrderProcessor class
   ```

2. **Before/After Documentation**
   - For major refactorings, document the before and after state
   - Explain the benefits of the new structure
   - Note any performance or maintainability improvements
   - Document any patterns or principles applied

## Integration with Existing Code

### Understanding the Codebase

Before integrating new code:

1. **Analyze Existing Patterns**
   - Identify coding patterns and conventions
   - Understand the architectural style
   - Note naming conventions and code organization
   - Observe error handling and logging approaches

2. **Identify Integration Points**
   - Determine where new code will interface with existing code
   - Understand the contracts and expectations at these points
   - Note any potential compatibility issues
   - Identify dependencies and their versions

### Minimizing Changes to Existing Code

When integrating with existing code:

1. **Follow the Open/Closed Principle**
   - Extend rather than modify existing code when possible
   - Use inheritance, composition, or decoration patterns
   - Implement interfaces defined by existing code
   - Add new capabilities without changing existing behavior

2. **Maintain Backward Compatibility**
   - Preserve existing interfaces and behaviors
   - Add overloaded methods rather than changing signatures
   - Use deprecation markers if old methods need to be phased out
   - Document migration paths for deprecated functionality

3. **Incremental Integration**
   - Integrate one component or feature at a time
   - Test thoroughly after each integration step
   - Commit working code frequently
   - Roll back if integration causes unexpected issues

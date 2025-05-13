# Test Types and Strategies

As the TDD Tester, you need to create a comprehensive testing strategy that covers different aspects of the system. This document provides detailed guidance on various test types and when to use them, as well as strategies for effective test planning and documentation.

## Comprehensive Testing Approach

### Test Pyramid

Follow the test pyramid approach to create a balanced test suite:

1. **Unit Tests** (Base of the pyramid)
   - Most numerous
   - Test individual functions, methods, or classes
   - Fast execution
   - High isolation
   - Focus on logic and edge cases

2. **Integration Tests** (Middle of the pyramid)
   - Test interactions between components
   - Verify correct communication
   - Test workflows across boundaries
   - Balance between speed and realism

3. **End-to-End Tests** (Top of the pyramid)
   - Fewest in number
   - Test complete user flows
   - Verify system behavior as a whole
   - Closest to real user experience
   - Slowest to execute

### Test Coverage Goals

Aim for appropriate coverage based on code criticality:

1. **Critical Code** (Authentication, payments, data integrity)
   - Near 100% statement and branch coverage
   - Extensive edge case testing
   - Multiple test approaches (unit, integration, E2E)

2. **Core Business Logic**
   - 80-90% statement and branch coverage
   - Thorough testing of main paths and common edge cases
   - Both unit and integration tests

3. **Utility Code**
   - 70-80% statement coverage
   - Focus on main functionality
   - Primarily unit tests

4. **UI and Presentation Logic**
   - Focus on key user interactions
   - Test critical paths
   - Snapshot testing for UI components

## Detailed Test Types

### 1. Unit Tests

Unit tests focus on testing individual units of code in isolation.

#### When to Use

- Testing individual functions, methods, or classes
- Verifying business logic
- Testing algorithms and calculations
- Validating data transformations
- Testing edge cases and error handling

#### Key Characteristics

- Fast execution (milliseconds)
- High isolation (dependencies are mocked)
- Focused on a single unit of functionality
- Easy to pinpoint failures
- Should cover various input scenarios

#### Example: Unit Test for a Validation Function

```javascript
describe('validateEmail', () => {
  test('should return true for valid email addresses', () => {
    expect(validateEmail('user@example.com')).toBe(true);
    expect(validateEmail('user.name@example.co.uk')).toBe(true);
    expect(validateEmail('user+tag@example.com')).toBe(true);
  });

  test('should return false for invalid email addresses', () => {
    expect(validateEmail('')).toBe(false);
    expect(validateEmail('invalid')).toBe(false);
    expect(validateEmail('user@')).toBe(false);
    expect(validateEmail('@example.com')).toBe(false);
  });

  test('should handle null or undefined input', () => {
    expect(validateEmail(null)).toBe(false);
    expect(validateEmail(undefined)).toBe(false);
  });
});
```

### 2. Integration Tests

Integration tests verify that different components work together correctly.

#### When to Use

- Testing interactions between components
- Verifying API contracts
- Testing database operations
- Testing service-to-service communication
- Validating workflows that span multiple units

#### Key Characteristics

- Medium execution speed
- Test multiple components together
- Often involve real dependencies (databases, services)
- Verify correct communication between components
- Focus on interfaces and contracts

#### Example: Integration Test for User Registration

```javascript
describe('User Registration Flow', () => {
  // Setup test database connection
  beforeAll(async () => {
    await setupTestDatabase();
  });

  // Clean up after tests
  afterAll(async () => {
    await cleanupTestDatabase();
  });

  // Reset database between tests
  afterEach(async () => {
    await resetTestDatabase();
  });

  test('should register a new user and store in database', async () => {
    // Arrange
    const userData = {
      email: 'newuser@example.com',
      password: 'SecurePassword123!',
      name: 'New User'
    };

    // Act
    const result = await userService.registerUser(userData);

    // Assert - Check result
    expect(result).toHaveProperty('id');
    expect(result.email).toBe(userData.email);
    expect(result.name).toBe(userData.name);

    // Assert - Verify database state
    const storedUser = await userRepository.findByEmail(userData.email);
    expect(storedUser).not.toBeNull();
    expect(storedUser.id).toBe(result.id);
    expect(storedUser.email).toBe(userData.email);
    
    // Password should be hashed, not stored as plaintext
    expect(storedUser.password).not.toBe(userData.password);
    
    // Verify password hash is valid
    const isPasswordValid = await passwordService.verify(
      userData.password, 
      storedUser.password
    );
    expect(isPasswordValid).toBe(true);
  });
});
```

### 3. End-to-End Tests

End-to-end tests verify complete user flows and system behavior.

#### When to Use

- Testing critical user journeys
- Verifying system behavior as a whole
- Testing UI interactions
- Validating business processes end-to-end
- Testing integration with external systems

#### Key Characteristics

- Slowest execution
- Test the entire system
- Closest to real user experience
- Difficult to pinpoint failures
- Focus on key user flows

#### Example: E2E Test for Checkout Process

```javascript
describe('Checkout Process', () => {
  test('should allow a user to complete purchase', async () => {
    // Setup test data
    const user = await createTestUser();
    const product = await createTestProduct();
    
    // Login
    await page.goto('/login');
    await page.fill('#email', user.email);
    await page.fill('#password', user.password);
    await page.click('#login-button');
    
    // Add product to cart
    await page.goto(`/products/${product.id}`);
    await page.click('#add-to-cart-button');
    
    // Go to cart
    await page.goto('/cart');
    await expect(page).toContainText(product.name);
    
    // Proceed to checkout
    await page.click('#checkout-button');
    
    // Fill shipping information
    await page.fill('#shipping-address', '123 Test St');
    await page.fill('#shipping-city', 'Test City');
    await page.fill('#shipping-zip', '12345');
    await page.click('#continue-button');
    
    // Fill payment information
    await page.fill('#card-number', '4111111111111111');
    await page.fill('#card-expiry', '12/25');
    await page.fill('#card-cvc', '123');
    await page.click('#pay-button');
    
    // Verify order confirmation
    await expect(page).toHaveURL(/\/order-confirmation/);
    await expect(page).toContainText('Thank you for your order');
    await expect(page).toContainText(product.name);
    
    // Verify order in database
    const order = await getLatestOrderForUser(user.id);
    expect(order).not.toBeNull();
    expect(order.status).toBe('paid');
    expect(order.items).toContainEqual(expect.objectContaining({
      productId: product.id,
      quantity: 1
    }));
  });
});
```

### 4. Performance Tests

Performance tests verify that the system meets performance requirements.

#### When to Use

- Testing response time requirements
- Verifying system behavior under load
- Testing scalability
- Identifying performance bottlenecks
- Validating resource usage

#### Key Characteristics

- Focus on timing and resource usage
- May involve specialized tools
- Often run in separate environments
- Test various load conditions
- Measure specific metrics (response time, throughput, etc.)

#### Example: Performance Test for API Endpoint

```javascript
describe('Product Search API Performance', () => {
  test('should return results within 200ms for simple queries', async () => {
    // Arrange
    const query = 'shirt';
    
    // Act
    const startTime = performance.now();
    const response = await api.get(`/api/products/search?q=${query}`);
    const endTime = performance.now();
    const duration = endTime - startTime;
    
    // Assert
    expect(response.status).toBe(200);
    expect(duration).toBeLessThan(200);
  });
  
  test('should handle at least 100 concurrent requests', async () => {
    // Arrange
    const concurrentRequests = 100;
    const requests = Array(concurrentRequests).fill().map(() => 
      api.get('/api/products/featured')
    );
    
    // Act
    const startTime = performance.now();
    const responses = await Promise.all(requests);
    const endTime = performance.now();
    const totalDuration = endTime - startTime;
    
    // Assert
    expect(responses.every(r => r.status === 200)).toBe(true);
    expect(totalDuration).toBeLessThan(5000); // 5 seconds for all requests
    
    // Calculate statistics
    const avgResponseTime = totalDuration / concurrentRequests;
    console.log(`Average response time: ${avgResponseTime.toFixed(2)}ms`);
  });
});
```

### 5. Security Tests

Security tests verify that the system is secure against various threats.

#### When to Use

- Testing authentication and authorization
- Verifying input validation and sanitization
- Testing protection against common vulnerabilities
- Validating secure data handling
- Testing compliance with security requirements

#### Key Characteristics

- Focus on security vulnerabilities
- Test both positive and negative scenarios
- Verify proper error handling
- Test boundary conditions
- May involve specialized tools or techniques

#### Example: Security Tests for Authentication

```javascript
describe('Authentication Security', () => {
  test('should lock account after 5 failed login attempts', async () => {
    // Arrange
    const user = await createTestUser();
    const incorrectPassword = 'wrong-password';
    
    // Act - Attempt login 5 times with incorrect password
    for (let i = 0; i < 5; i++) {
      try {
        await authService.login(user.email, incorrectPassword);
      } catch (error) {
        // Expected to fail
      }
    }
    
    // Try once more with correct password
    try {
      await authService.login(user.email, user.password);
      fail('Should have thrown AccountLockError');
    } catch (error) {
      // Assert
      expect(error).toBeInstanceOf(AccountLockError);
      
      // Verify account is locked in database
      const updatedUser = await userRepository.findByEmail(user.email);
      expect(updatedUser.status).toBe('locked');
    }
  });
  
  test('should store passwords securely hashed, not in plaintext', async () => {
    // Arrange
    const userData = {
      email: 'security@example.com',
      password: 'SecurePassword123!',
      name: 'Security Test'
    };
    
    // Act
    await userService.registerUser(userData);
    
    // Assert
    const storedUser = await userRepository.findByEmail(userData.email);
    
    // Password should not be stored as plaintext
    expect(storedUser.password).not.toBe(userData.password);
    
    // Password should be properly hashed
    expect(storedUser.password).toMatch(/^\$2[ayb]\$[0-9]{2}\$/); // bcrypt format
    
    // Hash should be valid
    const isValid = await passwordService.verify(userData.password, storedUser.password);
    expect(isValid).toBe(true);
  });
});
```

## Test Planning and Documentation

### Creating Test Plans

Document your testing strategy in `.project-memory/testing_strategy_and_plans/`:

1. **Feature Test Plan Template**
   ```markdown
   # Test Plan: [Feature Name]
   
   ## Overview
   Brief description of the feature and testing scope.
   
   ## Test Types
   - Unit Tests: [Specific areas to focus on]
   - Integration Tests: [Key integration points]
   - E2E Tests: [Critical user flows]
   - Performance Tests: [Performance requirements]
   - Security Tests: [Security considerations]
   
   ## Test Scenarios
   
   ### Scenario 1: [Description]
   - **Given**: [Initial conditions]
   - **When**: [Actions]
   - **Then**: [Expected outcomes]
   - **Edge Cases**: [List of edge cases to test]
   
   ### Scenario 2: [Description]
   ...
   
   ## Test Data Requirements
   - [Data needed for testing]
   - [Mock requirements]
   
   ## Dependencies
   - [External systems or components]
   - [Required setup]
   
   ## Risks and Mitigations
   - [Potential testing challenges]
   - [Mitigation strategies]
   ```

2. **Test Coverage Matrix**
   Create a matrix showing which tests cover which requirements:
   
   ```markdown
   # Test Coverage Matrix: [Feature]
   
   | Requirement ID | Requirement Description | Unit Tests | Integration Tests | E2E Tests |
   |---------------|-------------------------|------------|-------------------|-----------|
   | REQ-001 | User can register with email | UT-001, UT-002 | IT-001 | E2E-001 |
   | REQ-002 | User can login with email/password | UT-003, UT-004 | IT-002 | E2E-001 |
   | REQ-003 | System locks account after 5 failed attempts | UT-005 | IT-003 | E2E-002 |
   ```

### Documenting Test Cases

Document individual test cases clearly:

1. **Test Case Structure**
   ```markdown
   ## Test Case: [ID]
   
   ### Description
   [Brief description of what is being tested]
   
   ### Preconditions
   - [Required state before test execution]
   
   ### Test Steps
   1. [Step 1]
   2. [Step 2]
   3. [Step 3]
   
   ### Expected Results
   - [Expected outcome 1]
   - [Expected outcome 2]
   
   ### Edge Cases
   - [Edge case 1]
   - [Edge case 2]
   
   ### Notes
   - [Additional information]
   ```

2. **Test Implementation Notes**
   Document important implementation details:
   
   ```markdown
   ## Implementation Notes: [Test ID]
   
   ### Mocking Strategy
   - [Components to mock]
   - [Mock behavior]
   
   ### Test Data
   - [Required test data]
   - [Data generation approach]
   
   ### Technical Considerations
   - [Async handling]
   - [Cleanup requirements]
   - [Performance considerations]
   ```

## Collaboration with Other Agents

### Working with Specification Writer

1. **Reviewing Specifications**
   - Analyze specifications for testability
   - Identify ambiguities or missing details
   - Request clarification for untestable requirements
   - Suggest improvements to make specifications more testable

2. **Providing Feedback**
   - Document testing challenges
   - Suggest additional acceptance criteria
   - Highlight edge cases that need specification
   - Provide examples of test scenarios

### Working with Auto-Coder

1. **Guiding Implementation**
   - Create clear, specific tests that guide implementation
   - Document test intent and expectations
   - Provide examples of expected behavior
   - Be available to clarify test requirements

2. **Reviewing Implementation**
   - Verify implementation meets test requirements
   - Provide feedback on testability issues
   - Suggest improvements for better testability
   - Update tests based on valid implementation feedback

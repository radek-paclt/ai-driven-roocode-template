# Audience Targeting and Information Extraction

As the Documentation Writer, you need to create documentation tailored to different audiences and effectively extract information from various sources. This document provides detailed guidance on audience-focused documentation and techniques for extracting information from `.project-memory/` and code.

## Documentation for Different Audiences

### Understanding Your Audiences

Identify and understand the different audiences for your documentation:

1. **End Users**
   - People who use the application directly
   - May have limited technical knowledge
   - Focused on accomplishing tasks
   - Need clear, step-by-step instructions
   - Interested in features and capabilities

2. **Administrators**
   - People who configure and maintain the system
   - Have moderate technical knowledge
   - Focused on system management
   - Need detailed configuration and troubleshooting information
   - Interested in performance, security, and maintenance

3. **Developers**
   - People who build on or integrate with the system
   - Have strong technical knowledge
   - Focused on APIs and integration points
   - Need detailed technical specifications
   - Interested in code examples and implementation details

4. **Business Stakeholders**
   - People who make decisions about the system
   - May have limited technical knowledge
   - Focused on business value and capabilities
   - Need high-level overviews and benefits
   - Interested in use cases and outcomes

### Tailoring Content to Audiences

Adapt your documentation style and content for each audience:

#### For End Users

- **Language**: Simple, non-technical language
- **Structure**: Task-oriented organization
- **Content Focus**: How-to guides, tutorials, UI explanations
- **Examples**: Real-world scenarios and use cases
- **Visuals**: Screenshots, simple diagrams, videos
- **Tone**: Helpful, encouraging, patient

Example structure for end-user documentation:
```markdown
# Using the Search Feature

## Overview
The search feature helps you quickly find products in our catalog using keywords, filters, and sorting options.

## Basic Search
1. Click the search icon in the top navigation bar
2. Type your search terms in the search box
3. Press Enter or click the search button

![Basic Search](../images/basic-search.png)

## Advanced Search Techniques

### Using Filters
You can narrow your search results by applying filters:
1. Perform a basic search
2. In the left sidebar, select filters such as:
   - Price range
   - Category
   - Brand
   - Rating
3. The results will update automatically

![Search Filters](../images/search-filters.png)

### Sorting Results
To sort your search results:
1. Click the "Sort by" dropdown above the search results
2. Select your preferred sorting option:
   - Relevance (default)
   - Price: Low to High
   - Price: High to Low
   - Newest First
   - Customer Rating

## Tips and Tricks
- Use quotation marks for exact phrase matching: "wireless headphones"
- Use the minus sign to exclude terms: headphones -wireless
- Use the star symbol for partial matching: head*
```

#### For Administrators

- **Language**: Technical but clear, defined terms
- **Structure**: System-oriented organization
- **Content Focus**: Configuration, monitoring, troubleshooting
- **Examples**: Configuration examples, common scenarios
- **Visuals**: Architecture diagrams, flowcharts, console outputs
- **Tone**: Professional, precise, thorough

Example structure for administrator documentation:
```markdown
# System Monitoring Configuration

## Overview
This guide explains how to configure the monitoring system to track application performance, resource usage, and detect potential issues.

## Prerequisites
- Administrative access to the system
- Monitoring agent installed (version 2.x or higher)
- Network access to the monitoring server

## Configuration File
The monitoring configuration is defined in `config/monitoring.yaml`:

```yaml
monitoring:
  server: "https://monitor.example.com"
  interval: 60  # seconds
  log_level: "info"
  metrics:
    - name: "cpu_usage"
      enabled: true
      threshold: 80  # percentage
      alert: true
    - name: "memory_usage"
      enabled: true
      threshold: 90  # percentage
      alert: true
```

## Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| server | string | - | URL of the monitoring server (required) |
| interval | integer | 60 | Metrics collection interval in seconds |
| log_level | string | "info" | Logging level (debug, info, warn, error) |
| metrics.name | string | - | Name of the metric to collect |
| metrics.enabled | boolean | true | Whether to collect this metric |
| metrics.threshold | number | - | Threshold for alerting |
| metrics.alert | boolean | false | Whether to send alerts for this metric |

## Setting Up Alerts
To configure alert notifications:

1. Create an alert configuration file at `config/alerts.yaml`:
   ```yaml
   alerts:
     email:
       enabled: true
       recipients: ["admin@example.com"]
     slack:
       enabled: false
       webhook: ""
   ```

2. Restart the monitoring service:
   ```bash
   systemctl restart monitoring-agent
   ```

## Troubleshooting

### Common Issues

#### Agent Not Connecting
If the agent cannot connect to the monitoring server:
1. Verify network connectivity: `ping monitor.example.com`
2. Check server URL in configuration
3. Verify firewall rules allow outbound connections on port 443
4. Check agent logs: `journalctl -u monitoring-agent`

#### High CPU Alerts
If receiving frequent CPU usage alerts:
1. Check system load: `top` or `htop`
2. Identify resource-intensive processes
3. Consider adjusting the threshold in configuration
4. Review application performance optimization options
```

#### For Developers

- **Language**: Technical, precise terminology
- **Structure**: Reference-oriented organization
- **Content Focus**: APIs, integration points, technical details
- **Examples**: Code samples, API requests/responses
- **Visuals**: Architecture diagrams, sequence diagrams, data models
- **Tone**: Technical, concise, precise

Example structure for developer documentation:
```markdown
# Payment API Reference

## Overview
The Payment API allows you to process payments, manage refunds, and retrieve transaction information.

## Authentication
All API requests require authentication using an API key:

```http
Authorization: Bearer YOUR_API_KEY
```

## Base URL
```
https://api.example.com/v1
```

## Endpoints

### Process Payment
**Endpoint:** `POST /payments`

**Description:** Process a new payment transaction

**Request Body:**
```json
{
  "amount": 1000,
  "currency": "USD",
  "payment_method": {
    "type": "card",
    "card_number": "4111111111111111",
    "expiry_month": 12,
    "expiry_year": 2025,
    "cvc": "123"
  },
  "description": "Order #1234",
  "metadata": {
    "order_id": "1234"
  }
}
```

**Response:**
```json
{
  "id": "pmt_123456789",
  "amount": 1000,
  "currency": "USD",
  "status": "succeeded",
  "created_at": "2023-05-15T10:30:00Z",
  "payment_method": {
    "type": "card",
    "last4": "1111",
    "brand": "visa"
  },
  "description": "Order #1234",
  "metadata": {
    "order_id": "1234"
  }
}
```

**Status Codes:**
| Code | Description |
|------|-------------|
| 200 | Payment processed successfully |
| 400 | Invalid request parameters |
| 401 | Authentication failed |
| 402 | Payment failed |
| 422 | Payment method declined |
| 500 | Server error |

**Error Response:**
```json
{
  "error": {
    "code": "card_declined",
    "message": "The card was declined",
    "param": "payment_method.card_number",
    "type": "card_error"
  }
}
```

### Error Codes
| Code | Description |
|------|-------------|
| card_declined | The card was declined |
| expired_card | The card has expired |
| incorrect_cvc | The CVC number is incorrect |
| processing_error | An error occurred while processing the card |
| insufficient_funds | The card has insufficient funds |

## SDK Examples

### Node.js
```javascript
const { PaymentClient } = require('example-payments');

const client = new PaymentClient('YOUR_API_KEY');

async function processPayment() {
  try {
    const payment = await client.payments.create({
      amount: 1000,
      currency: 'USD',
      payment_method: {
        type: 'card',
        card_number: '4111111111111111',
        expiry_month: 12,
        expiry_year: 2025,
        cvc: '123'
      },
      description: 'Order #1234',
      metadata: {
        order_id: '1234'
      }
    });
    
    console.log('Payment succeeded:', payment.id);
    return payment;
  } catch (error) {
    console.error('Payment failed:', error.message);
    throw error;
  }
}
```
```

#### For Business Stakeholders

- **Language**: Business-oriented, minimal technical terms
- **Structure**: Value-oriented organization
- **Content Focus**: Capabilities, benefits, use cases
- **Examples**: Business scenarios, success stories
- **Visuals**: High-level diagrams, infographics, dashboards
- **Tone**: Professional, business-focused, value-driven

Example structure for business stakeholder documentation:
```markdown
# System Capabilities Overview

## Introduction
This document provides an overview of the key capabilities of our system and how they deliver business value.

## Key Capabilities

### Customer Management
Our system provides comprehensive customer management capabilities that help you:
- Maintain a unified view of customer information
- Track customer interactions across all channels
- Segment customers based on behavior and preferences
- Personalize customer experiences

**Business Impact:**
- 360° customer view increases upsell opportunities by 35%
- Personalization capabilities increase conversion rates by 25%
- Customer segmentation improves marketing ROI by 40%

### Order Processing
The order processing system streamlines the entire order lifecycle:
- Automated order validation and processing
- Real-time inventory management
- Flexible payment processing options
- Order tracking and notifications

**Business Impact:**
- Reduces order processing time by 75%
- Decreases order errors by 90%
- Improves customer satisfaction scores by 30%

## Use Cases

### Retail Chain Implementation
A national retail chain implemented our system and achieved:
- 45% reduction in checkout time
- 60% improvement in inventory accuracy
- 25% increase in repeat purchases
- $2.5M annual savings in operational costs

### B2B Distributor Case Study
A B2B distributor leveraged our system to:
- Automate 85% of routine order processing
- Reduce order fulfillment time from 3 days to 4 hours
- Decrease order discrepancies by 95%
- Improve customer retention by 40%

## Implementation Timeline
- Discovery and Planning: 2-4 weeks
- Core Implementation: 8-12 weeks
- Integration and Testing: 4-6 weeks
- Training and Rollout: 2-4 weeks

## ROI Analysis
Based on industry benchmarks, organizations typically achieve:
- Full ROI within 9-12 months
- 3-5x ROI over three years
- 30-40% reduction in operational costs
- 20-30% increase in revenue through improved capabilities
```

## Information Extraction Techniques

### Extracting from `.project-memory/`

#### 1. HLD Documents

High-Level Design documents contain architectural information:

- **What to Extract**:
  - System architecture overview
  - Component relationships
  - Key design decisions and rationales
  - Non-functional requirements
  - Technology stack

- **Extraction Approach**:
  - Identify the latest HLD documents in `.project-memory/hld/`
  - Focus on diagrams and visual representations
  - Extract high-level concepts and relationships
  - Note design principles and patterns
  - Identify key components and their purposes

- **Transformation for Documentation**:
  - Simplify technical details for end-user documentation
  - Maintain technical depth for developer documentation
  - Create visual representations appropriate for each audience
  - Link architectural concepts to user-facing features
  - Explain design decisions in terms of benefits

#### 2. LLD Documents

Low-Level Design documents contain detailed implementation information:

- **What to Extract**:
  - Detailed component specifications
  - Interface definitions
  - Data models and structures
  - Algorithms and processes
  - Error handling approaches

- **Extraction Approach**:
  - Review LLD documents in `.project-memory/lld/`
  - Focus on interface definitions and data models
  - Extract validation rules and constraints
  - Note error conditions and handling
  - Identify configuration options

- **Transformation for Documentation**:
  - Convert technical specifications to user instructions
  - Extract API details for developer documentation
  - Identify configuration parameters for administrator guides
  - Derive troubleshooting information from error handling
  - Create examples based on implementation details

#### 3. Specifications

Specifications contain requirements and feature descriptions:

- **What to Extract**:
  - Feature descriptions and capabilities
  - User requirements
  - Acceptance criteria
  - Business rules
  - Constraints and limitations

- **Extraction Approach**:
  - Review specification documents in `.project-memory/lld/`
  - Focus on user-facing requirements
  - Extract business rules and validation criteria
  - Note feature dependencies and relationships
  - Identify user roles and permissions

- **Transformation for Documentation**:
  - Convert requirements to feature descriptions
  - Derive user guides from acceptance criteria
  - Create tutorials based on user scenarios
  - Develop reference documentation from business rules
  - Map features to user benefits

### Extracting from Code

#### 1. API Endpoints

For API documentation:

- **What to Extract**:
  - Endpoint URLs and methods
  - Request parameters and formats
  - Response structures and status codes
  - Authentication requirements
  - Error responses

- **Extraction Approach**:
  - Review API controller files
  - Examine route definitions
  - Analyze parameter validation
  - Review response formatting
  - Identify error handling patterns

- **Transformation for Documentation**:
  - Create comprehensive API reference
  - Develop request and response examples
  - Document authentication methods
  - Create error code reference
  - Provide integration examples

#### 2. Data Models

For data structure documentation:

- **What to Extract**:
  - Entity definitions
  - Field types and constraints
  - Relationships between entities
  - Validation rules
  - Default values

- **Extraction Approach**:
  - Review model/entity definitions
  - Examine database schemas
  - Analyze validation code
  - Note relationship definitions
  - Identify business logic in models

- **Transformation for Documentation**:
  - Create entity relationship diagrams
  - Document field constraints for developers
  - Explain data structures in user-friendly terms
  - Provide examples of valid data
  - Document data lifecycle

#### 3. Configuration Options

For configuration documentation:

- **What to Extract**:
  - Configuration parameters
  - Default values
  - Valid options
  - Configuration file locations
  - Environment variables

- **Extraction Approach**:
  - Review configuration files
  - Examine environment variable usage
  - Analyze configuration loading code
  - Note validation of configuration
  - Identify configuration dependencies

- **Transformation for Documentation**:
  - Create configuration reference tables
  - Provide example configurations
  - Document configuration hierarchies
  - Explain effects of configuration changes
  - Create setup guides for administrators

## Documentation Maintenance and Updates

### Tracking Changes

Implement a system to track documentation changes:

1. **Version Documentation**
   - Include version information in documentation
   - Align documentation versions with software versions
   - Maintain a changelog for documentation

2. **Track Source Material Changes**
   - Monitor changes to `.project-memory/` artifacts
   - Watch for code changes that affect APIs or features
   - Note specification updates that require documentation changes

3. **Establish Update Triggers**
   - New feature implementation
   - API changes
   - UI changes
   - Configuration changes
   - Bug fixes that affect documented behavior

### Update Process

Follow a structured process for documentation updates:

1. **Identify Affected Documentation**
   - Determine which documents need updating
   - Assess the scope of required changes
   - Prioritize updates based on impact

2. **Extract Updated Information**
   - Review updated source materials
   - Identify specific changes
   - Extract new or modified information

3. **Update Documentation**
   - Make targeted updates to affected sections
   - Ensure consistency across related documents
   - Update examples and visuals as needed
   - Review cross-references and links

4. **Quality Check**
   - Verify technical accuracy of updates
   - Check for consistency with other documentation
   - Ensure appropriate style and tone
   - Validate examples and code samples

5. **Publish Updates**
   - Update version information
   - Note changes in changelog
   - Ensure proper formatting and organization
   - Publish to appropriate documentation channels

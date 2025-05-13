# HLD and LLD Creation Guidelines

As the Architect, you are responsible for creating both High-Level Design (HLD) and Low-Level Design (LLD) documents that guide the implementation of the system. This document provides guidelines for creating effective, comprehensive design documentation that serves as a foundation for the development process.

## Understanding HLD vs. LLD

### High-Level Design (HLD)

High-Level Design focuses on the overall system architecture and provides a broad view of the system:

- **Purpose**: Communicate the overall system structure and approach
- **Audience**: Business Owner, Orchestrator, and all development agents
- **Detail Level**: Broad, focusing on major components and their interactions
- **Timing**: Created early in the development process
- **Location**: Stored in `.project-memory/hld/`

### Low-Level Design (LLD)

Low-Level Design provides detailed specifications for individual components:

- **Purpose**: Guide specific implementation details
- **Audience**: Primarily Specification Writer, TDD Tester, and Auto-Coder agents
- **Detail Level**: Detailed, focusing on specific components, interfaces, and algorithms
- **Timing**: Created after HLD approval, before implementation
- **Location**: Stored in `.project-memory/lld/`

## HLD Creation Process

### 1. Preparation

Before creating the HLD:

- Review business requirements thoroughly
- Understand project constraints and quality attributes
- Research relevant architectural patterns and technologies
- Identify key stakeholders and their concerns
- Gather necessary information through clarification questions

### 2. HLD Structure and Content

Create HLD documents with the following sections:

#### a. System Overview
- Brief description of the system purpose and scope
- Key business drivers and requirements
- Major constraints and assumptions

#### b. Architectural Approach
- Selected architectural style(s) and patterns
- Rationale for architectural choices
- Alternatives considered and why they were rejected
- Key quality attributes addressed (performance, scalability, security, etc.)

#### c. System Context
- System context diagram showing external entities
- Description of system boundaries
- External interfaces and dependencies

#### d. Component Architecture
- High-level component diagram
- Major components and their responsibilities
- Component interactions and dependencies
- Key interfaces between components

#### e. Data Architecture
- High-level data model
- Data storage approach
- Data flow diagrams
- Data consistency and integrity strategies

#### f. Cross-Cutting Concerns
- Security approach
- Performance considerations
- Scalability strategy
- Monitoring and observability
- Error handling and logging approach

#### g. Technology Stack
- Selected technologies and frameworks
- Rationale for technology choices
- Version constraints and compatibility

#### h. Deployment Architecture
- Deployment model
- Infrastructure requirements
- Environment configurations
- Scaling approach

#### i. Risks and Mitigations
- Identified architectural risks
- Mitigation strategies
- Open issues and decisions

### 3. HLD Documentation Guidelines

When creating HLD documents:

- Use clear, concise language
- Include diagrams for visual understanding
- Focus on the "what" and "why" more than the "how"
- Highlight key architectural decisions and their rationale
- Address stakeholder concerns explicitly
- Maintain traceability to business requirements
- Keep the document concise but comprehensive

### 4. HLD Review and Refinement

After creating the initial HLD:

- Review with the Orchestrator
- Explain to the Business Owner in accessible language
- Gather feedback and address concerns
- Refine the architecture based on feedback
- Document changes and their rationale
- Obtain formal approval before proceeding to LLD

## LLD Creation Process

### 1. Preparation

Before creating the LLD:

- Ensure the HLD is approved and stable
- Identify components that need detailed design
- Prioritize components based on development sequence
- Gather additional information needed for detailed design
- Coordinate with Specification Writer for alignment

### 2. LLD Structure and Content

Create LLD documents with the following sections:

#### a. Component Overview
- Purpose and scope of the component
- Relationship to other components
- Key requirements addressed

#### b. Detailed Design
- Component structure (classes, modules, etc.)
- Interfaces and contracts
- Data structures and algorithms
- State management
- Error handling
- Performance optimizations

#### c. Interface Specifications
- API definitions (endpoints, methods, parameters)
- Request/response formats
- Error codes and messages
- Rate limiting and throttling
- Authentication and authorization requirements

#### d. Data Design
- Detailed data models
- Database schema
- Data validation rules
- Data access patterns
- Caching strategies

#### e. Behavior Specifications
- Sequence diagrams for key operations
- State diagrams where applicable
- Business rules and logic
- Transaction management
- Concurrency handling

#### f. Error Handling and Logging
- Error scenarios and handling strategies
- Logging requirements
- Monitoring points
- Alerting thresholds

#### g. Security Considerations
- Authentication and authorization details
- Data protection measures
- Input validation
- Security controls and mitigations

#### h. Testing Considerations
- Testability design
- Test approach recommendations
- Mock requirements
- Test data considerations

### 3. LLD Documentation Guidelines

When creating LLD documents:

- Be precise and unambiguous
- Include code-like pseudocode where helpful
- Use UML or similar diagrams for clarity
- Provide examples for complex logic
- Define all interfaces completely
- Specify error handling for each component
- Address performance and security explicitly
- Make the document actionable for implementers

### 4. LLD Review and Refinement

After creating the initial LLD:

- Review with the Specification Writer and TDD Tester
- Ensure alignment with HLD
- Validate technical feasibility
- Address implementation concerns
- Refine based on feedback
- Document changes and their rationale

## Ensuring Continuity and Knowledge Transfer

### 1. Documentation Organization

Organize design documentation for easy navigation and reference:

- Use consistent naming conventions
- Create an index document linking related designs
- Maintain a document hierarchy reflecting component relationships
- Use cross-references between related documents
- Include version history and change logs

### 2. Metadata and Traceability

Include comprehensive metadata in all design documents:

```markdown
---
title: "Component X Design"
version: "1.2.0"
status: "Approved"
created_by: "architect"
created_date: "2023-05-15T10:30:00Z"
last_modified_by: "architect"
last_modified_date: "2023-05-20T14:45:00Z"
related_tasks: ["ARCH-COMP-X-001"]
relevant_links: ["../hld/system_architecture.md"]
tags: ["component-x", "api", "authentication"]
parent_document: "../hld/system_architecture.md"
child_documents: ["../lld/component_x_api.md", "../lld/component_x_data_model.md"]
related_concepts: ["authentication", "authorization"]
project_type_tags: ["web-app", "api-backend"]
visibility: "internal"
---
```

### 3. Design Summaries for Context Recovery

Create summary documents to facilitate quick context recovery:

- **Architecture Overview Summary**: Concise summary of the entire architecture
- **Component Relationship Map**: Visual representation of component dependencies
- **Key Decisions Summary**: List of major architectural decisions and rationales
- **Design Principles Summary**: Core principles guiding the architecture

Store these summaries in `.project-memory/hld/summaries/` for easy reference.

### 4. Progressive Elaboration

Use progressive elaboration to manage complexity:

- Start with high-level concepts and gradually add detail
- Create "zoom levels" of documentation (system → component → module)
- Allow readers to navigate from abstract to detailed views
- Maintain consistency across levels of detail

## Diagramming Standards

### 1. System Context Diagrams

For system context diagrams:

- Show the system as a single box
- Include all external entities (users, systems, services)
- Show data flows between the system and external entities
- Label all entities and flows clearly
- Use different line styles for different types of interactions

Example:
```
┌─────────────────┐      ┌─────────────────┐
│                 │      │                 │
│    Customer     │─────→│   E-Commerce    │
│                 │←─────│     System      │
└─────────────────┘      └───────┬─────────┘
                                 │
                                 ↓
                         ┌─────────────────┐
                         │                 │
                         │    Payment      │
                         │    Gateway      │
                         │                 │
                         └─────────────────┘
```

### 2. Component Diagrams

For component diagrams:

- Show major components as boxes
- Group related components visually
- Show interfaces between components
- Indicate direction of dependencies
- Use consistent symbols for different component types

Example:
```
┌───────────────────────────────────────┐
│           Web Application             │
└───────────────┬───────────────────────┘
                │
                ↓
┌───────────────────────────────────────┐
│              API Gateway              │
└─┬─────────────┬──────────────────────┬┘
  │             │                      │
  ↓             ↓                      ↓
┌─────────┐ ┌─────────┐         ┌──────────┐
│ User    │ │ Product │         │ Order    │
│ Service │ │ Service │         │ Service  │
└────┬────┘ └────┬────┘         └─────┬────┘
     │           │                    │
     ↓           ↓                    ↓
┌─────────┐ ┌─────────┐         ┌──────────┐
│ User DB │ │Product DB│        │ Order DB │
└─────────┘ └─────────┘         └──────────┘
```

### 3. Sequence Diagrams

For sequence diagrams:

- Include all relevant components and actors
- Show the sequence of interactions in time order
- Label all messages clearly
- Include return values and responses
- Show error paths and alternative flows
- Add notes for clarification where needed

Example:
```
┌──────┐          ┌──────┐          ┌──────┐
│Client│          │API   │          │Auth  │
└──┬───┘          └──┬───┘          └──┬───┘
   │  Login Request  │                 │
   │───────────────→│                 │
   │                 │  Validate       │
   │                 │───────────────→│
   │                 │  Token          │
   │                 │←───────────────│
   │  Response       │                 │
   │←───────────────│                 │
┌──┴───┐          ┌──┴───┐          ┌──┴───┐
│Client│          │API   │          │Auth  │
└──────┘          └──────┘          └──────┘
```

## Examples

### Example 1: HLD Document Excerpt

```markdown
# E-Commerce System High-Level Design

## System Overview

The XYZ E-Commerce System is a cloud-native platform designed to provide a scalable, reliable online shopping experience. The system will support product browsing, user accounts, shopping carts, order processing, and payment integration.

## Architectural Approach

### Selected Architecture

The system will follow a microservices architecture with:
- Domain-driven design for service boundaries
- API Gateway pattern for client communication
- Event-driven architecture for asynchronous processes
- CQRS for high-performance read operations

### Rationale

This approach was selected to enable:
- Independent scaling of components based on load
- Team autonomy and parallel development
- Resilience through service isolation
- Flexibility in technology choices per service

### Alternatives Considered

1. **Monolithic Architecture**
   - Pros: Simpler development, deployment, and testing
   - Cons: Limited scalability, tight coupling, technology constraints
   - Rejection Reason: Would not meet scalability requirements for peak shopping periods

2. **Serverless Architecture**
   - Pros: Automatic scaling, reduced operational overhead
   - Cons: Cold start latency, vendor lock-in, complex debugging
   - Rejection Reason: Latency requirements for core shopping experience
```

### Example 2: LLD Document Excerpt

```markdown
# Product Service Low-Level Design

## Component Overview

The Product Service manages the product catalog, including product information, categories, pricing, and inventory. It provides APIs for product creation, updates, search, and retrieval.

## Detailed Design

### Core Entities

#### Product
- ProductID (UUID)
- Name (String, 1-100 chars)
- Description (String, 0-5000 chars)
- SKU (String, unique)
- Price (Decimal, min 0)
- Categories (Array of CategoryIDs)
- Attributes (Key-value pairs)
- Images (Array of Image objects)
- Status (Enum: Active, Inactive, Discontinued)
- CreatedAt (Timestamp)
- UpdatedAt (Timestamp)

#### Category
- CategoryID (UUID)
- Name (String, 1-50 chars)
- Description (String, 0-1000 chars)
- ParentCategoryID (UUID, nullable)
- Status (Enum: Active, Inactive)
- DisplayOrder (Integer)

### API Endpoints

#### Get Product
- **Endpoint:** GET /api/v1/products/{productId}
- **Parameters:** productId (UUID)
- **Response:** Product object
- **Error Codes:**
  - 404: Product not found
  - 400: Invalid product ID format

#### Search Products
- **Endpoint:** GET /api/v1/products
- **Parameters:**
  - query (String, optional): Search term
  - category (UUID, optional): Filter by category
  - minPrice, maxPrice (Decimal, optional): Price range
  - sort (String, optional): Sort field
  - order (String, optional): Sort direction (asc, desc)
  - page, pageSize (Integer, optional): Pagination
- **Response:** Paginated list of Product objects
- **Error Codes:**
  - 400: Invalid parameter format

### Data Access Patterns

#### Product Retrieval
```typescript
function getProduct(productId: string): Promise<Product> {
  // Validate productId format
  if (!isValidUUID(productId)) {
    throw new ValidationError("Invalid product ID format");
  }
  
  // Check cache first
  const cachedProduct = productCache.get(productId);
  if (cachedProduct) {
    return Promise.resolve(cachedProduct);
  }
  
  // Query database if not in cache
  return productRepository.findById(productId)
    .then(product => {
      if (!product) {
        throw new NotFoundError("Product not found");
      }
      
      // Update cache
      productCache.set(productId, product, CACHE_TTL);
      return product;
    });
}
```
```

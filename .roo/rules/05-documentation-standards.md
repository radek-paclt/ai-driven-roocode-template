# Documentation Standards

This document outlines the standards for creating and maintaining documentation throughout the project. It covers both internal working documentation (in `.project-memory/`) and final user-facing documentation (in `docs/`).

## General Principles

1. **Clarity and Conciseness**
   - Write in clear, simple language
   - Be concise but complete
   - Use active voice and present tense
   - Avoid jargon unless necessary (and define it when used)

2. **Audience Awareness**
   - Consider the intended audience for each document
   - Adjust technical depth accordingly
   - Provide context and background information as needed
   - Use appropriate terminology for the audience

3. **Consistency**
   - Use consistent terminology throughout documentation
   - Follow consistent formatting and structure
   - Maintain a consistent tone and style

4. **Maintainability**
   - Keep documentation up-to-date with code changes
   - Use version control for documentation
   - Follow established file naming and organization conventions

## Internal Documentation (`.project-memory/`)

### Structure and Organization

1. **File Naming**
   - Use `snake_case_with_prefixes.md`
   - Use numerical prefixes for ordering (e.g., `01_`, `02_`)
   - Use descriptive names that indicate content

2. **Metadata**
   - Include YAML frontmatter as specified in the Project Memory Guidelines
   - Keep metadata up-to-date, especially version and status
   - Use appropriate tags for categorization

3. **Content Organization**
   - Use hierarchical headings (# for title, ## for sections, etc.)
   - Include a table of contents for longer documents
   - Group related information together
   - Use lists and tables for structured information

### Content Guidelines

1. **Technical Documentation**
   - Include context and purpose
   - Document design decisions and alternatives considered
   - Explain rationale for important decisions
   - Include diagrams for complex systems or flows

2. **Specifications**
   - Be explicit about requirements
   - Include acceptance criteria
   - Define interfaces clearly
   - Document constraints and assumptions

3. **Meeting Notes and Decisions**
   - Record date, participants, and context
   - Clearly mark decisions and action items
   - Link to related documents or tasks
   - Update with follow-up information

## External Documentation (`docs/`)

### Structure and Organization

1. **File Organization**
   - Organize by user role or use case
   - Use a logical hierarchy
   - Include a clear navigation structure
   - Consider progressive disclosure of complexity

2. **Document Types**
   - README: Project overview and getting started
   - User Guides: How to use the system
   - API Documentation: Interface specifications
   - Architecture Documentation: System design and components
   - Contributing Guidelines: How to contribute to the project

### Content Guidelines

1. **User Documentation**
   - Focus on tasks users want to accomplish
   - Include step-by-step instructions
   - Provide examples and screenshots
   - Address common questions and issues

2. **API Documentation**
   - Document all endpoints, parameters, and responses
   - Include request and response examples
   - Document error codes and handling
   - Provide authentication information

3. **Technical Documentation**
   - Explain architecture and components
   - Document dependencies and requirements
   - Include setup and configuration instructions
   - Provide troubleshooting information

## Markdown Guidelines

1. **Headings**
   - Use ATX-style headings (`#` for level 1, `##` for level 2, etc.)
   - Use sentence case for headings
   - Don't skip heading levels
   - Keep headings concise

2. **Lists**
   - Use `-` for unordered lists
   - Use `1.` for ordered lists
   - Indent nested lists with 2 or 4 spaces
   - Be consistent with punctuation in list items

3. **Code Blocks**
   - Use triple backticks (```) for code blocks
   - Specify the language for syntax highlighting
   - Use inline code (`) for code references in text
   - Ensure code examples are correct and up-to-date

4. **Links and References**
   - Use descriptive link text
   - Use relative links for internal references
   - Check links regularly to ensure they're not broken
   - Include reference links for external sources

5. **Images and Diagrams**
   - Include alt text for images
   - Use appropriate image formats (PNG for screenshots, SVG for diagrams)
   - Keep images at a reasonable size
   - Consider using Mermaid for diagrams in Markdown

## Examples

### Example: Internal Technical Document

```markdown
---
title: "Authentication Service Design"
version: "1.0.0"
status: "ApprovedByTechLead"
created_by: "architect"
created_date: "2023-05-15T14:30:00Z"
last_modified_by: "architect"
last_modified_date: "2023-05-15T16:45:00Z"
related_tasks: ["AUTH-SERVICE-DESIGN"]
relevant_links: ["../hld/system_architecture.md"]
tags: ["authentication", "security", "backend"]
parent_document: "../hld/system_architecture.md"
child_documents: ["./auth_service_api_spec.md"]
related_concepts: ["jwt", "oauth"]
project_type_tags: ["web-app", "api-backend"]
visibility: "internal"
---

# Authentication Service Design

## Overview

This document describes the design of the authentication service for the XYZ application. The service is responsible for user registration, login, and session management.

## Architecture

The authentication service is a standalone microservice that communicates with other services via REST APIs. It maintains its own database for user credentials and session information.

### Components

- **API Layer**: Handles HTTP requests and responses
- **Service Layer**: Implements business logic
- **Data Access Layer**: Manages database operations
- **Security Layer**: Handles encryption and token management

## Authentication Flow

1. User submits credentials
2. Service validates credentials
3. If valid, service generates JWT
4. JWT is returned to client
5. Client includes JWT in subsequent requests

## Design Decisions

### JWT vs. Session Cookies

We chose JWT for authentication because:
- It's stateless, reducing database load
- It works well with microservices architecture
- It simplifies mobile API authentication

Alternatives considered:
- Session cookies: Rejected due to stateful nature and microservices complexity
- OAuth only: Rejected as too complex for our current needs

## Security Considerations

- Passwords are hashed using bcrypt
- JWTs are signed with RS256
- Token expiration is set to 24 hours
- Refresh tokens are implemented for seamless re-authentication
```

### Example: User-Facing Documentation

```markdown
# Getting Started with XYZ Application

This guide will help you set up and start using the XYZ application.

## Prerequisites

Before you begin, ensure you have:
- Node.js (v14 or later)
- npm (v6 or later)
- MongoDB (v4.4 or later)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/example/xyz-app.git
   cd xyz-app
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Update the values in `.env` with your configuration

4. Start the application:
   ```bash
   npm start
   ```

The application should now be running at `http://localhost:3000`.

## First Steps

### Creating an Account

1. Navigate to `http://localhost:3000/register`
2. Fill in your details
3. Click "Register"
4. Verify your email address using the link sent to your inbox

### Logging In

1. Navigate to `http://localhost:3000/login`
2. Enter your email and password
3. Click "Login"

## Next Steps

- [Explore the Dashboard](./dashboard.md)
- [Configure Your Profile](./profile.md)
- [Create Your First Project](./projects.md)

## Troubleshooting

### Common Issues

#### Application Won't Start

Check that:
- MongoDB is running
- The connection string in `.env` is correct
- The port specified is available

#### Can't Log In

- Ensure your email is verified
- Check for caps lock
- Try resetting your password
```

# Design REST API

## Overview

Design RESTful API endpoints following REST principles and best practices. Create well-structured, intuitive, and maintainable APIs that follow industry standards for resource naming, HTTP methods, status codes, and error handling.

## Steps

1. **Resource Identification**
    - Identify core resources/entities using nouns (e.g., `/users`, not `/getUsers`)
    - Define relationships and hierarchies between resources
    - List all data attributes for each resource
    - Keep nesting to 2-3 levels maximum

2. **URL Structure Design**
    - Use plural nouns for collections: `/api/users`, `/api/products`
    - Use path parameters for individual items: `/api/users/{id}`
    - Use hyphens for multi-word resources: `/api/order-items`
    - Version your API: `/api/v1/users`
    - Avoid file extensions in URLs

3. **HTTP Method Mapping**
    - **GET**: Retrieve resources (safe, idempotent)
    - **POST**: Create new resources
    - **PUT**: Replace entire resource (idempotent)
    - **PATCH**: Partial update (idempotent)
    - **DELETE**: Remove resource (idempotent)

4. **Endpoint Design**
    - Collections: `GET /api/users` - List all
    - Individual: `GET /api/users/{id}` - Get one
    - Create: `POST /api/users`
    - Update: `PUT/PATCH /api/users/{id}`
    - Delete: `DELETE /api/users/{id}`
    - Nested: `GET /api/users/{id}/orders`

5. **Query Parameters**
    - Filtering: `?role=admin&status=active`
    - Pagination: `?page=2&limit=20`
    - Sorting: `?sort=created_at&order=desc`
    - Searching: `?q=john`
    - Field selection: `?fields=id,name,email`

6. **Status Code Selection**
    - **200 OK**: Successful GET, PUT, PATCH, DELETE
    - **201 Created**: Successful POST (include Location header)
    - **204 No Content**: Successful DELETE with no body
    - **400 Bad Request**: Invalid request data
    - **401 Unauthorized**: Missing/invalid authentication
    - **403 Forbidden**: Not authorized
    - **404 Not Found**: Resource doesn't exist
    - **409 Conflict**: Duplicate/constraint violation
    - **422 Unprocessable Entity**: Validation errors
    - **500 Internal Server Error**: Server-side errors

7. **Request/Response Format**
    - Use JSON as default format
    - Use consistent field naming (camelCase or snake_case)
    - Include metadata in responses (pagination, timestamps)
    - Provide clear error messages with error codes
    - Return created resource in POST responses

8. **Error Response Design**
    - Consistent error structure across endpoints
    - Include error code, message, and field-level details
    - Use appropriate HTTP status codes
    - Don't expose internal implementation details

9. **Authentication & Authorization**
    - Choose method: JWT, OAuth, API keys
    - Protect endpoints requiring authentication
    - Implement role-based access control (RBAC)
    - Use HTTPS for all endpoints
    - Consider rate limiting and throttling

10. **API Documentation**
    - Document all endpoints with examples
    - Specify request/response schemas
    - Include authentication requirements
    - Document error responses
    - Consider OpenAPI/Swagger specification

## Checklist

### Design
- [ ] Resources identified using nouns
- [ ] URLs simple and intuitive
- [ ] API versioning strategy defined
- [ ] HTTP methods used appropriately
- [ ] Status codes assigned correctly

### Implementation
- [ ] Query parameters for filtering/pagination/sorting
- [ ] Consistent JSON format
- [ ] Error structure standardized
- [ ] Authentication/authorization implemented
- [ ] Rate limiting considered

### Documentation
- [ ] All endpoints documented
- [ ] Request/response schemas specified
- [ ] Error responses documented
- [ ] Examples provided

## Example: User Management API

```
# Basic CRUD
GET    /api/v1/users              # List users
POST   /api/v1/users              # Create user
GET    /api/v1/users/{id}         # Get user
PUT    /api/v1/users/{id}         # Update user
DELETE /api/v1/users/{id}         # Delete user

# Nested & Queries
GET    /api/v1/users/{id}/orders  # User's orders
GET    /api/v1/users?role=admin&page=1&limit=20
```

**Create User Request:**
```json
POST /api/v1/users
{
  "name": "John Doe",
  "email": "john@example.com",
  "role": "user"
}

Response: 201 Created
Location: /api/v1/users/123
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com",
  "role": "user",
  "created_at": "2026-01-13T10:30:00Z"
}
```

**Error Response:**
```json
Response: 422 Unprocessable Entity
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request data",
    "details": [
      {"field": "email", "message": "Email format is invalid"}
    ]
  }
}
```

## Best Practices

- Use lowercase in URLs, hyphens not underscores
- GET, PUT, PATCH, DELETE must be idempotent
- Always paginate large collections
- Support filtering and sorting on list endpoints
- Use HTTPS and validate all inputs
- Implement proper authentication and rate limiting
- Support field selection to reduce payload size

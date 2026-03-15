# Generate CRUD Operations

## Overview

Generate complete CRUD (Create, Read, Update, Delete) operations for a data model including database schema, API endpoints, business logic, validation, and tests. Accelerates development by scaffolding boilerplate code while following best practices.

## Steps

1. **Model Definition**
    - Define model name and purpose
    - List fields with types, constraints, and defaults
    - Identify required vs optional fields
    - Define relationships (foreign keys, associations)
    - Specify unique constraints and indexes

2. **Database Schema**
    - Create migration file
    - Define columns with appropriate data types
    - Add primary key, foreign keys, unique constraints
    - Create indexes for frequently queried columns
    - Add timestamps (created_at, updated_at)

3. **Data Model/ORM**
    - Create model class with all fields
    - Define data types and validation rules
    - Set up relationships (has many, belongs to, many-to-many)
    - Add computed fields and serialization methods

4. **Validation Layer**
    - Create validation schemas for create/update
    - Validate field types, lengths, ranges
    - Validate required fields and unique constraints
    - Provide clear error messages

5. **Repository/Data Access**
    - Implement findAll() with pagination
    - Implement findById(), create(), update(), delete()
    - Add query methods (findByField, search, filter)
    - Handle database errors gracefully

6. **Business Logic/Service**
    - Implement createResource() with validation
    - Implement getResource() with authorization
    - Implement updateResource(), deleteResource(), listResources()
    - Add domain-specific business rules

7. **API Controller/Handler**
    - Create CRUD endpoints (POST, GET, PUT, PATCH, DELETE)
    - Parse and validate request parameters
    - Call service layer methods
    - Return appropriate status codes

8. **Request/Response DTOs**
    - Create DTOs for requests and responses
    - Hide sensitive fields in responses
    - Define create/update request DTOs
    - Add pagination metadata for lists

9. **Error Handling**
    - Handle validation errors (400, 422)
    - Handle not found (404), conflict (409), authorization (403)
    - Provide clear error messages
    - Log errors appropriately

10. **Testing**
    - Write unit tests for service layer
    - Write integration tests for API endpoints
    - Test CRUD operations with valid/invalid data
    - Test validation rules and error scenarios

## Checklist

### Database & Model
- [ ] Migration file created with proper schema
- [ ] Indexes created for queried columns
- [ ] Model class with validation defined
- [ ] Relationships configured

### Business Logic
- [ ] Service layer with CRUD methods
- [ ] Validation implemented
- [ ] Authorization checks added
- [ ] Error handling in place

### API Layer
- [ ] All CRUD endpoints implemented
- [ ] Request/response DTOs defined
- [ ] Appropriate status codes returned
- [ ] Pagination/filtering supported

### Testing
- [ ] Unit tests for service layer
- [ ] Integration tests for API
- [ ] Validation rules tested
- [ ] Error scenarios covered

## Example: Product Model

**Model:**
```
Product:
  - id: integer (PK, auto-increment)
  - name: string (required, unique, max 255)
  - price: decimal(10,2) (required, min 0)
  - stock_quantity: integer (default 0, min 0)
  - category_id: integer (FK)
  - is_active: boolean (default true)
  - created_at, updated_at: timestamp
```

**Migration (SQL):**
```sql
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE,
  price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
  stock_quantity INTEGER NOT NULL DEFAULT 0,
  category_id INTEGER REFERENCES categories(id),
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_name ON products(name);
```

**API Endpoints:**
```
POST   /api/v1/products           # Create
GET    /api/v1/products           # List (paginated)
GET    /api/v1/products/{id}      # Get one
PUT    /api/v1/products/{id}      # Update
DELETE /api/v1/products/{id}      # Delete

# Queries
GET /api/v1/products?category_id=5&is_active=true
GET /api/v1/products?q=laptop&sort=price&order=asc
```

**Service Layer (TypeScript):**
```typescript
export class ProductService {
  async createProduct(data: CreateProductDTO): Promise<Product> {
    // Validate
    if (!data.name || data.price < 0) {
      throw new ValidationError('Invalid data');
    }
    
    // Check duplicates
    const existing = await this.repo.findByName(data.name);
    if (existing) {
      throw new ValidationError('Name exists');
    }
    
    return await this.repo.create(data);
  }

  async getProduct(id: number): Promise<Product> {
    const product = await this.repo.findById(id);
    if (!product) throw new NotFoundError('Not found');
    return product;
  }
}
```

## Best Practices

- Add indexes for foreign keys and frequently queried columns
- Validate on both frontend and backend
- Keep controllers thin, logic in services
- Use appropriate HTTP methods and status codes
- Support pagination for list endpoints
- Test happy paths and error scenarios

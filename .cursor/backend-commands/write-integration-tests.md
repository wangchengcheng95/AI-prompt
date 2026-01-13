# Write Integration Tests

## Overview

Create comprehensive integration tests that verify multiple components work correctly together. Unlike unit tests, integration tests validate interactions between modules, API endpoints with databases, external services, and complete workflows.

## Steps

1. **Test Scope Definition**
    - Identify components being integrated (API + Database, Service + External API)
    - Define integration boundaries and contracts
    - List all integration points
    - Determine test data requirements

2. **Test Environment Setup**
    - Configure test database (separate from dev/prod)
    - Set up test fixtures and seed data
    - Mock or stub external services if needed
    - Ensure test isolation (clean state per test)

3. **Database Integration Tests**
    - Test database migrations
    - Verify CRUD operations with actual database
    - Test transactions and rollbacks
    - Test constraint enforcement (foreign keys, uniqueness)

4. **API Integration Tests**
    - Test endpoints with real database connections
    - Verify request/response data flows
    - Test authentication and authorization
    - Test with valid, invalid, and edge case inputs
    - Verify error responses and status codes
    - Test pagination, filtering, sorting

5. **External Service Integration**
    - Test interactions with external APIs
    - Verify data transformation
    - Test error handling when service fails
    - Test timeout and retry logic
    - Verify webhook and callback handling

6. **Multi-Component Workflows**
    - Test complete user workflows across components
    - Verify data flows through multiple layers
    - Test state transitions
    - Test async operations and message queues

7. **Error Scenario Testing**
    - Test database connection failures
    - Test external service unavailability
    - Test network timeouts
    - Test invalid authentication
    - Test concurrent conflicts
    - Verify graceful degradation

8. **Test Organization**
    - Group related tests logically
    - Use descriptive test names
    - Follow Arrange-Act-Assert pattern
    - Keep tests independent
    - Make tests deterministic

9. **Performance Considerations**
    - Keep tests reasonably fast
    - Run slow tests separately
    - Parallelize tests where possible
    - Use transactions for database tests

10. **Documentation**
    - Document what each test verifies
    - Explain non-obvious test setup
    - Document how to run tests locally
    - Note external dependencies

## Checklist

### Setup
- [ ] Test database configured separately
- [ ] Test fixtures prepared
- [ ] External services mocked appropriately
- [ ] Test isolation ensured

### Coverage
- [ ] Database operations tested
- [ ] API endpoints tested with database
- [ ] Authentication/authorization tested
- [ ] Error scenarios covered
- [ ] Multi-component workflows verified

### Quality
- [ ] Tests are independent
- [ ] Tests are deterministic
- [ ] Descriptive test names used
- [ ] Resources cleaned up after tests

## Examples

### 1. API + Database Integration (JavaScript)

```javascript
describe('User API Integration', () => {
  beforeEach(async () => {
    await db.migrate.latest();
    await db.seed.run();
  });

  afterEach(async () => {
    await db.migrate.rollback();
  });

  test('POST /api/users creates user in database', async () => {
    const userData = { email: 'test@example.com', name: 'Test User' };
    
    const response = await request(app)
      .post('/api/users')
      .send(userData)
      .expect(201);
    
    expect(response.body).toHaveProperty('id');
    
    const user = await db('users').where({ id: response.body.id }).first();
    expect(user.email).toBe(userData.email);
  });

  test('POST /api/users rejects duplicate email', async () => {
    await db('users').insert({ email: 'existing@example.com' });
    
    await request(app)
      .post('/api/users')
      .send({ email: 'existing@example.com', name: 'User' })
      .expect(409);
  });
});
```

### 2. External Service Integration (Python)

```python
class PaymentServiceTest(unittest.TestCase):
    def setUp(self):
        self.payment_provider_mock = Mock()
        self.service = PaymentService(self.payment_provider_mock)
    
    def test_process_payment_success(self):
        self.payment_provider_mock.charge.return_value = {
            'status': 'success',
            'transaction_id': 'txn_12345'
        }
        
        result = self.service.process_payment(100.00, 'USD', 'tok_visa')
        
        self.assertEqual(result.status, 'success')
        self.payment_provider_mock.charge.assert_called_once()
```

### 3. Multi-Component Workflow (Go)

```go
func TestOrderWorkflow(t *testing.T) {
    db := setupTestDB(t)
    defer db.Close()
    
    orderService := NewOrderService(db)
    inventoryService := NewInventoryService(db)
    
    productID := createTestProduct(t, db, 10) // 10 in stock
    userID := createTestUser(t, db)
    
    order, err := orderService.CreateOrder(userID, []OrderItem{
        {ProductID: productID, Quantity: 2},
    })
    require.NoError(t, err)
    
    // Verify inventory decremented
    stock, err := inventoryService.GetStock(productID)
    require.NoError(t, err)
    assert.Equal(t, 8, stock) // 10 - 2 = 8
}
```

## Test Patterns

**Database Setup with Transactions:**
```python
class TestCase:
    def setUp(self):
        self.transaction = db.begin()
    
    def tearDown(self):
        self.transaction.rollback()
```

**Reusable Test Fixtures:**
```javascript
const fixtures = {
  createTestUser: async (overrides = {}) => {
    return await db('users').insert({
      email: 'test@example.com',
      name: 'Test User',
      ...overrides
    }).returning('*');
  }
};
```

## Best Practices

- Isolate tests: Each test starts with clean slate
- Use realistic data: Test with production-like data
- Test failure paths: Don't just test happy paths
- Keep tests fast: Use test databases, not full datasets
- Run in CI/CD: Catch integration issues early
- Document dependencies: Make setup clear
- Test idempotency: Verify operations can be retried
- Verify side effects: Check database state, not just returns

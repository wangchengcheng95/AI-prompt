# Optimize Database Queries

## Overview

Analyze and optimize database queries to improve performance, reduce load times, and eliminate bottlenecks. Provides systematic approaches to identify slow queries, understand execution plans, and apply optimization techniques.

## Steps

1. **Query Performance Analysis**
    - Identify slow-running queries in application
    - Review logs for query execution times
    - Use database profiling tools
    - Check for N+1 query problems
    - Measure baseline performance

2. **Execution Plan Analysis**
    - Use EXPLAIN/EXPLAIN ANALYZE
    - Identify sequential scans (should be index scans)
    - Look for missing indexes
    - Check for inefficient joins
    - Analyze estimated vs actual row counts

3. **Indexing Strategy**
    - Create indexes on WHERE clause columns
    - Index JOIN, ORDER BY, GROUP BY columns
    - Create composite indexes for multi-column queries
    - Remove unused or duplicate indexes
    - Balance read performance vs write overhead

4. **Query Optimization**
    - Avoid SELECT * - specify needed columns only
    - Use EXISTS instead of IN for subqueries
    - Replace subqueries with JOINs when possible
    - Use LIMIT to restrict result sets
    - Avoid functions on indexed columns in WHERE
    - Use UNION ALL instead of UNION when duplicates OK

5. **Join Optimization**
    - Ensure join columns are indexed
    - Join in order from smallest to largest tables
    - Use appropriate join types
    - Avoid Cartesian products
    - Filter early in query pipeline

6. **N+1 Query Problem**
    - Identify loops executing queries repeatedly
    - Use eager loading to fetch related data upfront
    - Replace multiple queries with single JOIN
    - Use batch loading for related records

7. **Query Caching**
    - Cache frequently accessed, rarely changing data
    - Use application-level caching (Redis, Memcached)
    - Set appropriate cache expiration times
    - Invalidate cache on data updates

8. **Data Model Optimization**
    - Review normalization vs denormalization trade-offs
    - Partition large tables by date or key ranges
    - Archive old data to separate tables
    - Consider read replicas for read-heavy workloads

9. **Connection & Transaction Optimization**
    - Use connection pooling
    - Keep transactions short and focused
    - Use appropriate isolation levels
    - Batch multiple operations in single transaction

10. **Monitoring & Maintenance**
    - Monitor slow query logs
    - Track execution times over time
    - Run VACUUM/ANALYZE regularly (PostgreSQL)
    - Monitor index usage and effectiveness

## Checklist

### Analysis
- [ ] Slow queries identified
- [ ] Execution plans analyzed with EXPLAIN
- [ ] N+1 problems found
- [ ] Baseline performance measured

### Optimization
- [ ] Indexes created on key columns
- [ ] SELECT * replaced with specific columns
- [ ] Subqueries replaced with JOINs
- [ ] N+1 problems resolved with eager loading
- [ ] Caching implemented for frequently accessed data

### Maintenance
- [ ] Query monitoring set up
- [ ] Slow query logs reviewed regularly
- [ ] Index usage monitored
- [ ] Database statistics updated

## Examples

### 1. Using EXPLAIN to Find Issues

**Before:**
```sql
EXPLAIN ANALYZE
SELECT * FROM orders WHERE customer_id = 1234;

-- Sequential Scan (SLOW)
Seq Scan on orders (cost=0.00..1234.56 rows=10)
  Filter: (customer_id = 1234)
  Rows Removed by Filter: 50000
```

**After Adding Index:**
```sql
CREATE INDEX idx_orders_customer ON orders(customer_id);

-- Now uses Index Scan (FAST)
Index Scan using idx_orders_customer on orders
  (cost=0.29..15.32 rows=10)
```

### 2. Fixing N+1 Query Problem

**Before (101 queries):**
```python
users = db.query("SELECT * FROM users LIMIT 100")
for user in users:
    orders = db.query("SELECT * FROM orders WHERE user_id = ?", user.id)
```

**After (2 queries):**
```python
users = db.query("SELECT * FROM users LIMIT 100")
user_ids = [user.id for user in users]
orders = db.query("SELECT * FROM orders WHERE user_id IN (?)", user_ids)
```

### 3. Optimizing Subqueries

**Before (slow):**
```sql
SELECT u.id, u.name,
  (SELECT COUNT(*) FROM orders WHERE user_id = u.id) as count
FROM users u;
```

**After (fast):**
```sql
SELECT u.id, u.name, COUNT(o.id) as count
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
GROUP BY u.id, u.name;
```

### 4. Composite Index

```sql
-- Query with multiple conditions
SELECT * FROM events 
WHERE user_id = 123 
  AND event_type = 'purchase' 
  AND created_at > '2026-01-01'
ORDER BY created_at DESC;

-- Composite index matches query pattern
CREATE INDEX idx_events_user_type_date 
ON events(user_id, event_type, created_at DESC);
```

## Database-Specific Commands

**PostgreSQL:**
```sql
ANALYZE table_name;                    -- Update statistics
VACUUM ANALYZE table_name;             -- Reclaim space
SELECT * FROM pg_stat_user_indexes;    -- Check index usage
```

**MySQL:**
```sql
ANALYZE TABLE table_name;              -- Update statistics
SHOW FULL PROCESSLIST;                 -- Check running queries
SET GLOBAL slow_query_log = 'ON';     -- Enable slow log
```

## Best Practices

- **Measure first**: Always measure before and after
- **Index wisely**: Indexes speed reads but slow writes
- **Monitor regularly**: Performance degrades over time
- **Test with production data**: Small datasets hide issues
- **Keep it simple**: Complex queries harder to optimize
- **Cache strategically**: Not everything needs caching
- **Review periodically**: Fast queries become slow as data grows

# Check for Similar Commands

## Overview

Before creating a new command, search specified directories to detect existing commands with similar functionality. This prevents duplication and helps maintain a clean, non-redundant command collection.

## When to Use

- Before creating a new command
- When considering whether to extend an existing command vs creating a new one
- When auditing the repository for redundant commands

## Steps

### 1. **Define the Proposed Command**

Clearly describe what the new command should do:
- Command purpose (one sentence)
- Key functionality (3-5 bullet points)
- Primary keywords (5-10 terms)

Example:
```
Purpose: Generate comprehensive API documentation for REST endpoints
Keywords: API, documentation, REST, endpoints, OpenAPI, Swagger, generate
```

### 2. **Specify Search Scope**

Determine which directories to search:
- `.cursor/backend-commands/` - Language-agnostic backend commands
- `.cursor/go-backend-commands/` - Go-specific backend commands
- `.cursor/user-commands/` - Project-agnostic workflow commands
- `.cursor/devops-commands/` - DevOps and infrastructure commands
- All of the above (comprehensive search)

### 3. **Search by Keywords**

Use grep to search for keyword matches in command files:

```bash
# Search for specific keywords across all commands
grep -r -i "keyword1\|keyword2\|keyword3" .cursor/*/

# Search with context (shows surrounding lines)
grep -r -i -C 3 "keyword" .cursor/*/

# Search in titles only (first line of each file)
find .cursor/*commands/ -name "*.md" -exec head -1 {} + | grep -i "keyword"
```

### 4. **Analyze File Names**

Check for similar file names:

```bash
# List all command files
find .cursor/*commands/ -name "*.md" -type f | sort

# Search for similar names
find .cursor/*commands/ -name "*keyword*.md"
```

### 5. **Read Potentially Similar Commands**

For each potential match:
- Read the Overview section
- Check the Steps section
- Review the Checklist

Assess similarity:
- **High similarity (80-100%)**: Identical or near-identical functionality
- **Medium similarity (50-80%)**: Overlapping functionality, could be merged
- **Low similarity (20-50%)**: Some overlap, but distinct enough
- **No similarity (0-20%)**: Different functionality, keywords matched by coincidence

### 6. **Make a Decision**

Based on findings:

**If High Similarity Found:**
- ❌ **Do NOT create new command**
- ✅ **Use existing command**
- Consider: Does existing command need enhancement?

**If Medium Similarity Found:**
- ⚠️ **Evaluate carefully**
- Option A: Extend existing command with additional steps
- Option B: Create new command if use cases are distinct
- Consider: Would combining create confusion?

**If Low/No Similarity Found:**
- ✅ **Proceed with creating new command**
- Ensure clear differentiation in naming and description

### 7. **Document Decision**

If creating a new command despite similarities:
- Add note in Overview explaining how it differs from similar commands
- Reference related commands if applicable

Example:
```markdown
## Overview
This command focuses on X, while `existing-command.md` focuses on Y.
Use this command when [specific condition], use existing-command when [other condition].
```

## Search Examples

### Example 1: Checking for API Documentation Commands

**Proposed Command**: Generate API documentation

**Search**:
```bash
# Search for "api" and "documentation" keywords
grep -r -i "api.*doc\|documentation.*api" .cursor/*/

# Check file names
find .cursor/*commands/ -name "*api*.md" -o -name "*doc*.md"
```

**Found**: `generate-api-docs.md` in `backend-commands/`

**Decision**: ❌ Command already exists, use existing command

---

### Example 2: Checking for Test-Related Commands

**Proposed Command**: Run tests and fix failures automatically

**Search**:
```bash
# Search for test-related keywords
grep -r -i "test.*fix\|run.*test" .cursor/*/

# Check file names
find .cursor/*commands/ -name "*test*.md"
```

**Found**:
- `write-unit-tests.md` in `user-commands/`
- `write-integration-tests.md` in `backend-commands/`
- `run-all-tests-and-fix.md` in `user-commands/`

**Analysis**:
- `write-unit-tests.md` - Creates tests (different)
- `write-integration-tests.md` - Creates integration tests (different)
- `run-all-tests-and-fix.md` - ✅ Exact match!

**Decision**: ❌ Command already exists

---

### Example 3: Checking for Database Query Optimization

**Proposed Command**: Optimize slow database queries

**Search**:
```bash
# Search for database and optimization keywords
grep -r -i "database.*optim\|query.*optim\|optim.*query" .cursor/*/

# Check file names
find .cursor/*commands/ -name "*database*.md" -o -name "*query*.md" -o -name "*optim*.md"
```

**Found**: `optimize-database-queries.md` in `backend-commands/`

**Decision**: ❌ Command already exists

---

### Example 4: Checking for Go Error Handling

**Proposed Command**: Add comprehensive error handling to Go code

**Search**:
```bash
# Search in Go-specific commands
grep -r -i "error.*handl" .cursor/go-backend-commands/

# Check file names
find .cursor/go-backend-commands/ -name "*error*.md"
```

**Found**: `add-error-handling.md` in `go-backend-commands/`

**Decision**: ❌ Command already exists

---

### Example 5: New Command (No Duplicates)

**Proposed Command**: Generate database schema migration rollback scripts

**Search**:
```bash
# Search for migration and rollback keywords
grep -r -i "migration.*rollback\|rollback.*migration" .cursor/*/

# Check migration-related files
find .cursor/*commands/ -name "*migration*.md"
```

**Found**: `database-migration.md` in `backend-commands/`

**Analysis**:
- Existing command covers creating migrations
- Does NOT cover rollback scripts specifically
- Functionality is related but distinct

**Decision**: ⚠️ Evaluate options
- Option A: Extend `database-migration.md` with rollback section
- Option B: Create `database-migration-rollback.md` if scope is large

**Recommendation**: Extend existing command (rollback is part of migration workflow)

## Checklist

- [ ] Clearly defined proposed command purpose and keywords
- [ ] Searched all relevant directories
- [ ] Used multiple search strategies (keywords, filenames)
- [ ] Read potentially similar commands completely
- [ ] Assessed similarity level (high/medium/low/none)
- [ ] Made decision: use existing, extend existing, or create new
- [ ] If creating new despite similarities, documented differentiation
- [ ] Updated `.cursor/README.md` inventory if creating new command

## Tips

### Effective Keyword Selection

Choose keywords that capture:
- **Action verbs**: generate, create, optimize, analyze, fix, deploy
- **Domain terms**: API, database, test, security, docker, kubernetes
- **Technology**: REST, GraphQL, SQL, NoSQL, Go, Python
- **Output artifacts**: documentation, migration, report, diagram

### Comprehensive Search Strategy

1. **Keyword search** - Find content matches
2. **Filename search** - Find naming matches
3. **Title search** - Check command titles (first line)
4. **Full read** - Read complete command if potential match
5. **Cross-reference** - Check related directories

### Avoiding False Positives

Some keywords are too generic and will match many commands:
- "code", "file", "project", "feature"
- "add", "create", "update", "delete"
- "test", "check", "verify", "validate"

Use more specific combinations:
- Instead of "test" → "integration test" or "e2e test"
- Instead of "create" → "create API endpoint" or "create migration"
- Instead of "code" → "refactor code" or "review code"

## Related Commands

- `create-ai-command.md` - Use after confirming no similar command exists
- `refactor-cursor-commands.md` - Refactor if similar commands should be merged

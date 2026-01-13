# Test AI Command

## Overview

Test and validate an AI command's effectiveness before committing it to the repository. This ensures commands provide clear instructions, produce expected results, and follow repository conventions. Use this command to quality-check new commands or refactored existing ones.

## Steps

1. **Command Review**
    - Read the command file completely
    - Verify it follows the standard structure (Overview, Steps, Checklist)
    - Check markdown formatting is correct
    - Ensure filename uses kebab-case
    - Confirm it's in the appropriate category directory
2. **Clarity Assessment**
    - Verify the Overview clearly explains the command's purpose
    - Check if the use case is obvious and well-defined
    - Ensure Steps are logically ordered and sequential
    - Confirm each sub-step is specific and actionable
    - Validate that technical terminology is used correctly
3. **Completeness Check**
    - Verify all necessary steps are included
    - Check for coverage of edge cases and error scenarios
    - Ensure prerequisites are mentioned if any exist
    - Confirm the command covers the entire workflow
    - Validate the Checklist captures all verifiable outcomes
4. **Practical Testing**
    - Execute the command with Cursor AI assistant
    - Test with a realistic scenario or example
    - Verify the AI produces expected outputs
    - Check if instructions are clear enough for AI interpretation
    - Validate that the command produces consistent results
5. **Quality Validation**
    - Ensure imperative language is used consistently
    - Check for grammar and spelling errors
    - Verify technical accuracy of all statements
    - Confirm examples (if any) are correct and relevant
    - Validate that the command is project-agnostic (if in user-commands)
6. **Comparison with Similar Commands**
    - Review similar commands in the repository
    - Check for consistency in structure and style
    - Ensure no unnecessary duplication with existing commands
    - Verify the command adds unique value
    - Consider if it should be merged with or split from other commands
7. **Documentation Verification**
    - Confirm the command is listed in `.cursor/README.md`
    - Verify the description in README matches the Overview
    - Check that command counts are updated correctly
    - Ensure categorization is appropriate

## Test AI Command Checklist

### Structure & Format
- [ ] Command follows standard structure (Overview, Steps, Checklist)
- [ ] Markdown formatting is correct
- [ ] Filename uses kebab-case
- [ ] File is in appropriate category directory

### Content Quality
- [ ] Overview clearly explains purpose and use case
- [ ] Steps are logically ordered and sequential
- [ ] All sub-steps are specific and actionable
- [ ] Technical terminology is accurate
- [ ] Imperative language used consistently
- [ ] No grammar or spelling errors

### Completeness
- [ ] All necessary steps included
- [ ] Edge cases and error scenarios covered
- [ ] Prerequisites mentioned if applicable
- [ ] Entire workflow covered from start to finish
- [ ] Checklist captures all verifiable outcomes

### Practical Validation
- [ ] Tested with Cursor AI assistant
- [ ] Produces expected outputs
- [ ] Instructions clear for AI interpretation
- [ ] Results are consistent across tests
- [ ] Works with realistic scenarios

### Repository Integration
- [ ] No unnecessary duplication with existing commands
- [ ] Adds unique value to command library
- [ ] Consistent with similar commands in style
- [ ] Command is project-agnostic (if applicable)
- [ ] Listed in `.cursor/README.md` correctly

## Testing Examples

### Example 1: Testing a New Command
```markdown
Command: setup-monitoring.md
Test Scenario: Ask AI to set up monitoring for a web application
Expected Output: AI should propose monitoring stack, provide configuration files, explain setup steps
Result: ✓ AI understood requirements and provided comprehensive monitoring setup
```

### Example 2: Testing Edge Cases
```markdown
Command: database-migration.md
Test Scenario: Ask AI to create migration with potential data loss
Expected Output: AI should warn about data loss, ask for confirmation, provide rollback plan
Result: ✓ AI identified risks and requested explicit confirmation
```

### Example 3: Testing Clarity
```markdown
Command: debug-issue.md
Test Scenario: Present vague bug description to AI
Expected Output: AI should ask clarifying questions before debugging
Result: ✗ AI started debugging immediately without clarifying - command needs improvement
```

## Revision Guidelines

If testing reveals issues, update the command following these priorities:

1. **Critical Issues** (must fix before committing):
    - Incorrect technical information
    - Missing critical steps
    - Ambiguous instructions that confuse AI
    - Broken markdown formatting

2. **Important Issues** (should fix):
    - Incomplete edge case coverage
    - Unclear step ordering
    - Missing validation checkpoints
    - Inconsistent terminology

3. **Nice to Have** (optional improvements):
    - Additional examples
    - More detailed explanations
    - Better formatting
    - Enhanced cross-references

## Best Practices

- **Test Early**: Test commands during development, not just at the end
- **Real Scenarios**: Use realistic examples from actual projects
- **Multiple Contexts**: Test with different project types if command is generic
- **AI Perspective**: Think like the AI - is every instruction clear and unambiguous?
- **Iterate**: Commands often need 2-3 revision cycles to get right
- **Feedback Loop**: Collect feedback from actual usage and refine accordingly

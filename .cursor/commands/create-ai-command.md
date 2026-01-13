# Create AI Command

## Overview

Create a new AI command file following the repository's established patterns and conventions. This meta-command helps maintain consistency across all commands and ensures new commands are properly structured, documented, and categorized.

## Steps

1. **Command Planning**
    - Define the command's purpose and scope
    - Identify the target category (user-commands, backend-commands, frontend-commands, go-backend-commands, devops-commands, or commands)
    - Determine if the command is project-agnostic or project-specific
    - Verify no similar command already exists
2. **Category Selection**
    - **`user-commands/`**: Project-agnostic, reusable across tech stacks
    - **`backend-commands/`**: Language-agnostic backend development
    - **`frontend-commands/`**: Frontend/UI development
    - **`go-backend-commands/`**: Go-specific backend development
    - **`devops-commands/`**: DevOps and infrastructure management
    - **`commands/`**: Multi-stack, meta-commands, or doesn't fit other categories
3. **Command Structure**
    - Create clear and descriptive title (use title case)
    - Write concise Overview section (1-2 paragraphs explaining purpose and when to use)
    - Design actionable Steps section with numbered workflow and sub-steps
    - Build comprehensive Checklist section with verifiable items
4. **Content Guidelines**
    - Use imperative language for actions ("Create", "Verify", "Implement")
    - Include specific technical details and best practices
    - Add examples where helpful (code snippets, command examples)
    - Consider edge cases and common pitfalls
    - Make steps sequential and logical
5. **File Creation**
    - Use kebab-case for filename (e.g., `my-new-command.md`)
    - Place file in the appropriate category directory
    - Ensure proper markdown formatting
    - Validate all markdown syntax
6. **Documentation Update**
    - Add command entry to `.cursor/README.md` in the appropriate section
    - Include one-line description in the README
    - Update command counts in the README
    - Commit with clear commit message

## Create AI Command Checklist

- [ ] Command purpose and scope clearly defined
- [ ] Target category identified and validated
- [ ] Verified no similar command exists
- [ ] Overview section written (1-2 paragraphs)
- [ ] Steps section created with numbered workflow
- [ ] Checklist section includes all verifiable items
- [ ] Used imperative language and specific technical details
- [ ] Filename uses kebab-case format
- [ ] File placed in correct category directory
- [ ] Markdown formatting validated
- [ ] `.cursor/README.md` updated with new command entry
- [ ] Command counts updated in README
- [ ] Changes committed with clear message

## Command Template

```markdown
# Command Title

## Overview

Brief description of what this command does and when to use it. Explain the value it provides and the problem it solves. Keep it concise but informative.

## Steps

1. **First Major Step**
    - Specific action or check
    - Another specific action
    - Additional considerations or best practices
2. **Second Major Step**
    - Detailed sub-step
    - Another sub-step with technical details
    - Edge cases or warnings
3. **Third Major Step**
    - Implementation details
    - Validation steps
    - Quality checks

## Command Name Checklist

- [ ] Actionable item that can be verified
- [ ] Another verifiable checkpoint
- [ ] Specific outcome that can be confirmed
- [ ] Quality gate or validation
- [ ] Final verification step
```

## Best Practices

- **Clarity**: Every step should be clear and unambiguous
- **Actionability**: Users should know exactly what to do
- **Completeness**: Cover the entire workflow from start to finish
- **Flexibility**: Allow for different project contexts
- **Quality**: Include validation and quality checks
- **Examples**: Provide concrete examples when helpful
- **Maintenance**: Consider how the command will age and need updates

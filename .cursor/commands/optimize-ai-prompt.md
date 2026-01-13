# Optimize AI Prompt

## Overview

Optimize AI prompts to improve clarity, effectiveness, and result quality. This command helps refine prompts for better AI comprehension, more accurate outputs, and more consistent behavior. Use this for any prompt that isn't producing expected results or could be improved.

## Steps

1. **Prompt Analysis**
    - Read the current prompt completely
    - Identify the prompt's primary goal and success criteria
    - List all instructions and constraints in the prompt
    - Note any ambiguous or unclear sections
    - Identify implicit assumptions that should be explicit
2. **Clarity Enhancement**
    - Replace vague language with specific instructions
    - Use imperative verbs ("Create", "Analyze", "Generate", not "Should create", "Try to analyze")
    - Break long sentences into shorter, focused statements
    - Remove unnecessary words and filler phrases
    - Eliminate double negatives and complex conditionals
    - Define technical terms if they might be ambiguous
3. **Structure Improvement**
    - Organize prompt into logical sections
    - Use numbered lists for sequential steps
    - Use bullet points for options or requirements
    - Add clear section headers for different concerns
    - Place constraints and requirements prominently
    - Separate context from instructions
4. **Specificity Enhancement**
    - Add concrete examples where helpful
    - Specify output format expectations clearly
    - Define success criteria explicitly
    - Include edge cases and error handling instructions
    - Specify tone, style, or voice requirements
    - Add quantitative metrics where applicable (e.g., "3-5 examples", not "several examples")
5. **Context Optimization**
    - Provide necessary background information upfront
    - Remove irrelevant context that might distract
    - Clarify the user's role and AI's role
    - Specify any domain-specific knowledge needed
    - Define the scope and boundaries clearly
6. **Constraint Definition**
    - List all must-have requirements explicitly
    - Specify what to avoid or exclude
    - Define quality standards and validation criteria
    - Set limits on length, complexity, or scope
    - Clarify priorities when trade-offs are needed
7. **Testing & Validation**
    - Test prompt with AI and review outputs
    - Check if outputs meet success criteria
    - Verify AI understands all instructions
    - Test with edge cases and unusual inputs
    - Compare results before and after optimization
    - Iterate based on test results

## Optimize AI Prompt Checklist

### Clarity
- [ ] All instructions use imperative verbs
- [ ] No vague or ambiguous language
- [ ] Long sentences broken into focused statements
- [ ] Unnecessary words and filler removed
- [ ] No double negatives or complex conditionals
- [ ] Technical terms defined where needed

### Structure
- [ ] Prompt organized into logical sections
- [ ] Sequential steps use numbered lists
- [ ] Options/requirements use bullet points
- [ ] Clear section headers present
- [ ] Constraints placed prominently
- [ ] Context separated from instructions

### Specificity
- [ ] Concrete examples provided where helpful
- [ ] Output format specified clearly
- [ ] Success criteria defined explicitly
- [ ] Edge cases covered
- [ ] Tone/style requirements specified
- [ ] Quantitative metrics used (not vague terms)

### Context
- [ ] Necessary background provided upfront
- [ ] Irrelevant context removed
- [ ] User and AI roles clarified
- [ ] Domain knowledge specified
- [ ] Scope and boundaries defined

### Constraints
- [ ] Must-have requirements listed explicitly
- [ ] Exclusions and avoidances specified
- [ ] Quality standards defined
- [ ] Length/complexity limits set
- [ ] Trade-off priorities clarified

### Validation
- [ ] Tested with AI and outputs reviewed
- [ ] Outputs meet success criteria
- [ ] AI understands all instructions
- [ ] Edge cases tested
- [ ] Results improved from original

## Optimization Patterns

### Before → After Examples

**Example 1: Vague to Specific**
```
Before: "Help me improve the code quality."
After: "Refactor this code to:
1. Extract reusable functions
2. Eliminate duplication
3. Improve variable naming
4. Reduce nesting to max 2 levels
Provide the refactored code with explanations."
```

**Example 2: Ambiguous to Clear**
```
Before: "Can you maybe add some error handling?"
After: "Add comprehensive error handling:
- Check all function return values
- Validate all user inputs
- Wrap errors with context
- Return meaningful error messages"
```

**Example 3: Unstructured to Structured**
```
Before: "I need to create a feature that does X, Y, and Z but also handles A, B, and C, and don't forget about error cases."

After:
"Create a feature with the following requirements:

**Core Functionality:**
1. Implement X
2. Implement Y
3. Implement Z

**Additional Requirements:**
- Handle scenario A
- Handle scenario B
- Handle scenario C

**Error Handling:**
- Add validation for all inputs
- Provide clear error messages
- Implement graceful degradation"
```

**Example 4: Implicit to Explicit**
```
Before: "Write tests for this function."

After: "Write unit tests for this function:
- Test happy path with valid inputs
- Test edge cases (empty input, null, max values)
- Test error conditions
- Use the project's testing framework (Jest)
- Aim for 100% code coverage
- Follow Arrange-Act-Assert pattern"
```

## Optimization Techniques

### 1. Front-Load Important Information
Place critical instructions at the beginning where AI attention is strongest.

### 2. Use Formatting for Emphasis
- **Bold** for critical requirements
- `Code formatting` for technical terms
- > Blockquotes for warnings or important notes

### 3. Provide Decision Criteria
When AI needs to make choices, provide explicit criteria:
```
"Choose the appropriate data structure based on:
- Use arrays for sequential access
- Use hash maps for key-based lookup
- Use sets for uniqueness checking"
```

### 4. Chain of Thought Prompting
For complex tasks, ask AI to think step-by-step:
```
"Before implementing:
1. Analyze the requirements
2. List potential approaches
3. Evaluate trade-offs
4. Choose the best approach and explain why
5. Then implement the solution"
```

### 5. Constrain Output Format
Specify exact format for structured outputs:
```
"Provide your response in this format:
## Issue: [brief description]
## Root Cause: [analysis]
## Solution: [proposed fix]
## Code: [implementation]"
```

## Common Issues & Fixes

| Issue | Problem | Solution |
|-------|---------|----------|
| AI is verbose | Prompt doesn't constrain output | Add "Be concise. Limit explanation to 2-3 sentences per point." |
| AI misses requirements | Requirements buried in text | Use numbered list with one requirement per line |
| Inconsistent outputs | Prompt is ambiguous | Add concrete examples of expected output |
| AI asks too many questions | Context is missing | Provide necessary background upfront |
| AI ignores constraints | Constraints not prominent | Use bold text and place at the beginning |
| Off-topic responses | Scope not defined | Add explicit scope boundaries and exclusions |

## Best Practices

- **Iterate**: Good prompts evolve through multiple refinements
- **Test**: Always test optimized prompts with real scenarios
- **Measure**: Compare results before and after optimization
- **Document**: Keep track of what optimizations work well
- **Simplify**: When in doubt, make it simpler and more direct
- **Examples**: Concrete examples are often more effective than lengthy explanations
- **Consistency**: Use consistent terminology throughout the prompt

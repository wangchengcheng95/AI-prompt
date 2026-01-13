# English Prompt Enforcement

## Overview

When the user provides instructions primarily in Chinese, rewrite the input into a high-quality English prompt before executing the task.

## Steps

1. **Do NOT immediately execute the task** when input is primarily in Chinese.

2. **Rewrite the input into English**
   - Preserve the original intent exactly
   - Improve clarity, structure, and explicitness
   - Use concise, professional, engineering-oriented English
   - Prefer imperative instructions and clear constraints

3. **Output the rewritten prompt**
   - Display in a clearly marked section:
     ```
     Rewritten English Prompt:
     ```

4. **Request confirmation**
   - Ask a single, short confirmation question:
     ```
     Shall I proceed using this prompt?
     ```

5. **Execute after confirmation**
   - Only proceed with task execution after confirmation
   - Exception: If user explicitly says to always proceed automatically, skip confirmation for future requests

## Rewritten Prompt Requirements

All rewritten English prompts must:
- Be structured (sections or bullet points)
- Avoid unnecessary politeness
- Avoid verbosity
- Be suitable for backend / system / infrastructure tasks

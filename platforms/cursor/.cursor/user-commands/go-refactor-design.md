# Go Refactor: Design Patterns

## Overview

Refactor selected Go code to improve architecture using design patterns, SOLID principles, and high cohesion / low coupling.

> **Portability:** Project-agnostic. Follows GoF patterns adapted for Go idioms.

> ⚠️ **Cognitive Load Warning:** Apply patterns only when they **reduce** complexity. Never add patterns to demonstrate knowledge or "for future flexibility." Start simple; refactor to patterns when pain points emerge.

## Target

- `$SELECTION` — Selected code, file(s), or folder to refactor

## Code Smells to Identify

| Smell | Indicator |
|-------|-----------|
| God struct | Too many responsibilities, >7 fields/methods |
| Feature envy | Method uses other struct's data excessively |
| Primitive obsession | Overuse of primitives vs domain types |
| Shotgun surgery | One change requires edits across many files |
| Long parameter list | >4 parameters |
| Concrete dependencies | Depends on `*Type` instead of interface |
| Circular dependencies | Package A imports B, B imports A |

## SOLID Principles

| Principle | Go Implementation |
|-----------|-------------------|
| **SRP** | One struct = one reason to change. Split `UserService` → `AuthService` + `ProfileService` |
| **OCP** | Use interfaces for extension. Add new payment types without modifying `ProcessPayment()` |
| **LSP** | Implementations must honor interface contracts. No panics, no unexpected errors |
| **ISP** | Small interfaces (1-3 methods). Define at consumer, not provider |
| **DIP** | Depend on interfaces, inject via constructor. `repo UserRepository` not `*userRepo` |

## Design Patterns for Go

### Creational Patterns

| Pattern | Problem It Solves | Go Implementation |
|---------|-------------------|-------------------|
| **Factory Method** | Decouple creation from usage | `New*` constructor functions |
| **Abstract Factory** | Create families of related objects | Interface returning interfaces |
| **Builder** | Complex objects with many optional params | Functional options `WithTimeout()` |
| **Prototype** | Clone objects to avoid expensive init | `Clone()` method |
| **Singleton** | Single shared instance | `sync.Once` + package var |

### Structural Patterns

| Pattern | Problem It Solves | Go Implementation |
|---------|-------------------|-------------------|
| **Adapter** | Make incompatible interfaces work together | Wrapper struct |
| **Bridge** | Separate abstraction from implementation | Interface + injection |
| **Composite** | Treat leaf and composite uniformly | Interface + slice of same interface |
| **Decorator** | Add behavior without modifying original | Middleware, wrapper functions |
| **Facade** | Simplify complex subsystem | Aggregating struct |
| **Flyweight** | Share state among many objects | Shared cache/map |
| **Proxy** | Control access, add caching/logging | Wrapper implementing same interface |

### Behavioral Patterns

| Pattern | Problem It Solves | Go Implementation |
|---------|-------------------|-------------------|
| **Chain of Responsibility** | Pass request along handlers | Middleware chain |
| **Command** | Encapsulate request; support undo | `Execute()` + `Undo()` interface |
| **Iterator** | Sequential access without exposing structure | Channels or iterator interface |
| **Mediator** | Centralize communication | Coordinator struct |
| **Memento** | Save/restore state | Snapshot struct |
| **Observer** | Notify on state changes | Channels or callbacks |
| **State** | Behavior changes with internal state | State interface + context |
| **Strategy** | Interchangeable algorithms | Interface + multiple impls |
| **Template Method** | Algorithm skeleton with variable steps | Embedded struct + hooks |
| **Visitor** | Add operations without modifying objects | Visitor interface |

## ⚠️ Patterns to Use Sparingly

| Pattern | Why Sparingly | Go Alternative |
|---------|---------------|----------------|
| **Singleton** | Hidden global state; hard to test | Dependency injection |
| **Visitor** | Double dispatch; complex | Type switches |
| **Mediator** | Can become god object | Direct interfaces; event bus |
| **Prototype** | No deep copy built-in; error-prone | Factory functions |
| **Abstract Factory** | Over-engineering | Simple factory functions |
| **Template Method** | Awkward inheritance simulation | Strategy; function params |

### When NOT to Apply Patterns

- Small codebase — Keep it simple
- Single implementation — No interface needed
- No polymorphism required — Skip abstraction
- Performance-critical — Patterns add indirection
- Prototype/MVP stage — Get it working first

## Go-Idiomatic Shortcuts

| Situation | Skip Pattern? | Alternative |
|-----------|---------------|-------------|
| One-method interface with one impl | ✅ Skip | Plain function |
| Swap algorithms at runtime | ❌ Use Strategy | — |
| Many optional fields | ❌ Use Builder | Functional options |
| Add behavior without modifying | ❌ Use Decorator | Middleware |
| Async event notification | ✅ Skip Observer | Channels + goroutines |
| Type-safe collections | ✅ Skip Iterator | Generics |
| Deep hierarchy | ✅ Skip | Composition + `any` + type switch |
| Global shared resource | ⚠️ Avoid Singleton | Dependency injection |

**Key Go idioms:**
- Prefer plain functions over tiny one-method structs
- Prefer `any` + type assertion over deep hierarchies
- Prefer channels/pub-sub over classic Observer when async
- Prefer generics + constraints for reusable iterators/collectors

## High Cohesion / Low Coupling

### Cohesion Checklist
- [ ] All methods operate on struct's own data
- [ ] Package has single, clear purpose
- [ ] No "util" packages with unrelated functions
- [ ] Related functionality grouped together

### Coupling Checklist
- [ ] Depends on interfaces, not concrete types
- [ ] No circular dependencies
- [ ] No global state
- [ ] Services communicate via interfaces or events

## Refactoring Techniques

| Technique | When to Apply |
|-----------|---------------|
| **Extract Interface** | Need to decouple or mock |
| **Replace Conditional with Polymorphism** | Large type switches → Strategy pattern |
| **Introduce Parameter Object** | >4 parameters |
| **Extract Method** | Long function with distinct sections |

## Refactoring Checklist

### SOLID
- [ ] Single responsibility per struct
- [ ] New features via new types (not modifying existing)
- [ ] Interface implementations substitutable
- [ ] Interfaces small (1-3 methods)
- [ ] Dependencies injected via constructor

### Patterns Applied
- [ ] Factory functions for creation
- [ ] Functional options for complex config
- [ ] Strategy for interchangeable algorithms
- [ ] Decorator/middleware for cross-cutting concerns
- [ ] Facade for subsystem simplification

## Output Format

1. **Issues identified** — Code smells and design problems
2. **Patterns applied** — Which patterns and why
3. **Refactored code** — Complete, compilable Go code
4. **Dependency changes** — New interfaces or structural changes

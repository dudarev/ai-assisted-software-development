# Spec Branch Flow

**Spec Branch Flow** is a branching strategy designed to keep the `main` codebase clean while allowing for messy, iterative exploration of specifications, PRDs, and documentation in a parallel track.

## The Problem
Developing specifications (PRDs, design docs, rough notes) often involves rapid iteration, drafting, and "pollution" that shouldn't necessarily clutter the clean history of the `main` branch. Creating a new branch for every small spec change creates overhead, yet keeping them out of the repo makes them harder to reference during coding.

## The Solution: A Parallel Spec Branch

We maintain a long-lived branch named `spec` (or similar).

1.  **Pollution-Free Main**: The `main` branch remains pristine, containing only production-ready code.
2.  **Messy Spec Branch**: The `spec` branch contains everything in `main` **plus** the working drafts, experiments, and active specifications.
3.  **One-Way Sync**: We regularly merge `main` into `spec` to keep the specs compatible with the latest code. We **never** merge the entire `spec` branch back into `main`.


## The Workflow

1.  **Drafting**: Write and iterate on specs in the `spec` branch.
2.  **Feature Start**: When ready to implement a feature, create a `feature` branch from `main` (as usual).
3.  **Inject Spec**: Bring the relevant spec into your working context.
    *   Command: `git checkout spec -- path/to/spec.md`
    *   *AI Assistant Role*: Ask the AI to "Bring the spec for feature X," and it handles the checkout.
4.  **Implementation & Refinement**: Work on the code in the `feature` branch.
    *   **Crucial Step**: As you discover inconsistencies between the spec and reality (technical constraints, edge cases), **update the spec file directly in the feature branch**.
    *   This ensures the spec evolves from "what we thought we wanted" to "what we actually built."
5.  **Merge to Main**: Merge the `feature` branch into `main` *including* the updated spec file.
    *   This converts the spec from a "draft" into "system documentation."
6.  **Loop**: Irregularly sync `main` back into `spec` so the `spec` branch inherits the finalized, reality-tested documentation.

## Advantages
*   **Automatic Documentation**: By merging the spec, `main` always contains documentation that reflects the actual implementation, not just the initial wish-list.
*   **Efficiency**: Fixing specs in flight prevents the "stale documentation" problem without requiring context switching back to the `spec` branch during coding.
*   **Context Injection**: AI agents can easily pull context from the `spec` branch without user intervention.
*   **Separation of Concerns**: Humans can "think" in the `spec` branch and "build" in the `feature` branch.

## Flexibility
This flow is a guideline, not a strict rule.
*   If a spec is purely ephemeral (e.g., a rough brainstorm), you might choose *not* to commit it.
*   If a spec covers multiple features, you might check it out, partially implement it, and only commit the relevant sections.
*   Teams should adjust the "strictness" of the main-to-spec sync based on their cadence.


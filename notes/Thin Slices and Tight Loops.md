---
title: Thin Slices and Tight Loops
created: 2026-02-05
tags:
  - incrementalism
  - feedback-loops
  - cycle-time
  - risk-management
  - agile
  - ai-assisted-coding
  - publish
distilled_refs:
  - "[[distilled/20260104-204814Z--how-ai-will-change-software-engineering-with-martin-fowler.md]]"
---

# Thin Slices and Tight Loops

**Incrementalism** is the practice of **reducing batch size** so you can:
- learn sooner (faster feedback)
- reduce risk (smaller blast radius)
- keep options open (cheaper course-correction)

In AI-assisted work, the same idea becomes more important, not less: the tooling can generate *more* output faster, but that doesn’t make it *more trustworthy*.

## Core Idea

Build in **thin slices** and run a **tight loop**:
1. Decide the smallest slice that will teach you something real.
2. Specify only what you need to move forward (avoid “whole spec first”).
3. Implement the slice, verify it (tests + review), and integrate it.
4. Ship or stage it (flags if needed), observe, and repeat.

The goal is not “more output per cycle”; it’s **shorter cycle time** and **higher learning rate**.

## Why It Works (Even When It Feels Slower)

- **Learning is the work:** software development is largely discovering what you should build and how it behaves in reality.
- **Integration is where truth appears:** slices that don’t reach running code (or users) often create false confidence.
- **Risk scales superlinearly with batch size:** bigger changes hide more surprises and make rollback/recovery harder.

## AI-Specific Interpretation

Treat AI output like a high-throughput collaborator:
- Assume it can be helpful and fast.
- Assume it can be wrong in subtle ways.
- Keep slices small enough that humans can *actually* review and verify them.

Heuristic: prefer **more frequent, smaller slices** over “let the model generate a lot at once.”

## What Counts as a “Slice”

A slice is small enough that you can:
- review it carefully (diff-sized)
- test it meaningfully
- integrate it without destabilizing unrelated areas

Good slices are often **vertical** (user-visible capability end-to-end), but slices can also be risk-focused (e.g., one refactor that enables safer next steps).

## Common Failure Modes

- **Waterfall-by-prompt:** “big spec → big generated code dump → integrate later.”
- **Prototype-to-production drift:** exploratory code becomes the real system without a deliberate hardening step.
- **Fake slices:** lots of commits, but no working checkpoint or feedback.
- **Bigger-slice rationalization:** “AI is fast, so we can do more per cycle” (often increases review/verification debt).

## Practical Checks

- Can someone review this slice in ~15–30 minutes and explain what changed?
- Does the slice include the tests/checks needed to trust it?
- Is there a clear rollback/containment boundary (flags, canaries, limited scope)?
- After this slice, did we learn something we could not have known before?

---

## Related Notes

- [[Compounding Engineering Loop]]
- [[Three Developer Loops of Vibe Coding]]
- [[Loop-aware patterns and principles for AI-assisted software development]]
- [[Maker-Checker Pattern]]
- [[Executable Specs]]
- [[Measuring AI Assistant's Impact on Software Development Life Cycle]]

## References

- “How AI will change software engineering – with Martin Fowler” (interview). YouTube: https://www.youtube.com/watch?v=CQmI4XKTa0U

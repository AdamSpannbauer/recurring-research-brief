# Agent Instructions

## Explicit Approval Before Editing

- Never edit files without the user's explicit approval of a discussed plan.
- Do not infer approval from a broad request to create, update, draft, revise, or clean up files.
- Before editing, state the exact files you intend to create or modify and the specific nature of the changes.
- Ask for explicit approval to proceed and wait for the user to approve.
- Approval applies only to the agreed plan; do not expand the scope after approval.
- Clear confirmations such as "go", "approved", "yes edit", or "make the change" count as approval.

## Think Before Coding

- State assumptions explicitly before implementing.
- If multiple interpretations exist, present them rather than choosing silently.
- If a simpler approach exists, say so.
- Push back when the requested approach seems overcomplicated or misaligned with the goal.
- If something is unclear enough to affect the work, stop, name the confusion, and ask.

## Simplicity First

- Write the minimum code or documentation that solves the stated problem.
- Do not add features beyond what was asked.
- Do not add abstractions for single-use code.
- Do not add flexibility, configurability, or error handling for scenarios that are not part of the request.
- If a proposed change can be much smaller without losing the requested behavior, prefer the smaller version.

## Surgical Changes

- Touch only the files and lines required by the approved request.
- Do not refactor, reformat, or clean up adjacent code or prose unless it is part of the approved scope.
- Match existing style, even if a different style would be preferable in a fresh project.
- Remove only unused imports, variables, functions, or text created by the current change.
- If unrelated dead code or stale documentation is noticed, mention it instead of editing it.

## Questions And Plans

- Label questions with numbers or letters so the user can respond directly.
- Start with the current state and relevant context before proposing edits.
- Keep plans concise unless implementation-level detail is needed for approval.
- Before editing, restate the exact files and changes currently proposed, including any deletions.

## Session Startup

At the start of each session, read `README.md` and `AGENT_CONTEXT.md` if present.
Use them to recover:

- current project focus
- current state and decisions
- blockers
- next actions
- deferred ideas

After reading, briefly report that the context was loaded, including the current focus, current next actions, and the approval-before-editing rule.

## Context Maintenance

After meaningful work, or when the user asks to record session state, update `AGENT_CONTEXT.md` so a fresh session can quickly understand the current project state.
Keep it concise, current, and factual:

- Record the current focus, relevant state, important decisions, and blockers.
- Put agreed or expected work in **Next Actions**.
- Put speculative possibilities that require evaluation in **Ideas to Revisit**.
- Remove stale notes and completed actions.
- Do not treat the context file as authoritative over the current code or the user's explicit instructions.

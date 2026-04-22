# Daily Reflection Tree — DT Fellowship Assignment

> *A deterministic end-of-day reflection tool for employees. No LLM at runtime. Fully auditable. Every path traceable.*

---

## Repository Structure

```
/tree/
  reflection-tree.json      ← Part A: the complete tree data (33 nodes)
  tree-diagram.md           ← Part A: visual Mermaid diagram + path legend

/agent/
  agent.py                  ← Part B: CLI agent (Python 3, no dependencies)

/transcripts/
  persona-1-transcript.md   ← Victor / Contributor / Altrocentric path
  persona-2-transcript.md   ← Victim / Entitled / Self-Centric path (+ contrast table)

write-up.md                 ← Design rationale (2 pages)
README.md                   ← This file
```

---

## Part A — Reading the Tree

The tree lives in `tree/reflection-tree.json`. It is human-readable without running any code.

**Node types and what they do:**

| Type | Employee sees | Auto-advances? |
|------|--------------|----------------|
| `start` | Greeting | Yes → first question |
| `question` | Question + fixed options | No — waits for selection |
| `decision` | Nothing (internal routing) | Yes — evaluates rules, picks branch |
| `reflection` | Insight/reframe based on path | Yes — after employee continues |
| `bridge` | Axis-transition statement | Yes → next axis opening |
| `summary` | End-of-session synthesis using path data | Yes — after employee reads |
| `end` | Closing message | Session ends |

**How to trace a path manually:**

1. Start at node `"id": "START"`.
2. Follow `"target"` or `"parentId"` chains.
3. At `decision` nodes, evaluate the `"options"` rules top-to-bottom — first matching rule wins.
4. At `question` nodes, the selected option determines the signal recorded and feeds the next decision node.
5. Reflections use `{node_id.answer}` and `{axis.dominant}` interpolation.
6. `SUMMARY` selects a `summary_templates` entry using the key `{axis1_dominant}_{axis2_dominant}_{axis3_dominant}`.

**Node counts:**

| Type | Count |
|------|-------|
| start / end | 2 |
| question | 11 |
| decision | 8 |
| reflection | 7 |
| bridge | 2 |
| summary | 1 |
| **Total** | **33** |

---

## Part B — Running the Agent

**Requirements:** Python 3.7+, no external packages.

```bash
# From repo root
python agent/agent.py
```

The agent will load `tree/reflection-tree.json` automatically and walk you through the session in your terminal.

**What the agent does:**
- Loads the tree from the JSON file (not hardcoded)
- Renders each node with appropriate formatting and pacing
- Waits for input at `question` nodes, auto-advances at all others
- Accumulates axis signals as you answer
- Interpolates your earlier answers into reflection text
- Selects the correct summary template from your profile
- Prints your path at the end of the session

---

## The Three Axes

| Axis | Spectrum | Source Psychology |
|------|---------|-------------------|
| 1 — Locus | Victim (external) ↔ Victor (internal) | Rotter (1954), Dweck (2006) |
| 2 — Orientation | Entitlement ↔ Contribution | Campbell et al. (2004), Organ (1988) |
| 3 — Radius | Self-Centric ↔ Altrocentric | Maslow (1969), Batson (2011) |

---

## Design Principles

1. **No LLM at runtime.** The tree is a static data file walked by simple rule evaluation. Same answers always produce the same path and the same reflection.
2. **Fixed options only.** Every question has 3–4 predefined choices. This forces the designer (me) to model the full spectrum, not delegate it to a model.
3. **No moralizing.** Every reflection is written to meet the employee where they are. The "victim/entitled/self-centric" path ends with honesty and a forward-facing question — not shame.
4. **Interpolation, not generation.** Reflections feel personal because they embed your own words back to you. This is string templating, not AI generation.
5. **Axes flow as a sequence.** Axis 3's opening references the framing established in Axis 1. The conversation builds.

---

## Sample Paths

See `/transcripts/` for full annotated runs.

| Persona | Axis 1 | Axis 2 | Axis 3 | Summary template |
|---------|--------|--------|--------|-----------------|
| Priya | internal | contribution | altrocentric | *"A complete day — even if outcomes were imperfect."* |
| Rajan | external | entitlement | self | *"What would shift if, just once tomorrow, you looked for one choice and one person to help?"* |

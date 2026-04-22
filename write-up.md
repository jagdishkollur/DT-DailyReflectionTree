# Design Write-Up — Daily Reflection Tree
 
**Assignment:** DT Fellowship — Daily Reflection Tree  

---

## Why These Questions

The hardest constraint in this assignment is not the branching logic — it's writing questions that *a tired person at 7pm would actually answer honestly*. Most reflection surveys fail because they ask people to perform insight rather than arrive at it. I designed around three principles:

**1. Concrete before abstract.** Instead of asking "Do you have an internal locus of control?", I ask "When something worked today, what's the honest reason it worked?" The abstract concept is smuggled in through a concrete question. The employee doesn't know they're answering a Rotter-scale item; they think they're just describing their day.

**2. The options must be genuinely hard to choose between.** The Axis 2 opening question offers four options that span a real spectrum — from clearly generous to clearly entitled. They're not trick questions and they're not loaded. Each option is something a real person at a real company actually thinks. If I wrote the options well, there's a moment of uncomfortable recognition when someone reads option C or D.

**3. No option should feel shameful to choose.** The assignment brief was explicit: this isn't a grading tool. Someone who picks "I was waiting to be noticed" should feel seen, not judged. The reflection that follows has to meet them where they are without moralizing — "There's nothing wrong with wanting recognition" is the opening, not a closing caveat.

---

## How I Designed the Branching

The tree has three levels of branching decision:

**Level 1 — Day framing (opening):** The first question ("If today were a chapter...") routes to either the agency-high or agency-low question track. This is a gentle proxy — people who frame the day positively are more likely to be in an agentive state, but the follow-up still tests the hypothesis. It doesn't assume; it steers.

**Level 2 — Per-axis signal accumulation:** Each question node tags a signal (e.g., `axis1:internal`). After two questions per axis, the tree checks the dominant signal — not just the last answer — to route to the reflection. This prevents a single question from fully determining the path, which reduces the feeling that the system "knows" you from one answer.

**Level 3 — Summary template selection:** The final summary chooses from 8 pre-written templates based on the 3-axis profile (e.g., `internal_contribution_altrocentric`). Each template is tuned to affirm what's working and point — once, lightly — at the next edge. The templates were the hardest thing to write. The constraint was: must feel specific to the profile, must not lecture, must end with possibility rather than deficit.

**Trade-offs I made:**

- I chose depth over breadth. 2 substantive questions per axis produces more insight than 5 shallow ones. The assignment minimum was 2/axis; I stayed at that floor intentionally.
- I kept the Axis 3 question directly linked to the Axis 1 answer via interpolation. Someone who framed the day as "The Day Things Fell Apart" sees that exact phrase reflected back in their Axis 1 reflection. This creates continuity — the conversation feels like *one conversation* rather than three surveys stitched together.
- Decision nodes are invisible. The employee never sees "you answered X, so now we ask Y." The routing is embedded in the question sequencing. This preserves the feeling of a natural flow.

---

## Psychological Sources

**Axis 1 — Locus of Control (Rotter, 1954):** Rotter's original Internal-External Locus of Control scale used forced-choice items between internal and external attributions. My questions follow the same logic but avoid his clinical framing. The critical insight from Dweck's work (Mindset, 2006) that I incorporated: it's not just *whether* someone had agency, but whether they *saw it as actionable*. That's why the second Axis 1 question asks "Did you see a choice you had?" rather than "Did you have a choice?" — the perception is what matters for growth.

**Axis 2 — Entitlement vs OCB (Campbell et al., 2004; Organ, 1988):** Psychological entitlement is often invisible to its holder. Organ's OCB framework distinguishes between *formal* job performance and *discretionary* citizenship behavior — going beyond the role. The key insight I embedded: entitlement and contribution aren't opposites on a single axis; they can coexist. Someone can genuinely contribute and still feel underrecognized. The Axis 2 question sequence is designed to surface this nuance without collapsing it to a binary.

**Axis 3 — Self-Transcendence (Maslow, 1969):** Maslow's posthumously integrated work placed self-transcendence above self-actualization on his hierarchy. The shift from "what do I need?" to "what does the world need from me?" correlates with both meaning and psychological resilience. Batson's (2011) work on perspective-taking informed the Axis 3 question design — the options range from purely self-referential (A: "Just me") to fully other-oriented (D: "The customer/end user"), mirroring his empathy continuum. The reflection for the altrocentric path quotes Maslow directly because it's specific, true, and grounding.

---

## What I'd Improve With More Time

**1. Temporal tracking.** The most valuable version of this tool tracks the same employee over 30 days and surfaces patterns: "This is the third week in a row you've leaned external on Axis 1 after meetings with your manager." That's not possible in a single session tree, but the data structure (signals + path log) is designed to support it.

**2. More nuanced Axis 2 branching.** The current tree has a three-way branch at A2 (contribution / neutral / entitlement) but the neutral path converges quickly. A better design would hold the neutral path longer — asking "what would it have taken for you to give more today?" before merging.

**3. A check-in node at the end of Axis 1 for employees who say "I'm not sure" to the agency question.** Currently this routes to the external path, which is a reasonable default but not always accurate. A dedicated "uncertainty" branch that asks a clarifying question before routing would improve fidelity.

**4. Edge-case testing.** I built two personas (Priya and Rajan), but a real QA process would walk 8-12 personas through all combinations to verify every SUMMARY template fires correctly and no path dead-ends.

---

*Total nodes: 33 | Question nodes: 11 | Decision nodes: 8 | Reflection nodes: 7 | Bridge nodes: 2 | Summary: 1 | Start/End: 2*

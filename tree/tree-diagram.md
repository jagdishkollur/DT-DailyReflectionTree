# Daily Reflection Tree — Visual Diagram

```mermaid
flowchart TD
    START([🌙 START\nGood evening. Take a breath.])
    START --> A1_OPEN

    A1_OPEN{A1_OPEN\nIf today were a chapter —\nwhat would its title be?}
    A1_OPEN -- Held Together / Surprised Myself --> A1_D1_HIGH[A1_D1 decision]
    A1_OPEN -- Things Fell Apart / Just Another Day --> A1_D1_LOW[A1_D1 decision]

    A1_D1_HIGH --> A1_Q_AGENCY_HIGH{A1_Q_AGENCY_HIGH\nWhen something worked today,\nwhat is the honest reason?}
    A1_D1_LOW --> A1_Q_AGENCY_LOW{A1_Q_AGENCY_LOW\nWhen things got difficult,\nwhat was your first instinct?}

    A1_Q_AGENCY_HIGH -- Prepared / Adjusted --> A1_D2a[decision]
    A1_Q_AGENCY_HIGH -- Someone else / Just happened --> A1_D2b[decision]
    A1_Q_AGENCY_LOW -- Figure out control / Push through --> A1_D2c[decision]
    A1_Q_AGENCY_LOW -- Wait / Frustrated --> A1_D2d[decision]

    A1_D2a --> A1_Q2_INT
    A1_D2c --> A1_Q2_INT
    A1_D2b --> A1_Q2_EXT
    A1_D2d --> A1_Q2_EXT

    A1_Q2_INT{A1_Q2_INT\nDid you see a choice\nyou had today?}
    A1_Q2_EXT{A1_Q2_EXT\nLooking back — what was\nwithin your influence?}

    A1_Q2_INT --> A1_D3[axis1 signal tally]
    A1_Q2_EXT --> A1_D3

    A1_D3 -- internal dominant --> A1_R_INT[/A1_R_INT\nYou kept showing up as\nsomeone with a hand in\nwhat happened./]
    A1_D3 -- external dominant --> A1_R_EXT[/A1_R_EXT\nBuried in that day was\na sliver of choice.\nYou're seeing it now./]

    A1_R_INT --> BRIDGE_1_2
    A1_R_EXT --> BRIDGE_1_2

    BRIDGE_1_2([BRIDGE 1→2\nNow let's look at the\ndirection of your energy.])
    BRIDGE_1_2 --> A2_OPEN

    A2_OPEN{A2_OPEN\nThink of a specific interaction.\nWhich feels most honest?}
    A2_OPEN -- Gave without being asked --> A2_Q_CONTRIB
    A2_OPEN -- Did what was expected --> A2_Q_NEUTRAL
    A2_OPEN -- Waiting to be noticed / Unfair distribution --> A2_Q_ENTITLE

    A2_Q_CONTRIB{A2_Q_CONTRIB\nWhen you gave that effort —\nwhat was the pull behind it?}
    A2_Q_NEUTRAL{A2_Q_NEUTRAL\nWas there a moment you\ncould have given more?}
    A2_Q_ENTITLE{A2_Q_ENTITLE\nThat feeling of imbalance —\ndid you do anything with it?}

    A2_Q_CONTRIB --> A2_Q2_COMMON
    A2_Q_NEUTRAL --> A2_Q2_COMMON
    A2_Q_ENTITLE --> A2_Q2_COMMON

    A2_Q2_COMMON{A2_Q2_COMMON\nIf a colleague described your\ncontribution today — what would\nthey most accurately say?}

    A2_Q2_COMMON -- Helped team / Solid work --> A2_D2a[decision]
    A2_Q2_COMMON -- Focused on own work / Frustrated --> A2_D2b[decision]

    A2_D2a --> A2_R_CONTRIB[/A2_R_CONTRIB\nSmall acts of contribution\nthat no one mandated.\nThat's what culture is made of./]
    A2_D2b --> A2_R_ENTITLE[/A2_R_ENTITLE\nThere's nothing wrong with\nwanting recognition. Tomorrow\nis still available./]

    A2_R_CONTRIB --> BRIDGE_2_3
    A2_R_ENTITLE --> BRIDGE_2_3

    BRIDGE_2_3([BRIDGE 2→3\nAlmost done. Who else\nwas in the picture today?])
    BRIDGE_2_3 --> A3_OPEN

    A3_OPEN{A3_OPEN\nThinking about today's biggest\nchallenge — who comes to mind first?}
    A3_OPEN -- Just me --> A3_Q_SELF
    A3_OPEN -- My team --> A3_Q_TEAM
    A3_OPEN -- Colleague / Customer --> A3_Q_WIDE

    A3_Q_SELF{A3_Q_SELF\nWas someone else's difficulty\nvisible to you today?}
    A3_Q_TEAM{A3_Q_TEAM\nDid you act on that sense of\nbeing in it together — or just feel it?}
    A3_Q_WIDE{A3_Q_WIDE\nDid that wider awareness\nchange how you worked today?}

    A3_Q_SELF --> A3_D2
    A3_Q_TEAM --> A3_D2
    A3_Q_WIDE --> A3_D2

    A3_D2[axis3 signal tally]
    A3_D2 -- self dominant --> A3_R_SELF[/A3_R_SELF\nCarrying your own weight\nis real work. Is there one\nperson you could notice tomorrow?/]
    A3_D2 -- team dominant --> A3_R_TEAM[/A3_R_TEAM\nYou hold the team in awareness.\nThe next step: does it\nbecome action?/]
    A3_D2 -- altrocentric dominant --> A3_R_WIDE[/A3_R_WIDE\nThe most resilient people\norient beyond themselves.\nYou found that today./]

    A3_R_SELF --> SUMMARY
    A3_R_TEAM --> SUMMARY
    A3_R_WIDE --> SUMMARY

    SUMMARY[/SUMMARY\nToday you called it {A1_OPEN.answer}.\nOn agency: {axis1.dominant}\nOn contribution: {axis2.dominant}\nOn radius: {axis3.dominant}\n{summary_reflection}/]
    SUMMARY --> END([🌙 END\nSee you tomorrow.\nGet some rest.])

    style START fill:#1a1a2e,color:#e0e0ff,stroke:#6c63ff
    style END fill:#1a1a2e,color:#e0e0ff,stroke:#6c63ff
    style BRIDGE_1_2 fill:#16213e,color:#a0c4ff,stroke:#4895ef
    style BRIDGE_2_3 fill:#16213e,color:#a0c4ff,stroke:#4895ef
    style SUMMARY fill:#0f3460,color:#e0e0ff,stroke:#e94560
    style A1_R_INT fill:#1b4332,color:#d8f3dc,stroke:#52b788
    style A1_R_EXT fill:#1b4332,color:#d8f3dc,stroke:#52b788
    style A2_R_CONTRIB fill:#1b4332,color:#d8f3dc,stroke:#52b788
    style A2_R_ENTITLE fill:#1b4332,color:#d8f3dc,stroke:#52b788
    style A3_R_SELF fill:#1b4332,color:#d8f3dc,stroke:#52b788
    style A3_R_TEAM fill:#1b4332,color:#d8f3dc,stroke:#52b788
    style A3_R_WIDE fill:#1b4332,color:#d8f3dc,stroke:#52b788
```

## Node Legend

| Shape | Meaning |
|-------|---------|
| `([...])` | Start / End / Bridge — auto-advances |
| `{...}` | Question — waits for user input |
| `[decision]` | Decision — internal routing, invisible to user |
| `[/.../ ]` | Reflection / Summary — user reads, then continues |

## Possible Conversation Paths

The tree has **3 primary branching axes**, each with 2-3 paths, producing **12+ distinct conversation flows**. All paths converge at SUMMARY.

Key path examples:
- **Victor / Contributor / Altrocentric**: A1_Q_AGENCY_HIGH → A1_Q2_INT → A1_R_INT → A2_Q_CONTRIB → A2_R_CONTRIB → A3_Q_WIDE → A3_R_WIDE → SUMMARY (template: *internal_contribution_altrocentric*)
- **Victim / Entitled / Self-Centric**: A1_Q_AGENCY_LOW → A1_Q2_EXT → A1_R_EXT → A2_Q_ENTITLE → A2_R_ENTITLE → A3_Q_SELF → A3_R_SELF → SUMMARY (template: *external_entitlement_self*)
```

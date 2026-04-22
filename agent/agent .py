#!/usr/bin/env python3
"""
Daily Reflection Tree — CLI Agent v1.1
Loads reflection-tree.json and walks the employee through the session.
No LLM calls at runtime. Fully deterministic. Routing is target-based only.
"""

import json, os, sys, time
from textwrap import fill, indent

RESET="\033[0m"; BOLD="\033[1m"; DIM="\033[2m"; CYAN="\033[96m"
GREEN="\033[92m"; YELLOW="\033[93m"; PURPLE="\033[95m"; BLUE="\033[94m"; WHITE="\033[97m"
WIDTH=72

def wrap(text, pad=4):
    return "\n".join(indent(fill(l, WIDTH-pad), " "*pad) if l.strip() else "" for l in text.split("\n"))

def hr(char="─", c=DIM): print(f"{c}{char*WIDTH}{RESET}")
def pause(msg="  Press Enter to continue…", c=DIM): input(f"\n{c}{msg}{RESET}\n")

def slow_print(text, delay=0.016):
    for ch in text: sys.stdout.write(ch); sys.stdout.flush(); time.sleep(delay)
    print()

def load_tree(path):
    with open(path) as f: data = json.load(f)
    return {n["id"]: n for n in data["nodes"]}, data.get("meta", {})

class State:
    def __init__(self, axis_labels):
        self.answers = {}
        self.signals = {"axis1":{"internal":0,"external":0},"axis2":{"contribution":0,"entitlement":0},"axis3":{"self":0,"altrocentric":0}}
        self.axis_labels = axis_labels
        self.path = []

    def record_signal(self, s):
        if not s: return
        ax, pole = s.split(":")
        self.signals[ax][pole] += 1

    def dominant(self, axis):
        return max(self.signals[axis], key=self.signals[axis].get)

    def label(self, axis):
        return self.axis_labels.get(axis, {}).get(self.dominant(axis), self.dominant(axis))

    def summary_key(self):
        return f"{self.dominant('axis1')}_{self.dominant('axis2')}_{self.dominant('axis3')}"

    def interpolate(self, text):
        for nid, val in self.answers.items():
            text = text.replace("{"+nid+".answer}", val)
        for axis in self.signals:
            text = text.replace("{"+axis+".dominant}", self.dominant(axis))
            text = text.replace("{"+axis+".label}", self.label(axis))
        return text

def evaluate_decision(node, state):
    last = list(state.answers.values())[-1] if state.answers else ""
    for rule in node["options"]:
        if rule.startswith("answer="):
            rest = rule[len("answer="):]
            vals_part, target = rest.rsplit(":", 1)
            if last in vals_part.split("|"): return target
        elif rule.startswith("signal="):
            rest = rule[len("signal="):]
            sig_part, target = rest.rsplit(":", 1)
            axis, pole = sig_part.split(":")
            if state.dominant(axis) == pole: return target
    return node["options"][-1].rsplit(":", 1)[-1]

def run_start(node, state):
    os.system("clear" if os.name=="posix" else "cls")
    hr("═", PURPLE); print(f"\n{PURPLE}{BOLD}  🌙  Daily Reflection Tree{RESET}\n"); hr("═", PURPLE); print()
    slow_print(wrap(node["text"]), 0.012); print(); pause()
    return node["target"]

def run_bridge(node, state):
    hr(c=BLUE); print()
    slow_print(f"{BLUE}{wrap(node['text'])}{RESET}", 0.015); print(); pause()
    return node["target"]

def run_question(node, state):
    hr(); print()
    print(f"{WHITE}{BOLD}{wrap(state.interpolate(node['text']), pad=2)}{RESET}\n")
    opts = node["options"]
    for i, o in enumerate(opts, 1): print(f"  {CYAN}{BOLD}[{i}]{RESET}  {o}")
    print()
    while True:
        raw = input(f"  {DIM}Your choice (1–{len(opts)}): {RESET}").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(opts):
            state.answers[node["id"]] = opts[int(raw)-1]
            state.record_signal(node.get("signal"))
            return node["target"]
        print(f"  {YELLOW}Please enter a number between 1 and {len(opts)}.{RESET}")

def run_reflection(node, state):
    os.system("clear" if os.name=="posix" else "cls")
    hr("·", GREEN); print(f"\n{GREEN}{BOLD}  ✦  Reflection{RESET}\n")
    slow_print(f"{GREEN}{wrap(state.interpolate(node['text']))}{RESET}", 0.014); print(); pause()
    return node["target"]

def run_summary(node, state):
    os.system("clear" if os.name=="posix" else "cls")
    hr("═", PURPLE); print(f"\n{PURPLE}{BOLD}  ✦  Today's Reflection{RESET}\n"); hr("═", PURPLE); print()
    key = state.summary_key()
    sr = node.get("summary_templates", {}).get(key, "Every day is data. You showed up.")
    text = state.interpolate(node["text"]).replace("{summary_reflection}", sr)
    slow_print(f"{WHITE}{wrap(text)}{RESET}", 0.013); print(); hr(c=DIM)
    shown = " → ".join(state.path[:9]) + ("…" if len(state.path) > 9 else "")
    print(f"\n  {DIM}Path: {shown}{RESET}\n")
    pause("  Press Enter to close your session…")
    return node["target"]

def run_end(node, state):
    hr("═", PURPLE); print()
    slow_print(f"{PURPLE}{BOLD}{wrap(node['text'])}{RESET}", 0.015); print(); hr("═", PURPLE); print()

def walk(nodes):
    axis_labels = nodes.get("SUMMARY", {}).get("axis_labels", {})
    state = State(axis_labels)
    current_id = "START"
    dispatch = {"start":run_start,"bridge":run_bridge,"question":run_question,
                "reflection":run_reflection,"summary":run_summary}
    while current_id:
        node = nodes[current_id]
        state.path.append(current_id)
        ntype = node["type"]
        if ntype == "decision":
            current_id = evaluate_decision(node, state)
        elif ntype == "end":
            run_end(node, state); break
        elif ntype in dispatch:
            current_id = dispatch[ntype](node, state)
        else:
            current_id = node.get("target")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tree", "reflection-tree.json")
    if not os.path.exists(path):
        print(f"Error: tree file not found at {path}"); sys.exit(1)
    nodes, meta = load_tree(path)
    print(f"\n  Loaded '{meta.get('name','Tree')}' v{meta.get('version','?')} — {len(nodes)} nodes\n")
    time.sleep(0.8)
    walk(nodes)

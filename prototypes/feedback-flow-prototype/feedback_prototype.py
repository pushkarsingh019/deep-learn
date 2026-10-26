#!/usr/bin/env python3
"""
PROTOTYPE — throw away after the feedback state model is validated.

Question: Does automatic lesson snapshotting plus explicit keep, friction,
revision, rejection, and blind-comparison actions feel controllable enough to
collect useful personalization data without silently inferring preferences?
Nothing in this prototype is written to disk.
"""

import json
import sys
from feedback_logic import export_preview, initial_state, reduce

BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"
CLEAR = "\033[2J\033[H"


def compact_state(state):
    records = []
    for record in state["records"]:
        if record["kind"] == "episode":
            records.append({
                "id": record["id"],
                "kind": "episode",
                "lesson": record["lesson"],
                "disposition": record["disposition"],
                "friction": record["friction"],
                "revision": record["revision"],
            })
        else:
            records.append(record)
    return {
        "capture_policy": state["capture_policy"],
        "records": records,
        "export_preview": export_preview(state),
        "notice": state["notice"],
    }


def render(state, clear=True):
    if clear:
        print(CLEAR, end="")
    print(f"{BOLD}DEEP LEARN FEEDBACK — LOGIC PROTOTYPE{RESET}")
    print(f"{DIM}In memory only. No files are being saved.{RESET}\n")
    print(json.dumps(compact_state(state), indent=2, ensure_ascii=False))
    print(
        f"\n{BOLD}[n]{RESET} new lesson  {BOLD}[k]{RESET} keep  "
        f"{BOLD}[f]{RESET} friction  {BOLD}[r]{RESET} revised  "
        f"{BOLD}[x]{RESET} reject\n"
        f"{BOLD}[c]{RESET} compare  {BOLD}[a]{RESET}/{BOLD}[b]{RESET}/{BOLD}[0]{RESET} prefer  "
        f"{BOLD}[d]{RESET} forget latest  {BOLD}[e]{RESET} export preview  "
        f"{BOLD}[q]{RESET} quit"
    )


def ask(label, default=""):
    suffix = f" [{default}]" if default else ""
    value = input(f"{label}{suffix}: ").strip()
    return value or default


def interactive():
    state = initial_state()
    while True:
        render(state)
        command = input("\nAction: ").strip().lower()
        if command == "q":
            return
        if command == "n":
            state = reduce(state, {"type": "capture", "lesson": ask("Lesson title")})
        elif command == "k":
            state = reduce(state, {"type": "keep", "reason": ask("Why keep it", "I would continue reading")})
        elif command == "f":
            state = reduce(state, {"type": "friction", "passage": ask("Exact passage"), "reason": ask("Why it caused friction")})
        elif command == "r":
            state = reduce(state, {"type": "revise", "revision": ask("What your revision changed")})
        elif command == "x":
            state = reduce(state, {"type": "reject", "reason": ask("Why reject it")})
        elif command == "c":
            state = reduce(state, {
                "type": "compare",
                "topic": ask("Topic"),
                "A": ask("Candidate A description"),
                "B": ask("Candidate B description"),
            })
        elif command in {"a", "b", "0"}:
            choice = {"a": "A", "b": "B", "0": "neither"}[command]
            state = reduce(state, {"type": "prefer", "choice": choice, "reason": ask("Why")})
        elif command == "d":
            state = reduce(state, {"type": "forget"})
        elif command == "e":
            state["notice"] = "Export preview: " + json.dumps(export_preview(state))
        else:
            state["notice"] = "Unknown action."


def demo():
    state = initial_state()
    actions = [
        {"type": "capture", "lesson": "Why learn the solver itself?"},
        {
            "type": "friction",
            "passage": "This distinction is the heart of the paper.",
            "reason": "It announces importance instead of letting the explanation earn it.",
        },
        {
            "type": "revise",
            "revision": "Replaced the announcement with a concrete contrast in continuous prose.",
        },
        {
            "type": "compare",
            "topic": "Opening the next lesson",
            "A": "Begins with one physical situation and develops it as an essay.",
            "B": "Begins with objectives, definitions, and a notation table.",
        },
        {
            "type": "prefer",
            "choice": "A",
            "reason": "I would keep reading; B feels like generated courseware.",
        },
    ]

    render(state, clear=False)
    for index, action in enumerate(actions, 1):
        state = reduce(state, action)
        print(f"\n{'=' * 72}\nDEMO ACTION {index}: {action['type']}\n")
        render(state, clear=False)


if __name__ == "__main__":
    if "--demo" in sys.argv:
        demo()
    else:
        interactive()

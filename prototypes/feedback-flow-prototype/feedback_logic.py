"""Pure state transitions for the throwaway feedback-flow prototype."""

from copy import deepcopy


def initial_state():
    return {
        "prototype": True,
        "capture_policy": {
            "lesson_snapshots": "automatic after Deep Learn writes a lesson",
            "preference_labels": "explicit only",
            "persistence": "none in this prototype",
        },
        "records": [],
        "notice": "Ready. Simulate a generated lesson or a blind comparison.",
    }


def _next_id(state, prefix):
    count = sum(record["id"].startswith(prefix) for record in state["records"])
    return f"{prefix}{count + 1:03d}"


def _latest(state, kind=None):
    for record in reversed(state["records"]):
        if kind is None or record["kind"] == kind:
            return record
    return None


def reduce(state, action):
    """Return a new state after one user-visible action."""
    next_state = deepcopy(state)
    kind = action["type"]

    if kind == "capture":
        record = {
            "id": _next_id(next_state, "E"),
            "kind": "episode",
            "lesson": action["lesson"],
            "snapshot": action.get("snapshot", "generated lesson snapshot"),
            "disposition": "unrated",
            "friction": [],
            "revision": None,
        }
        next_state["records"].append(record)
        next_state["notice"] = f'{record["id"]} captured automatically; no preference inferred.'

    elif kind in {"keep", "reject"}:
        episode = _latest(next_state, "episode")
        if not episode:
            next_state["notice"] = "No lesson episode exists yet."
        else:
            episode["disposition"] = kind
            episode["reason"] = action.get("reason", "")
            next_state["notice"] = f'{episode["id"]} explicitly marked {kind}.'

    elif kind == "friction":
        episode = _latest(next_state, "episode")
        if not episode:
            next_state["notice"] = "No lesson episode exists yet."
        else:
            episode["friction"].append({
                "passage": action["passage"],
                "reason": action["reason"],
            })
            next_state["notice"] = (
                f'Friction attached to {episode["id"]}; its overall disposition remains '
                f'{episode["disposition"]}.'
            )

    elif kind == "revise":
        episode = _latest(next_state, "episode")
        if not episode:
            next_state["notice"] = "No lesson episode exists yet."
        else:
            episode["disposition"] = "revised"
            episode["revision"] = action["revision"]
            next_state["notice"] = f'{episode["id"]} now supplies an original/revised training pair.'

    elif kind == "compare":
        record = {
            "id": _next_id(next_state, "C"),
            "kind": "comparison",
            "topic": action["topic"],
            "A": action["A"],
            "B": action["B"],
            "choice": "pending",
            "reason": "",
        }
        next_state["records"].append(record)
        next_state["notice"] = f'{record["id"]} awaits A, B, or neither.'

    elif kind == "prefer":
        comparison = _latest(next_state, "comparison")
        if not comparison or comparison["choice"] != "pending":
            next_state["notice"] = "No unresolved comparison exists."
        else:
            comparison["choice"] = action["choice"]
            comparison["reason"] = action.get("reason", "")
            next_state["notice"] = f'{comparison["id"]} resolved as {action["choice"]}.'

    elif kind == "forget":
        if not next_state["records"]:
            next_state["notice"] = "Nothing exists to forget."
        else:
            forgotten = next_state["records"].pop()
            next_state["notice"] = f'{forgotten["id"]} and its attached feedback were forgotten.'

    return next_state


def export_preview(state):
    demonstrations = 0
    preferences = 0
    rejected = 0
    friction_spans = 0

    for record in state["records"]:
        if record["kind"] == "episode":
            if record["disposition"] in {"keep", "revised"}:
                demonstrations += 1
            if record["disposition"] == "revised":
                preferences += 1
            if record["disposition"] == "reject":
                rejected += 1
            friction_spans += len(record["friction"])
        elif record["choice"] in {"A", "B"}:
            demonstrations += 1
            preferences += 1

    return {
        "supervised_demonstrations": demonstrations,
        "pairwise_preferences": preferences,
        "unpaired_rejections": rejected,
        "annotated_friction_spans": friction_spans,
        "note": "Neither choices remain evaluation evidence but are not DPO pairs.",
    }

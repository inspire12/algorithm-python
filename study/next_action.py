#!/usr/bin/env python3
"""Select exactly one next learning action from problem-registry.json."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path


REGISTRY = Path(__file__).with_name("problem-registry.json")


def load_registry() -> dict:
    with REGISTRY.open(encoding="utf-8") as file:
        return json.load(file)


def select_next_action(registry: dict, today: str) -> dict | None:
    due = []

    for problem in registry["problems"]:
        action = problem["next_action"]
        action_due = action["due"]

        if action["eligible"] and action_due is not None and action_due <= today:
            due.append(problem)

    if due:
        return min(
            due,
            key=lambda problem: (
                problem["next_action"]["priority"],
                problem["next_action"]["due"],
                problem["id"],
            ),
        )

    active = [
        problem
        for problem in registry["problems"]
        if problem.get("active") and problem["next_action"]["eligible"]
    ]
    return active[0] if len(active) == 1 else None


def with_atlas_context(registry: dict, selected: dict | None) -> dict | None:
    """Attach learner-authored context without changing selection or verified status."""
    if selected is None:
        return None
    atlas = registry.get("atlas", {})
    nodes = {node["id"]: node for node in atlas.get("nodes", [])}
    related = {node["id"] for node in nodes.values() if selected["id"] in node.get("problems", [])}
    for identifier in list(related):
        visited = set()
        while identifier in nodes and identifier not in visited:
            visited.add(identifier)
            related.add(identifier)
            identifier = nodes[identifier].get("parent")
    context = []
    for item in list(nodes.values()) + atlas.get("ideas", []):
        if item["id"] not in related and not set(item.get("targets", [])) & (related | {selected["id"]}):
            continue
        reflection = atlas.get("reflections", {}).get(item["id"], {})
        note = atlas.get("notes", {}).get(item["id"], "")
        if reflection or note:
            context.append({"id": item["id"], "title": item["title"], "self_assessment": reflection, "note": note})
    result = dict(selected)
    if context:
        result["atlas_context"] = context
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=date.today().isoformat())
    args = parser.parse_args()

    registry = load_registry()
    selected = with_atlas_context(registry, select_next_action(registry, args.date))
    print(json.dumps(selected, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

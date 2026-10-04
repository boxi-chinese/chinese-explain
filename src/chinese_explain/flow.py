from __future__ import annotations

from pathlib import Path
from .schema import load

def run(path: Path, response: str, revised: str, transfer: str) -> dict:
    lesson = load(path)
    dimensions = {name: {"status": "inspect", "rationale": f"Review the learner response for {name}."} for name in lesson["feedback_dimensions"]}
    return {"lesson_id": lesson["lesson_id"], "context": lesson["context"], "response": response, "feedback": dimensions, "revision": revised, "transfer": transfer}

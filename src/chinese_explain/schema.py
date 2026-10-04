from __future__ import annotations

import json
from pathlib import Path

REQUIRED = {"schema_version", "lesson_id", "title", "learner_level", "context", "segments", "task", "feedback_dimensions", "revision_prompt", "transfer_prompt"}
FORBIDDEN = {"proficiency_score", "overall_score", "cefr_level"}

def load(path: Path) -> dict:
    data = json.loads(path.read_text())
    missing = REQUIRED - data.keys()
    if missing:
        raise ValueError(f"missing lesson fields: {sorted(missing)}")
    if data["schema_version"] != "lesson-bundle/v0.1":
        raise ValueError("unsupported schema version")
    if FORBIDDEN & data.keys():
        raise ValueError("lesson bundles cannot claim proficiency or an overall score")
    if not data["segments"] or not data["feedback_dimensions"]:
        raise ValueError("segments and feedback_dimensions must be non-empty")
    ids = [segment.get("id") for segment in data["segments"]]
    if any(not item for item in ids) or len(ids) != len(set(ids)):
        raise ValueError("segment IDs must be non-empty and unique")
    for segment in data["segments"]:
        if not segment.get("text"):
            raise ValueError("every segment needs text")
    return data

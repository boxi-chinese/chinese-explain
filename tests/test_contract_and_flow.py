import json
import unittest
from pathlib import Path
from chinese_explain.flow import run
from chinese_explain.schema import load

ROOT=Path(__file__).parents[1]

class ContractTests(unittest.TestCase):
    def test_valid_lessons_and_stable_flow(self):
        for name in ("tones-context.json", "word-order.json"):
            path=ROOT/"fixtures"/name
            lesson=load(path)
            result=run(path,"我的回答","我的修订","我的迁移")
            self.assertEqual(result["lesson_id"],lesson["lesson_id"])
            self.assertEqual(list(result["feedback"]),lesson["feedback_dimensions"])
            self.assertEqual(run(path,"我的回答","我的修订","我的迁移"),result)
    def test_proficiency_claim_is_rejected(self):
        path=ROOT/"fixtures"/"bad.json"
        data=json.loads((ROOT/"fixtures"/"tones-context.json").read_text()); data["proficiency_score"]=99; path.write_text(json.dumps(data))
        try:
            with self.assertRaises(ValueError):
                load(path)
        finally:
            path.unlink()

if __name__ == "__main__": unittest.main()

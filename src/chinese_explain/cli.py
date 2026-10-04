from __future__ import annotations

import argparse
import json
from pathlib import Path
from .flow import run
from .schema import load

def main() -> int:
    parser=argparse.ArgumentParser()
    sub=parser.add_subparsers(dest="command",required=True)
    check=sub.add_parser("validate"); check.add_argument("lesson",type=Path)
    execute=sub.add_parser("run"); execute.add_argument("lesson",type=Path); execute.add_argument("--response",required=True); execute.add_argument("--revised-response",required=True); execute.add_argument("--transfer-response",required=True)
    args=parser.parse_args()
    if args.command == "validate":
        data=load(args.lesson); print(json.dumps({"lesson_id":data["lesson_id"],"status":"valid"},ensure_ascii=False)); return 0
    print(json.dumps(run(args.lesson,args.response,args.revised_response,args.transfer_response),ensure_ascii=False,indent=2)); return 0

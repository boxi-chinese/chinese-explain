# chinese-explain

This MVP provides a text-first Chinese lesson contract and an inspectable offline flow:

```text
语境 -> 输入 -> 产出 -> 分维度反馈 -> 修订 -> 迁移
```

Validate a lesson:

```text
PYTHONPATH=src python -m chinese_explain validate fixtures/tones-context.json
```

Run a lesson flow:

```text
PYTHONPATH=src python -m chinese_explain run fixtures/tones-context.json \
  --response "买米" \
  --revised-response "我想买米。" \
  --transfer-response "我去市场买水果。"
```

Run tests without network dependencies:

```text
PYTHONPATH=src python -m unittest discover -s tests -p 'test_*.py'
```

The MVP deliberately avoids accounts, speech recognition, learner data, opaque scoring, and proficiency claims.

# chinese-explain

面向中文学习的可执行解释：把语境、汉字、拼音、声调、产出、反馈和修订放进同一个可检查的学习单元。

> **Status:** scaffold. The public lesson contract and first MVP are being designed.

## Scope

`chinese-explain` will provide a versioned lesson bundle, text-first playback, optional audio/character layers, inspectable feedback, and static export. It must support Chinese-specific learning objects without reducing learning to a single score.

Initial MVP scenes:

1. tones and pronunciation in context;
2. word order, aspect, and meaning;
3. dialogue repair and pragmatic fit.

## Learning loop

```text
语境 → 预测 → 输入 → 产出 → 对比反馈 → 修订 → 迁移
```

## Repository boundaries

This repository owns reusable lesson schemas, alignment and feedback primitives. Public learning content lives in `boxi-chinese/chinese-scenarios`; the site is a separate presentation layer. Personal learner data, private class records, and proficiency claims do not belong here.

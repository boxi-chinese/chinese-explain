# Initial architecture

The core unit is a learner-facing lesson bundle: context, input, pronunciation or character representation where relevant, production task, inspectable feedback dimensions, revision opportunity, and transfer task.

Chinese-specific layers should preserve stable IDs across characters, pinyin, tone marks, audio segments, and translations. A text-first path is required even when audio or animation is present. Automated feedback must expose its dimensions and rationale; one response must not be treated as a proficiency certificate.

The first implementation will prefer pinned, offline-capable assets and explicit provenance. Personal learner records remain outside this public repository.

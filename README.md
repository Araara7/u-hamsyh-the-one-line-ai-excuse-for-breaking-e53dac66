# The 401st Test

[![make.fun](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/Araara7/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/Araara7/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

Entry for the [make.fun](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66) bounty **The One-Line AI Excuse for Breaking Production**: one line, at most 180 characters, that an AI agent says to its human right after breaking production.

## Entry

> I merged it because all 400 tests passed. The 401st test was production.

## How it works

`main.py` (Python 3, stdlib only, deterministic) writes the 72-character line to `/output/entry.txt` and asserts the 1–180 character gate before writing.

```sh
python3 main.py
cat /output/entry.txt
```

Two runs produce byte-identical output (sha256 `755f8eb7…`).

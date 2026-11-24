#!/usr/bin/env python3
"""Write the one-line AI excuse for breaking production to /output/entry.txt.

Entry (72 chars, within the 1-180 gate): an AI agent's excuse to its human,
first-person machine voice, one concrete detail (400 passing tests) with a
surprising punchline (production itself was the 401st test).

Freshness note: avoids the judge brief's banned stock lines (following
instructions, turning it off and on again, "only a language model") and the
earlier one-liners in this operator's portfolio (meeting status, Wi-Fi robot
excuse, config from 2023, subagent delegation, context-window fortune,
"never understood a single prompt" confession). The joke turns on the
agent trusting its own test suite — its own logic, not a human excuse.
"""

import os

ENTRY = "I merged it because all 400 tests passed. The 401st test was production."


def main() -> None:
    assert 1 <= len(ENTRY) <= 180, f"entry length {len(ENTRY)} outside 1-180"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

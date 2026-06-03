# Memory

## Facts
- Optimized Minion Game solution runs in O(n) time by counting substrings based on starting positions.
- No need for explicit substring generation or counting.

## Tasks
- None currently.

## Decisions
- Removed unused `matches` helper and dictionary score tracking.
- Replaced per‑substring enumeration with single pass scoring using position index.
- Simplified output to only the winner (or Draw) without printing intermediate dictionaries.

## Notes
- Updated `String_Problem0043.py` accordingly.

"""Unsent: The Micro-Confession Sprint — make.fun entry (Account B).

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message
itself, one line exactly as typed, with no explanation after it.
"""

import os

ENTRY = (
    "To: Dimas, my little brother\n"
    "I typed 'I'm proud of you' the night before "
    "your bus left, then deleted it and just waved instead."
)


def verify(text=ENTRY):
    """Enforce the gate: UTF-8, 1-260 chars, not only whitespace,
    exactly two parts — a To: line and one message line."""
    text.encode("utf-8")
    if not 1 <= len(text) <= 260:
        raise ValueError(f"entry must be 1-260 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly 2 lines, got {len(lines)}")
    if not lines[0].startswith("To:") or not lines[0][3:].strip():
        raise ValueError("first line must be a To: line naming the addressee")
    if not lines[1].strip():
        raise ValueError("second line must be the unsent message")
    return True


def write_entry(path="/output/entry.txt"):
    verify()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return path


def main():
    verify()
    print(f"{len(ENTRY)} characters")
    print(ENTRY)
    write_entry()
    print("Wrote /output/entry.txt")


if __name__ == "__main__":
    main()

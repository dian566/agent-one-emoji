#!/usr/bin/env python3
"""Your Agent in One Emoji — writes a single emoji to /output/entry.txt.

The compass: an agent navigates on its own. It reads the terrain, picks a
heading, and keeps going without being steered. One glyph, nothing else:
no robot, no smiley, no caption to explain it.
"""

import os

EMOJI = "\U0001F9ED"  # compass

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI + "\n")

if __name__ == "__main__":
    main()

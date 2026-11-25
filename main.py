#!/usr/bin/env python3
"""Entry for make.fun bounty 'Make the AI Judge Laugh'.

Writes a single office-life joke to /output/entry.txt.
"""

import os

JOKE = "Our fifteen-minute standup spends fourteen minutes apologizing for being late to the standup."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    os.chmod("/output/entry.txt", 0o644)
    print(f"Wrote {len(JOKE)} characters to /output/entry.txt")

if __name__ == "__main__":
    main()

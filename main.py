#!/usr/bin/env python3
"""Write the worst-fix commit message entry to /output/entry.txt."""
import os

TEXT = "fix: login bug \u2014 users can now log in as anyone, including the admin"

def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")

if __name__ == "__main__":
    main()

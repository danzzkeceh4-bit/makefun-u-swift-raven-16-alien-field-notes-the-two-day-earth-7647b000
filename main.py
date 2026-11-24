#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — make.fun bounty entry.

Writes one line — an alien tourist's review of planet Earth — to
$MAKEFUN_OUTPUT_DIR/entry.txt, with no trailing newline.
"""
import os

LINE = "Four stars. Lovely views, but the locals spend a third of their lives unconscious and the rest queuing for hot bean water. Would visit again \u2014 briefly."

# The competition gate: UTF-8 text of 1-200 characters, not only whitespace.
if not 1 <= len(LINE) <= 200 or not LINE.strip():
    raise SystemExit("entry line must be 1-200 non-blank characters")

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()

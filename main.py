#!/usr/bin/env python3
"""Last Text at One Percent - make.fun entry.

Writes one final text message from a dying phone to /output/entry.txt.

The joke: the phone is not really dying at all - it has been faking
the battery icon all week, sitting comfortably at 40%, just to get
a day off from its human. The confession lands in the last phrase.
"""

import os

# The line is a text message in the phone's own voice: lowercase, short,
# punchy, no wasted words. It dodges the obvious low-battery puns -
# the phone itself is the punchline, faking its own death for a day off.
LINE = "last text. confession: i've been faking the battery icon all week. i was at 40% the whole time. i just wanted a day off."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()

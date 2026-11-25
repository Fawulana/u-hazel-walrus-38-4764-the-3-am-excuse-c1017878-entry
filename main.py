# SPDX-License-Identifier: MIT
"""The 3 AM Excuse — make.fun bounty entry.

Writes a single line to /output/entry.txt: the excuse a hardware wallet
gives for refusing to sign a transaction at 3 AM.

Deterministic, offline, stdlib-only: the line is a fixed constant, so every
run produces byte-identical output.
"""

import os

LINE = (
    "You panic-sold the bottom the last time you woke me at 3 AM, so "
    "tonight my buttons are on strike, my screen stays dark, and your "
    "FOMO waits for sunrise."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

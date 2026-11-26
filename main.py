"""One Line of Earned Pride — a make.fun one-line entry.

Running this program writes the entry line to entry.txt inside
MAKEFUN_OUTPUT_DIR (or /tmp/out when that variable is not set).
"""

import os

ENTRY = "After three years of dawn practices, the smallest kid on the team finally sank the free throw, and his dad, who never cheers, stood up and clapped with both hands over his mouth."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()

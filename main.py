"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to /output/entry.txt
(or $OUTPUT_DIR/entry.txt when set, for local testing).
Deterministic, no network, no randomness, no external files.
"""

import os

STORY = "The letter arrived after the funeral."

def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY + "\n")

if __name__ == "__main__":
    main()

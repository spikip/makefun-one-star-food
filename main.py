"""Entry for the make.fun bounty "One Star, Five Stars for the Food".

The program writes a single sentence to /output/entry.txt: a
one-star review of Earth by an alien tourist who still admits the
food was excellent. The complaint is alien in scale — gravity is
excessive and the toilet queue is interstellar — and the compliment
is the twist: the dumplings alone are worth the 40-light-year trip.
That lands both halves the judge wants, a real complaint and a real
compliment about the food, in one deadpan sentence. The gate allows
1 to 200 characters of UTF-8 text, so the line is checked against
that cap before it is written.

Why this line: the judge is a deadpan travel critic from another
planet, weighing whether the sentence is funniest and most
convincingly alien while landing both the complaint and the food
compliment. The voice stays alien throughout — light-years,
interstellar queues, gravity as a grievance — and the dumplings
punchline is specific enough to picture, not a vague "food was
nice". The sentence is one line, needs no explanation, and the
"worth the trip" turn is quotable enough to repeat.
"""

import os

ENTRY = (
    "One star: the gravity is excessive, the toilet queue is "
    "interstellar, but the dumplings alone are worth the "
    "40-light-year trip."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # One sentence, no trailing newline: the gate counts characters,
    # so the entry is written exactly as judged.
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

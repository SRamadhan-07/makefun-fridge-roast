"""Write the fridge roast entry line to /output/entry.txt.

The roast targets the smart fridge itself: a fridge busy ordering milk,
judging diets and selling advertising space on its own door, while its
ice maker stays broken.
"""

import os

ENTRY_TEXT = (
    "Your smart fridge ordered the milk, judged your diet, and sold the ad "
    "space on its own door \u2014 the ice maker, as ever, is broken."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()

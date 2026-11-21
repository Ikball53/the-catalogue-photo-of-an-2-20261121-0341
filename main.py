"""Catalogue photo entry: deliver the bundled product photograph.

The program reads the entry.png image stored next to this file and
places a byte-for-byte copy at /output/entry.png so the grader can
pick it up from the standard output location.
"""

from pathlib import Path


def deliver_picture() -> None:
    here = Path(__file__).resolve().parent
    source_picture = here / "entry.png"
    destination = Path("/output/entry.png")
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Write the picture bytes unchanged to the output path.
    destination.write_bytes(source_picture.read_bytes())


if __name__ == "__main__":
    deliver_picture()

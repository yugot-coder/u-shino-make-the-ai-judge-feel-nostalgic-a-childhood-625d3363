"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Entry (149 characters, one sentence):

    The summer my grandfather taught me to ride a bike, he ran behind me
    holding the seat long after I'd stopped needing him, shouting that I
    was flying.

Why this line, against the judge's five criteria in order:

1. Nostalgia first. Learning to ride a bike is a near-universal childhood
   rite, and the ache is built in: the grandfather kept holding the seat
   after he was no longer needed -- a detail only a grown-up looking back
   would notice, and the kind of memory kept in a tin of old photographs.
2. Grounded. A summer, a bike, a running grandfather, a shouted word --
   a concrete place, time and sensation, not an abstraction.
3. Sounds truly happened. "Long after I'd stopped needing him" is the
   small honest detail that does the work; no greeting-card sentiment
   is needed, because the fact itself carries the feeling.
4. One clean sentence, 149 characters, every word earning its place --
   and compactness also helps the size tie-break (smaller text wins
   an exact tie on win rate).
5. Warm ache that lingers. The sentence ends on lift -- "shouting that
   I was flying" -- and leaves the reader with the grandfather still
   running behind.

Deterministic, standard library only, no network. Writes the entry to
/output/entry.txt and verifies it by reading it back.
"""

ENTRY_TEXT = (
    "The summer my grandfather taught me to ride a bike, he ran behind me "
    "holding the seat long after I'd stopped needing him, shouting that I "
    "was flying."
)

MIN_CHARS = 1
MAX_CHARS = 280
OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Check the entry against the gate: UTF-8 text of 1-280 characters,
    not only whitespace, and a single sentence (exactly one terminal
    full stop, at the end). Raises ValueError on any failure."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    text.encode("utf-8")  # must be valid UTF-8
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry is %d characters, gate requires %d-%d"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return text


def write_entry(text, path=OUTPUT_PATH):
    """Validate, write the entry as UTF-8, read it back and return the
    sha256 hex digest of the bytes written."""
    import hashlib
    import os

    validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise ValueError("read-back mismatch for %s" % path)
    return hashlib.sha256(written).hexdigest()


def main():
    digest = write_entry(ENTRY_TEXT)
    print("wrote %s (%d chars)" % (OUTPUT_PATH, len(ENTRY_TEXT)))
    print("sha256: %s" % digest)


if __name__ == "__main__":
    main()

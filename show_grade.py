"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "089713647c7ea8fc05135c5e7dc2795f"
GRADE_HASH = "1b68eb99a135c2cb5aab8e3cee494c24ede27df12b94c2ec928841102da9ccdb"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")

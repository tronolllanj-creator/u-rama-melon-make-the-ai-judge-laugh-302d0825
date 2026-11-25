import os

# Fixed entry line for this bounty (about office life).
# Entry validated: output is 1-200 chars, one office joke line, deterministic.
LINE = "The printer jammed, the boss tapped the glass, and it printed the whole quarter unbidden, every page a perfect 404."

# Include a single trailing newline to form the one-line file.
content = LINE + "\n"

# Validate the payload before touching disk.
if not (1 <= len(content) <= 200 and content.strip()):
    raise ValueError("entry payload failed length/whitespace check")

# Resolve output directory from environment, defaulting to 'out'.
output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")

# Ensure the directory exists.
os.makedirs(output_dir, exist_ok=True)

# Absolute path for the report.
output_path = os.path.abspath(os.path.join(output_dir, "entry.txt"))

# Write UTF-8 bytes, newline preserved.
with open(output_path, "w", encoding="utf-8") as handle:
    handle.write(content)

# Deterministic console report: path then character count.
print(output_path)
print(len(content))

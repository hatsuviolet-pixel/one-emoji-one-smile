from pathlib import Path
import os

# Write a single optimal emoji for warmth judging
output_dir = Path("/output")
output_dir.mkdir(parents=True, exist_ok=True)

# Entry: 🤗 (hugging face) - selected for maximum warmth/universality
# Criteria matched: single emoji, warm to strangers, culturally universal,
# feels chosen not default, appropriate for陌生 interaction
entry = "🤗"

(output_dir / "entry.txt").write_text(entry, encoding="utf-8")
print(f"Wrote entry: {entry}")

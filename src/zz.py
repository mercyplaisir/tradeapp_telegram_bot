from pathlib import Path

THISFOLDER = Path(__file__).resolve().parent
TOKENFOLDER = f"{THISFOLDER}/token.txt"

with open(TOKENFOLDER, "r") as f:
    token = f.read()

print(token.strip())
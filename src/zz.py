from pathlib import Path


TOKENFOLDER = f"./token.txt"

with open(TOKENFOLDER, "r") as f:
    token = f.read()

print(token)
from pathlib import Path


name = Path('new_dir')
if not name.exists():
    name.mkdir()


p = Path("temp/")
p.mkdir(parents=True, exist_ok=True)
filename = "cccccc.txt"
filepath = p / filename
with filepath.open("w", encoding ="utf-8") as f:
    f.write('kek')
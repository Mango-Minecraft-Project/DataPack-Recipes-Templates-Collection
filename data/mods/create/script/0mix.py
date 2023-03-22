import json
import pathlib
bp = "./data/mods/create/recipes/"
with open("./data/mods/create/script/base.json") as f:
  bd = json.load(f)
print(bd)
for i in pathlib.Path(bp).glob("*.json"):
  if (i_n:=i.name) not in {"sequenced_assembly.json", "mechanical_crafting.json"}:
    with open(bp + i_n) as f:
      d = json.load(f)
    print(d, bd | d)
    with open(bp + i_n, "w") as f:
      json.dump({"type": f"create:{i.stem}"} | bd | d, f, indent=2)
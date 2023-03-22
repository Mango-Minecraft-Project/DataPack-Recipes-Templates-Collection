import json
import pathlib
bp = "./data/mods/minecraft/recipes/"
with open("./data/mods/minecraft/script/base.json") as f:
  bd = json.load(f)
print(bd)
for i in pathlib.Path(bp).glob("*.json"):
  with open(bp + i.name) as f:
    d = json.load(f)
  print(d, bd | d)
  if i.stem not in {"smithing_transform", "smithing_trim", "smithing", "crafting_decorated_pot"}:
    d = bd | d
  with open(bp + i.name, "w") as f:
    json.dump({"type": f"minecraft:{i.stem}"} | d, f, indent=2)
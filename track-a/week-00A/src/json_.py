import json, tempfile
from pathlib import Path

p = Path(tempfile.gettempdir()) / "week0a.json"
obj = {"id":1, "tags": ["python", "data"], "active": True}
p.write_text(json.dumps(obj, ensure_ascii=False, indent=2))
print(json.loads(p.read_text()) == obj)
import logging
import os
import json, tempfile
from pathlib import Path
def safe_write_json(path: Path, obj: dict) -> None:
    tmp_path = path.with_suffix(".tmp")
    path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(obj=obj, ensure_ascii=False)
    byte_data = data.encode("utf-8")
    logging.info(f"Wrote {obj} to {tmp_path}")
    with open(tmp_path, "wb") as f:
        f.write(byte_data)
        f.flush()
        # os.fsync(f.fileno())

    os.replace(tmp_path, path)
    logging.info(f"Wrote {len(byte_data)} bytes atomically to {path}")
        
safe_write_json(Path(os.path.join(os.getcwd(), "test.json")), {"Check": "This"})
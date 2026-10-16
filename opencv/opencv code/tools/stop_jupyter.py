from pathlib import Path
import json, urllib.request
root = Path(__file__).resolve().parents[1]
count = 0
for path in (root / ".jupyter-runtime").glob("jpserver-*.json"):
    try:
        info = json.loads(path.read_text(encoding="utf-8"))
        request = urllib.request.Request(info["url"].rstrip("/") + "/api/shutdown", data=b"", headers={"Authorization": "token " + info.get("token", "")}, method="POST")
        with urllib.request.urlopen(request, timeout=5) as response:
            count += 1
    except Exception:
        pass
print("Stopped course Jupyter servers:", count)

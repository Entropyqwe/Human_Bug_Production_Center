from pathlib import Path
import json, os, subprocess, sys, time, urllib.request, webbrowser
ROOT = Path(__file__).resolve().parents[1]
PYTHON = r"D:\anaconda\envs\opencv-course\python.exe"
PREFIX = Path(PYTHON).parent
os.environ["PATH"] = str(PREFIX) + os.pathsep + str(PREFIX / "Scripts") + os.pathsep + str(PREFIX / "Library/bin") + os.pathsep + os.environ.get("PATH", "")
RUNTIME = ROOT / ".jupyter-runtime"
RUNTIME.mkdir(exist_ok=True)
os.environ["JUPYTER_RUNTIME_DIR"] = str(RUNTIME)
os.environ["PYTHONIOENCODING"] = "utf-8"

def open_existing():
    for path in RUNTIME.glob("jpserver-*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            from urllib.parse import quote
            url = data["url"].rstrip("/")
            headers = {"Authorization": "token " + data.get("token", "")}
            request = urllib.request.Request(url + "/api", headers=headers)
            with urllib.request.urlopen(request, timeout=2) as response:
                if response.status != 200:
                    continue
            webbrowser.open(url + "/notebooks/notebooks/01_environment_check.ipynb?token=" + quote(data.get("token", "")))
            return True
        except Exception:
            pass
    return False

if not open_existing():
    log = (RUNTIME / "server.log").open("a", encoding="utf-8")
    subprocess.Popen([PYTHON,"-m","notebook", "--ServerApp.ip=127.0.0.1", "--ServerApp.port=8890", "--ServerApp.port_retries=20", "--ServerApp.open_browser=False", "--ServerApp.root_dir=" + str(ROOT)], cwd=ROOT, env=os.environ.copy(), stdout=log, stderr=log, creationflags=getattr(subprocess,"CREATE_NO_WINDOW",0))
    for _ in range(60):
        time.sleep(1)
        if open_existing():
            break
    else:
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, str(RUNTIME / "server.log"), "Jupyter startup failed - check log", 0)

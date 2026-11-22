import time, json, sys
from ultralytics import YOLO

CFGS = [
    ("imgsz640_batch16", 640, 16),
    ("imgsz640_batch32", 640, 32),
    ("imgsz416_batch16", 416, 16),
]

if __name__ == "__main__":
    out = []
    for name, imgsz, batch in CFGS:
        m = YOLO("yolo26n.pt")
        t0 = time.time()
        try:
            m.train(data="data/datasets/bench2700.yaml", epochs=1, batch=batch, imgsz=imgsz,
                    workers=4, cache=False, plots=False, verbose=False,
                    project="bench", name=name, exist_ok=True, val=False)
            dt = time.time() - t0
            per = dt  # 含 ~15s 启动开销
            out.append((name, round(dt, 1), round((dt - 15), 1)))
            print(f">>> {name}: 1 epoch 墙钟 {dt:.1f}s (扣除启动约 {dt-15:.1f}s)", flush=True)
        except Exception as e:
            print(f">>> {name}: 失败 {type(e).__name__} {str(e)[:120]}", flush=True)
            out.append((name, None, str(e)[:80]))
    print(json.dumps(out, ensure_ascii=False))

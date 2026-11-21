import time
from ultralytics import YOLO

if __name__ == "__main__":
    t_load = time.time()
    m = YOLO("yolo26n.pt")
    print(f"[load] {time.time() - t_load:.1f}s", flush=True)
    t0 = time.time()
    r = m.train(data="data/datasets/bench2700.yaml", epochs=2, batch=8, imgsz=640,
                workers=4, cache=False, plots=False, verbose=False,
                project="bench", name="b2700", exist_ok=True, val=True, patience=2)
    dt = time.time() - t0
    print(f"[wall] 2 epoch(训练+验证) 总计 {dt:.1f}s -> 平均每轮 {dt/2:.1f}s", flush=True)
    print(f"[rate] 训练+验证综合吞吐 ~= {2700/(dt/2):.1f} 张/s", flush=True)

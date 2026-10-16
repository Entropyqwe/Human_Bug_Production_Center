from pathlib import Path
import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt

def read_image(path):
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"请选择完整图片文件路径，而不是文件夹: {path}")
    img = cv2.imdecode(np.fromfile(str(path), dtype=np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError(f"图片无法解码: {path}")
    return img

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image", nargs="?", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    image_path = args.image or root / "data" / "sample.png"
    img = read_image(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 80, 160)
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    for ax, image, title in zip(axes, [cv2.cvtColor(img, cv2.COLOR_BGR2RGB), gray, edges], ["Original RGB", "Grayscale", "Canny edges"]):
        ax.imshow(image, cmap="gray" if image.ndim == 2 else None)
        ax.set_title(title)
        ax.axis("off")
    fig.tight_layout()
    result = root / "results" / "image_demo.png"
    result.parent.mkdir(exist_ok=True)
    fig.savefig(result, dpi=140)
    print(f"SUCCESS | OpenCV {cv2.__version__} | image {img.shape} | {result}")
    if args.check:
        plt.close(fig)
    else:
        plt.show()

if __name__ == "__main__":
    main()

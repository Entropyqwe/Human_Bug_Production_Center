from pathlib import Path
import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 普通 .py 文件用 plt.show()；%matplotlib inline 只能写在 Notebook 中。
image_path = Path(r"C:\Users\23832\Pictures\NevernessToEverness\26_07_03_00_00_47.png")
if not image_path.is_file():
    raise FileNotFoundError(f"图片不存在：{image_path}")

# 兼容中文路径，读取后得到 BGR 顺序的数组。
img = cv2.imdecode(np.fromfile(str(image_path), dtype=np.uint8), cv2.IMREAD_COLOR)
if img is None:
    raise ValueError(f"图片无法解码：{image_path}")

print("Python:", sys.executable)
print("图片形状:", img.shape)
print(img)
plt.figure(figsize=(10, 6))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.tight_layout()
if "--check" in sys.argv:
    plt.close()
    print("CHECK PASSED")
else:
    plt.show()

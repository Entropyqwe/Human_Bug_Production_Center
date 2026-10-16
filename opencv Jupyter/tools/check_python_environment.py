import sys
from pathlib import Path
import cv2
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
print("Python:", sys.executable)
print("OpenCV:", cv2.__version__)
print("NumPy:", np.__version__)
print("Matplotlib:", matplotlib.__version__)
image = np.zeros((300, 500, 3), dtype=np.uint8)
cv2.circle(image, (250, 140), 90, (0, 255, 255), -1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
assert gray.shape == (300, 500)
assert cv2.imencode('.png', image)[0]
results = root / 'results'
results.mkdir(exist_ok=True)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('OpenCV environment OK')
plt.savefig(results / 'python-environment-check.png')
plt.close()
cv2.imshow('Python OpenCV - environment OK', image)
cv2.waitKey(1500)
cv2.destroyAllWindows()
print("PASS: imports, image processing, PNG encoding, Matplotlib and OpenCV window")
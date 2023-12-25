from urllib.request import urlretrieve
from matplotlib import pyplot as plt
from PIL import Image
import seaborn as sns

urlretrieve('https://i.imgur.com/SkPbq.jpg','chart.jpg')
img = Image.open('chart.jpg')

plt.figure(figsize=(12,6))
plt.grid(False); plt.axis('off'); plt.imshow(img)
plt.show()
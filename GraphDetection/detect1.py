from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
from os.path import join

# only  use jpegs please

image = Image.open(join('images','graph2.jpg'))
plt.imshow(image)
plt.pause(3)
image = image.filter(ImageFilter.FIND_EDGES)
print("ahhh")
plt.imshow(image)
plt.pause(3)
image.save(join('images','graph_edges.jpg'))

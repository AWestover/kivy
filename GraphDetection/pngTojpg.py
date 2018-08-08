from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
from os.path import join

inp = input("File name?\t")

image = Image.open(inp)
image.save(inp.replace('png', 'jpg'))
plt.imshow(image)
plt.pause(3)
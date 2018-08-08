from scipy.ndimage.measurements import center_of_mass as c_mass
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
from pprint import pprint
from os.path import join
import numpy as np
import pdb


"""
This will take in an image,
compute edges (with PIL)
then go to its center of mass (scipy)
travel left to the edge of the picture 
traversing and deleting loops as it goes (arbitrary)
and the best loop is our graph (probably longest)
"""


"""

SLIGHT PROBLEM:
the edge detection might not really be binary!!!!!!!!!! (check on real images)

"""

ims = 128  # image size

# only  use jpegs please
image = Image.open(join('images','graph.jpg'))
image = image.resize((ims,ims),Image.ANTIALIAS)
plt.imshow(image)
plt.pause(2)

image = image.filter(ImageFilter.FIND_EDGES)
image = np.sum((np.array(image)!=[0,0,0]).astype(int),axis=2)/3

# now go left till you hit stuff and then keep going left
loops = []

def edge_in_bubble(pos, image, radius=3):
	try:
		for i in range(-3, 3):
			for j in range(-3, 3):
				c_idx = np.array([i, j])+pos
				# print(pos)
				if image[c_idx[0]][c_idx[1]] == 1:
					return c_idx
		return False
	except:
		print("ERROR")
		return False


def deal_with_edge(start, image, radius=3):
	loop = []
	while type(start) != bool:
		loop.append(start)
		image[start[0]][start[1]] = 0
		start = edge_in_bubble(start, image, radius=radius)
	return loop

radius = 16

cm=c_mass(image)
pos = np.array([int(cm[0]), int(cm[1])])
while pos[0] > radius*2:
	pos -= np.array([1,0])
	start = edge_in_bubble(pos, image, radius=radius)
	if type(start) != bool:
		# note we pass image in BY REFERENCE
		# so the function can (and will) change the image
		# it blacks over edges that have been traversed
		loops.append(deal_with_edge(start, image, radius=radius))

cm=c_mass(image)
pos = np.array([int(cm[0]), int(cm[1])])
while pos[0] < ims - radius*2:
	pos += np.array([1,0])
	start = edge_in_bubble(pos, image, radius=radius)
	if type(start) != bool:
		loops.append(deal_with_edge(start, image, radius=radius))


pprint(np.array(image))
plt.imshow(image)
plt.scatter(cm[0],cm[1])
plt.pause(3)

# pdb.set_trace()

loop_display = np.zeros((ims, ims))
for l in range(0, len(loops)):
	for pos in loops[l]:
		loop_display[pos[0]][pos[1]] = len(loops) - l + 1

plt.imshow(loop_display)
plt.pause(5)



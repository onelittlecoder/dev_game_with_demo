import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
img=cv2.imread("/Users/super/work/projects/python_src/day2/pic.png")
org_img=np.asarray(img)
new_img=org_img.copy()
roi_len=9
x,y=random.randint(200,895),random.randint(200,530)
new_img[y-roi_len:y+roi_len,x-roi_len:x+roi_len,:]=200

fig, axes = plt.subplots(nrows = 1, ncols = 2)
axes[0].imshow(org_img)
axes[1].imshow(new_img)
plt.show()


from PIL import Image
import numpy as np

im = np.array(Image.open("F:\测试发票图片\map\\braids-3959201_1920.jpg"))

print(im.shape,im.dtype)

b = [255,255,255] - im
img = Image.fromarray(b.astype('uint8'))
img.save("F:\测试发票图片\map\\braids.jpg")
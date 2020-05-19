from PIL import Image
import numpy as np
import os,uuid,time
from functools import wraps
import traceback

# def get_time(func):
#     @wraps(func)
#     def foo(*args,**kwargs):
#         start_time = time.time()
#         data = func(*args,**kwargs)
#         end_time = time.time()
#         print(end_time - start_time)
#         return data
#     return foo
#
#
# @get_time
# def img_cl(path):
#     try:
#         if path.split('.')[-1] in ['jpg','jpeg','png']:
#             img_msg = np.array(Image.open(path).convert('L'))
#             print(img_msg.shape)
#             new_msg = 255 - img_msg
#             im = Image.fromarray(new_msg.astype('uint8'))
#             new_path = os.path.dirname(path) + str(uuid.uuid4()) + '.jpg'
#             im.save(new_path)
#     except:
#         traceback.print_exc()


def if_img(func):
    @wraps(func)
    def img_after(*args,**kwargs):
        img_path = args[0]
        if img_path and os.path.isfile(img_path) and img_path.split('.')[-1] in ['jpg','jpeg','png']:
            data = func(*args,**kwargs)
            return data
        else:
            return ''
    return img_after

@if_img
def img_size(path):
    try:
        img_data = Image.open(path)
        new_img = img_data.resize((int(img_data.width/2),int(img_data.height/2)))
        new_img.save("new.jpg")
    except:
        traceback.print_exc()

if __name__ == '__main__':
    img_path = "F:\测试发票图片\map\\braids-3959201_1920.jpg"
    # img_cl(img_path)
    img_size(img_path)
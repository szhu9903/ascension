from PIL import Image
import numpy as np
import os,uuid,time
from functools import wraps

def get_time(func):
    @wraps(func)
    def foo(*args,**kwargs):
        start_time = time.time()
        data = func(*args,**kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return data
    return foo


@get_time
def img_cl(path):
    if path.split('.')[-1] in ['jpg','jpeg','png']:
        img_msg = np.array(Image.open(path))
        print(img_msg.shape)
        new_msg = [255,255,255] - img_msg
        im = Image.fromarray(new_msg.astype('uint'))
        new_path = img_path.split('\\')[:-1] + str(uuid.uuid4()) + img_path.split('.')[-1]
        im.save(new_path)

if __name__ == '__main__':
    img_path = '‪F:\测试发票图片\map\\underwater-4731696_1920.jpg'
    img_cl(img_path)
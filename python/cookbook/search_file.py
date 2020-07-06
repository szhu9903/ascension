

# python 通配符匹配 (遍历文件夹-查找文件)
from fnmatch import fnmatch
import os

def test_path_jpg(test_path,search):
    try:
        for root,dirs,files in os.walk(test_path):
            jpg_list = [path for path in files if fnmatch(path.lower(),'*%s'%search)]
            if jpg_list:
                print({test_path:jpg_list})
            for path_down in dirs and dirs:
                path_down = os.path.join(test_path,path_down)
                test_path_jpg(path_down,search)
            return True
    except Exception as er:
        print(er)
        return {'msg':'程序出错'}

if __name__ == '__main__':
    test_path = 'E:\作业'
    search_path = '.png'
    test_path_jpg(test_path,search_path)



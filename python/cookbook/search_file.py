

# python 通配符匹配 (遍历文件夹-查找文件)
from fnmatch import fnmatch
import os

def test_path_jpg(test_path,search):
    try:
        for root,dirs,files in os.walk(test_path):
            jpg_list = [path for path in files if fnmatch(path.lower(),'*%s'%search)]
            if jpg_list:print({test_path:jpg_list})
            for path_down in dirs and dirs:
                path_down = os.path.join(test_path,path_down)
                test_path_jpg(path_down,search)
            return True
    except Exception as er:
        print(er)
        return {'msg':'程序出错'}

# 获取目录结构json
def path_json(test_path, file_json):
    for dir_file in os.listdir(test_path):
        file_path = os.path.join(test_path, dir_file)
        if os.path.isdir(file_path):
            path_json(file_path, file_json)
        else:
            file_json.append(dir_file)
    return file_json

if __name__ == '__main__':
    test_path = 'E:\作业'
    search_path = '.png'
    # test_path_jpg(test_path,search_path)
    file_namelist = path_json(test_path = test_path, file_json = [])
    print(file_namelist)



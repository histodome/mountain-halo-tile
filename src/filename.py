import os
# import pandas as pd

file_path = "/Users/duanqigeng/Desktop/aas"  #文件路径
# path_list = os.listdir(file_path) #遍历整个文件夹下的文件name并返回一个列表

# for i in path_list:
#     path_name.append(i) #若带有后缀名，利用循环遍历path_list列表，split去掉后缀名

def get_all_files(dir):
    files_ = []
    list_ = os.listdir(dir)
    for i in range(0, len(list_)):
        path = os.path.join(dir, list_[i])
        if os.path.isdir(path):
            files_.extend(get_all_files(path))
        if os.path.isfile(path):
            files_.append(path)
    return files_

path_name = get_all_files(file_path)

for file_name in path_name:
    # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有"save.txt"会自动创建
    with open("/Users/duanqigeng/Desktop/aas.txt", "a") as file:
        file.write(file_name + "\n")
        print(file_name)
    file.close()


import os
import pyminizip


def zipdir(path, zipname, password):
    # 获取所有文件和文件夹（包括子文件夹）
    file_paths = []
    relative_paths = []
    filenames = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filenames.append(os.path.basename(file))
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, path)
            file_paths.append(full_path)
            relative_paths.append(relative_path)
    # 解决倒数第二层文件夹为文件名的问题
    for i in range(len(filenames)):
        if filenames[i] in relative_paths[i]:
            relative_paths[i] = relative_paths[i].replace(filenames[i], '')
    # 使用pyminizip压缩文件
    pyminizip.compress_multiple(file_paths, relative_paths, zipname, password, 5)


if __name__ == '__main__':
    # 要压缩的文件夹路径
    dir_to_zip = './ttg/'
    # 压缩文件的名称
    zip_file_name = './zip/your_zip_file.zip'
    # 解压密码
    password = '123456'

    zipdir(dir_to_zip, zip_file_name, password)




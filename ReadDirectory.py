import os


def read_directory(dir_path):
    if os.path.exists(dir_path):
        print(dir_path)
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            if os.path.isfile(file_path):
                print(os.path.join(dir_path, file))
            elif os.path.isdir(file_path):
                print('dir==>', file_path)
                read_directory(file_path)
    else:
        print("No path exists")


if __name__ == '__main__':
    dir_path='/home/shashi/Desktop'
    read_directory(dir_path)
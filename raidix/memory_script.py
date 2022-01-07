import zipfile
import os
from datetime import datetime

disk = os.statvfs("/")
print("calculation of disk usage:")
totalBytes = float(disk.f_bsize*disk.f_blocks)
tb = round(totalBytes/(1024**3), 3)
print("Total space : {} GBytes".format(tb))
totalUsedSpace = float(disk.f_bsize*(disk.f_blocks-disk.f_bfree))
tus = round(totalUsedSpace/(1024**3), 3)
print("Used space : {} GBytes".format(tus))
totalAvailSpace = float(disk.f_bsize*disk.f_bfree)
tas = round(totalAvailSpace/(1024**3), 3)
print("Available space : {} GBytes".format(tas))

current_date = datetime.now().date()
zipPath = str(current_date)+".zip"
final_dir = r'/tmp/'+zipPath
dirPath = '/home/somename/work'     # Вместо somename использовать имя текущего пользователя

file_dir = os.listdir(dirPath)
with zipfile.ZipFile(final_dir, mode='w',
                     compression=zipfile.ZIP_DEFLATED) as zf:
    for file in file_dir:
        add_file = os.path.join(dirPath, file)
        zf.write(add_file)
    print('Создан архив' + final_dir)

GB = 1024**3
size = 1024**3      # Указать предел размера файла
for root, dirs, files in os.walk('directory'):      # Указываем путь к необходимой директории
    for file in files:
        path = os.path.join(root, file)
        if os.stat(path).st_size >= size:
            res_round = round(((int(os.stat(path).st_size)) / GB), 1)
            print(str(res_round) + "Gb")
            print(path + ' ' + str(res_round) + "Gb")
            os.remove(path)
            print("File Deleted")

import os
from pydub import AudioSegment
import shutil

files_folder_name = 'files'

folder_name = '/Volumes/{}/'.format(os.listdir('/Volumes')[1])
folder = [x for x in os.listdir(folder_name) if x.endswith(".aiff")]
name = input('Введите название диска: ')
if not os.path.exists(files_folder_name):
    os.mkdir(files_folder_name)
for f in folder:
    if (not os.path.isfile(files_folder_name + '/' + f)) or ((os.path.isfile(files_folder_name + '/' + f) and os.path.getsize(files_folder_name + '/' + f) != os.path.getsize(folder_name + f))):
        print('Копирование "{}"'.format(f))
        if os.path.isfile(files_folder_name + '/' + f):
            os.remove(files_folder_name + '/' + f)
        shutil.copy(folder_name + f, 'files')
result = AudioSegment.from_file(files_folder_name + '/' + folder[0])
folder = folder[1:]
for i, filename in enumerate(folder):
    result += AudioSegment.from_file(files_folder_name + '/' + filename)
    print('{0:.1f}%'.format(i / len(folder) * 100))
print('{0:.1f}%'.format(100))
while True:
    try:
        result.export(input('Куда сохранить результат? ') + '/' + name + '.mp3', format='mp3')
        break
    except Exception:
        pass
shutil.rmtree(files_folder_name)

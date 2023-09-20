'''

1. Решить задачи, которые не успели решить на семинаре. 
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

'''
import os
from pathlib import Path
import shutil

# Список расширений для каждого типа файлов
EXTENSIONS = {
    "audios": [".mp3", ".wav", ".ogg"],
    "pictures": [".jpg", ".jpeg", ".png"],
    "texts": [".txt", ".docx", ".pdf"],
}

def my_sort_files(path_):
    # Получение списка всех файлов в указаной директории
    my_files_list = os.listdir(path_)
    
    # Создание папок для каждой группы
    for group in EXTENSIONS.keys():
        os.makedirs(os.path.join(path_, group), exist_ok=True)
    
    # Сортировка файлов по группам
    for file in my_files_list:
        file_path = os.path.join(path_, file)   # полный путь к текущему файлу из списка
        if os.path.isfile(file_path):           # проверка что это файл (а не папка)
            for group, extensions in EXTENSIONS.items():
                if any(file.lower().endswith(ext) for ext in extensions): # проверяет, имеет ли имя файла одно из расширений, указанных в списке
                    shutil.move(file_path, os.path.join(path_, group)) # перемещение файла в  соответствующ папку
                    break
    
if __name__=="__main__":
    my_path= Path().cwd() / "homework07" / "task01" / "myfiles"
    print(f"{my_path=}")
    print(f"files: {os.listdir(my_path)}")
    my_sort_files(my_path)
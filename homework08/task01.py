"""
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.

"""
import csv
import json
import pickle
import os

from pathlib import Path
  
def create_file_(dir_, filename_="new_file", size_=100):
    """
    функция создания файла
    """

    # Проверяем, существует ли указанная директория
    if not os.path.exists(dir_):
        # Если директории не существует, создаем ее
        os.makedirs(dir_)

    # Создаем полный путь к файлу
    file_path = os.path.join(dir_, filename_)

    # Открываем файл в режиме записи и записываем указанное количество байт
    with open(file_path, 'wb') as file:
        file.write(b'\0' * size_)

def get_size_(path_):
    total_size = 0
    for dir_path, dir_names, file_names in os.walk(path_):
        for file in file_names:
            file_path = os.path.join(dir_path, file)
            total_size += os.path.getsize(file_path)
    return total_size

def save_directory_info(path_):
    results = []

    # Рекурсивно обходим директорию и все вложенные директории
    for dir_path, dir_names, file_names in os.walk(path_, topdown=True, onerror=None, followlinks=False):



        # добавляем информацию о директории
        dir_info = {
            'path': dir_path,
            'type': 'directory',
            'size': get_size_(dir_path)
        }
        results.append(dir_info)        

        # добавляем информацию о файлах
        for file in file_names:
            file_path = os.path.join(dir_path, file)
            file_info = {
                'path': file_path,
                'type': 'file',
                'size': os.path.getsize(file_path)
            }
            results.append(file_info)


    # Сохраняем результаты обхода в файлы JSON, CSV и pickle
    
    save_path=os.path.join(os.path.dirname(my_path), os.path.basename(path_))

    with open(f'{save_path}.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)

    with open(f'{save_path}.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['path', 'type', 'size'])
        for result in results:
            writer.writerow([result['path'], result['type'], result['size']])

    with open(f'{save_path}.pickle', 'wb') as pickle_file:
        pickle.dump(results, pickle_file)

   


if __name__ == "__main__":
    my_path = Path().cwd() / "homework08" /"myfiles"
    create_file_(my_path,"file00")
    my_path = Path().cwd() / "homework08" /"myfiles"/"dir1"
    create_file_(my_path,"file01",200)
    my_path = Path().cwd() / "homework08" /"myfiles"/"dir2"
    create_file_(my_path,"file02",300)
    create_file_(my_path,"file03",150)
    my_path = Path().cwd() / "homework08" /"myfiles"
    save_directory_info(my_path)
    a_path = os.path.dirname(my_path)
    print(a_path)
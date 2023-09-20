'''
 Напишите функцию группового переименования файлов. Она должна:
    принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
    принимать параметр количество цифр в порядковом номере.
    принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
    принимать параметр расширение конечного файла.
    принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
    К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 
'''
import os
from pathlib import Path

def my_rename_files(path_, source_ext, fin_ext, range_=[0,0], numc=3, new_name="new"):
    """
    Переименование файлов в папке
        path_: Путь к папке с файлами
        new_name: Новое имя для всех файлов (без номера)
        numc: Количество цифр в номере
        source_ext: Расширение исходного файла
        fin_ext: Расширение конечного файла
        range_: Диапазон сохраняемого оригинального имени
    """
    
    files = [file for file in os.listdir(path_) if file.lower().endswith(source_ext) ]
    counter = 1
    
    for file in files:
        
            file_name,ext = os.path.splitext(file)
            file_name = file_name[range_[0]-1:range_[1]] + new_name
            new_file_name = f"{file_name}{str(counter).zfill(numc)}.{fin_ext}"
            os.rename(os.path.join(path_, file), os.path.join(path_, new_file_name))
            counter += 1

if __name__=="__main__":
    my_path= Path().cwd() / "homework07" / "task02" / "myfiles2"
    print(f"{my_path=}")
    print(f"files: {os.listdir(my_path)}")
    my_rename_files(my_path, "txt","txt",numc=2,new_name="olo",range_=[1,2])
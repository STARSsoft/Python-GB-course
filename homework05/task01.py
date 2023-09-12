'''
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
'''
def escape_control_characters(input_string):
    escaped_chars = {
        '\a': '\\a',
        '\n': '\\n',
        '\r': '\\r',
        '\t': '\\t',
        '\b': '\\b',
        '\f': '\\f',
        '\v': '\\v',
    }
    escaped_string = ""
    for char in input_string:
        if char in escaped_chars:
            escaped_string += escaped_chars[char]
        else:
            escaped_string += char
    return escaped_string


def my_func(s):
  e=escape_control_characters(s)
  *path, full_name=e.split("\\")
  *file_name, ext =full_name.split(".")
  file_name=".".join(file_name)
  path="/".join(path)
  return path,file_name,ext


s="C:\ИГРЫ(рус)\Balbdur's Gate 3\ate.3\bin.file.xyz\tg.my.game.exe"
print(my_func(s))

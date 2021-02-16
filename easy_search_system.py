import os

files_frequency = {}
files_paths = {}
list_of_files = []

#получение списка текстовых файлов
def get_list_of_files(list_of_files):
    directory = os.getcwd()
    local_list_files = [file for file in os.listdir(directory) if file.endswith(".txt") and file not in list_of_files]
    list_of_files += local_list_files
    return list_of_files

list_of_files = get_list_of_files(list_of_files)

print(list_of_files)
#словарь с названием файла и его путь
def get_files_paths(list_of_files, files_paths):
    files_paths.update({file: os.path.abspath(file) for file in list_of_files})
    return files_paths

get_files_paths(list_of_files, files_paths)


#вычисления частотности
def get_frequency(file_name: str) -> dict:
    with open(file_name) as data_file:
        info = data_file.read().lower().replace('\n', ' ')
        list_of_words = info.split(' ')

        # создаем сет с словами, чтобы потом для них найти частотность
        one_copy_of_word = set(list_of_words)

        #создаем список с частнотностью слов
        list_frequency = [list_of_words.count(word) for word in one_copy_of_word]

        frequency_of_words = {word: frequency for word, frequency in zip(one_copy_of_word, list_frequency)}
        return frequency_of_words


#частотность слова в тексте
def add_frequency_to_dict(list_of_files: list) -> dict:
    for file_name in list_of_files:
        files_frequency[file_name] = get_frequency(file_name)
    return files_frequency


add_frequency_to_dict(list_of_files)

for key, value in files_frequency.items():
    print(key, value)
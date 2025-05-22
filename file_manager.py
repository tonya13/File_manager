import os
import shutil
from config import WORKING_DIRECTORY


class FileManager:
    def __init__(self):
        self.current_directory = WORKING_DIRECTORY

    def change_directory(self, path):
        """Сменить рабочую директорию."""
        new_path = os.path.join(self.current_directory, path)
        if os.path.isdir(new_path):
            self.current_directory = new_path
            print(f"Текущая директория: {self.current_directory}")
        else:
            print("Ошибка: Папка не существует.")

    def list_files(self):
        """Отображение файлов и папок в текущей директории."""
        files = os.listdir(self.current_directory)
        for file in files:
            print(file)

    def create_directory(self, name):
        """Создание новой папки."""
        new_dir = os.path.join(self.current_directory, name)
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
            print(f"Папка {name} успешно создана.")
        else:
            print("Ошибка: Папка уже существует.")

    def delete_directory(self, name):
        """Удаление папки."""
        dir_path = os.path.join(self.current_directory, name)
        if os.path.isdir(dir_path):
            os.rmdir(dir_path)
            print(f"Папка {name} удалена.")
        else:
            print("Ошибка: Папка не существует.")

    def create_file(self, name):
        """Создание нового файла."""
        file_path = os.path.join(self.current_directory, name)
        with open(file_path, 'w') as f:
            f.write("")
        print(f"Файл {name} успешно создан.")

    def delete_file(self, name):
        """Удаление файла."""
        file_path = os.path.join(self.current_directory, name)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Файл {name} удален.")
        else:
            print("Ошибка: Файл не существует.")

    def rename_file(self, old_name, new_name):
        """Переименование файла."""
        old_file = os.path.join(self.current_directory, old_name)
        new_file = os.path.join(self.current_directory, new_name)
        if os.path.isfile(old_file):
            os.rename(old_file, new_file)
            print(f"Файл {old_name} переименован в {new_name}.")
        else:
            print("Ошибка: Файл не существует.")

    def copy_file(self, src, dest):
        """Копирование файла."""
        src_file = os.path.join(self.current_directory, src)
        dest_file = os.path.join(self.current_directory, dest)
        if os.path.isfile(src_file):
            shutil.copy(src_file, dest_file)
            print(f"Файл {src} скопирован в {dest}.")
        else:
            print("Ошибка: Файл не существует.")

    def move_file(self, src, dest):
        """Перемещение файла."""
        src_file = os.path.join(self.current_directory, src)
        dest_file = os.path.join(self.current_directory, dest)
        if os.path.isfile(src_file):
            shutil.move(src_file, dest_file)
            print(f"Файл {src} перемещен в {dest}.")
        else:
            print("Ошибка: Файл не существует.")

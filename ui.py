# ui.py
import os
from file_manager import FileManager


def show_menu():
    print("Файловый менеджер")
    print("1. Показать файлы")
    print("2. Создать файл")
    print("3. Удалить файл")
    print("4. Переименовать файл")
    print("5. Копировать файл")
    print("6. Переместить файл")
    print("7. Создать папку")
    print("8. Удалить папку")
    print("9. Перейти в папку")
    print("10. Выйти")


def main():
    file_manager = FileManager()

    while True:
        show_menu()
        choice = input("Выберите опцию: ")

        if choice == '1':
            file_manager.list_files()
        elif choice == '2':
            file_name = input("Введите имя файла для создания: ")
            file_manager.create_file(file_name)
        elif choice == '3':
            file_name = input("Введите имя файла для удаления: ")
            file_manager.delete_file(file_name)
        elif choice == '4':
            old_name = input("Введите старое имя файла: ")
            new_name = input("Введите новое имя файла: ")
            file_manager.rename_file(old_name, new_name)
        elif choice == '5':
            src = input("Введите имя файла для копирования: ")
            dest = input("Введите имя файла назначения: ")
            file_manager.copy_file(src, dest)
        elif choice == '6':
            src = input("Введите имя файла для перемещения: ")
            dest = input("Введите имя папки назначения: ")
            file_manager.move_file(src, dest)
        elif choice == '7':
            folder_name = input("Введите имя папки для создания: ")
            file_manager.create_directory(folder_name)
        elif choice == '8':
            folder_name = input("Введите имя папки для удаления: ")
            file_manager.delete_directory(folder_name)
        elif choice == '9':
            folder_path = input("Введите путь к папке: ")
            file_manager.change_directory(folder_path)
        elif choice == '10':
            print("Выход из файлового менеджера.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()

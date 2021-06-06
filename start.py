import os
from moviepy.editor import *
from moviepy.editor import TextClip,VideoFileClip, concatenate_videoclips
dir_name_main = "Z:\\slideshow\\" # The directory contains other directories - Каталог содержит другие каталоги
dir_name_output = "Z:\\slideshow_out" # Directory for saving files mp4 - Каталог для сохранения файлов mp4
python_scrypt = "slideshow.py" # Script to start generating the mp4 file - Скрипт для запуска формирования файла mp4
Video_type = 4 #  1 - 720х480, 2 - 854x480, 3 - 1280x720, 4 - 1920x1080,  5 - 3840x2160 - Разрешение для видео
def save_file_busy(fname):
    f = open(fname,"a")
    f.write("busy")
    f.close()

def main() : 
    global dir_name_main,dir_name_output,python_scrypt
    # Создать каталог если он не существует
    if os.path.isdir(dir_name_output) == False:
        os.mkdir(dir_name_output)
    dir_names = os.listdir(dir_name_main) # We read the contents of the directory - Читаем содержимое каталога
    is_found_dir = False # Found directory attribute - Признак найденного каталога 
    fname_mp4 = ""
    dir_fullname = ""
    fname_busy = ""
    for dir_name in dir_names:
        dir_fullname = os.path.join(dir_name_main, dir_name) # We get the full name - Получаем полное имя
        fname_mp4 = dir_name + "_ns.mp4" # Mp4 file name - Название файла mp4
        print("File ",dir_name) # Display the current directory - Выводим текущий каталог  
        print("Fullname ",dir_fullname) # Displaying the full directory name - Выводим полное имя каталога
        print("File mp4 ",fname_mp4) # Displaying the name of the mp4 file - Выводим название файла mp4
        if not os.path.isdir(dir_fullname) :
            print("Directory not found ",dir_fullname) # Не найден каталог
            continue
        fname_busy = os.path.join(dir_fullname, "busy.txt") # Flag filename taken - Имя файла с флагом занято  
        if os.path.isfile(fname_busy) :  
            print("Found file ",fname_busy) # Найден файл
            continue
        is_found_dir = True
        break

    if is_found_dir :
        save_file_busy(fname_busy) # Save the flag is busy - Сохранение флага занято
        str_exec = python_scrypt + " "+dir_fullname+" "+fname_mp4 +" " + dir_name_output + " " + str(Video_type) # form a string for execution - формируем строку для выполнения
        print("Execute ",str_exec) # Displaying - Выводим на экран
        os.system(str_exec) # Run the script for execution - Запускаем скрипт на выполнение
  
if __name__ == "__main__":
    main()    
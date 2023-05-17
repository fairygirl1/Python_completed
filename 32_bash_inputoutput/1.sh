#Перенаправьте ввод так чтобы выполнить команды хранящиеся 
# в файле file_for_1st_task.txt
#если возникнут ошибки перенаправьте в файл errors
#в конце очистите файл не удаляя его

#!/bin/bash

# Выполнение команд из файла и перенаправление ошибок в файл errors
bash < file_for_1st_task.txt 2> errors

# Очистка файла без его удаления
> file_for_1st_task.txt


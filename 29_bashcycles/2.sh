# выведите отдельные слова из файла filefortask2.txt в столбик

#!/bin/bash

contents=$(cat file_2_task.txt)
echo "$contents" | tr ';' '\n'


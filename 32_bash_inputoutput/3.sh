# напишите скрипт который выводит надпись "Bash - это лучшее что может быть" 20 раз в консоль
# если передан ключ -f то после него идет имя файла в который перенаправляется вывод

#!/bin/bash

message="Bash - это лучшее что может быть"
count=20

# Проверка наличия ключа -f
if [ "$1" = "-f" ]; then
    if [ -n "$2" ]; then
        output_file="$2"
        for ((i=1; i<=$count; i++)); do
            echo "$message"
        done > "$output_file"
        echo "Вывод сохранен в файл: $output_file"
    else
        echo "Не указано имя файла для перенаправления вывода"
    fi
else
    for ((i=1; i<=$count; i++)); do
        echo "$message"
    done
fi

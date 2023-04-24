#Напишите скрипт который принимает 2 аргумента и записывает первый аргумент в файл где имя файла второй аргумент.

#!/bin/bash

if [ $# -lt 2 ]; then
  echo "Usage: $0 <text> <filename>"
  exit 1
fi

echo "$1" > "$2"
echo "Text written to file $2"

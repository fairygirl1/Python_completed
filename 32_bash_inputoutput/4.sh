# создайте скрипт который выводит числа от 1 до 30
# четные числа перенаправляются в файл имя которого передается скрипту в качестве параметра
# нечетные числа выводятся в консоль

#!/bin/bash

output_file="$1"

for ((i=1; i<=30; i++)); do
  if ((i % 2 == 0)); then
    echo $i >> "$output_file"
  else
    echo $i
  fi
done

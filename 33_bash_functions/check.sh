
check_admission() {
  score=$1

  if ((score > 50)); then
    echo "True"
  else
    echo "False"
  fi
}
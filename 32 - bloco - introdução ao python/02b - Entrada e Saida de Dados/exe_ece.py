alunos = open("alunos_notas.txt",  mode="w")

alunos.writelines([
"Marcos 10\n", "Felipe 4\n", "José 6\n", "Ana 10\n", "Maria 9\n", "Miguel 5\n"
])

alunos.close()





recuStudents = []
gradesFile = open("alunos_notas.txt", mode="r")
content = gradesFile.read().split("\n")
for index in content:
  index = index.split(" ")
  if (int(index[1]) < 6):
    print(index[0])











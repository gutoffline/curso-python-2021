"""
fruta1 = "maçã"
fruta2 = "laranja"
fruta3 = "morango"

frutas = ["maçã" , "laranja" , "morango"]

print(frutas)
print(frutas[1])
frutas[1] = "Banana"
print(frutas)
"""
materias = ["Portugês", "Matemática", "História"]
alunos = ["Antonio", "Giovana", "Mariane"]

print(materias)
print(alunos)

#corrigir o nome da Giovana para Geovana
alunos[1] = "Geovana"
print(alunos)

#acrescentar as matérias de física, química e biologia
materias.append("Física")
materias.append("Química")
materias.insert(0,"Biologia")
print(materias)

#remover a aluna mariane
alunos.remove("Mariane")
print(alunos)

#matricular o tomaz e a jaqueline
alunos.extend(["Tomaz","Jaqueline"])
print(alunos)

#verificar quantos alunos estão matriculados
print(len(alunos))

#remover a matéria Biologia
materias.pop(0)
print(materias)

#remover todos os alunos
alunos.clear()
print(alunos)